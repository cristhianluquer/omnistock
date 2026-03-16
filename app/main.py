#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from config import get_db, SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# ── Decoradores ────────────────────────────────────────────────────────────
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            flash('Debes iniciar sesión', 'error')
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated

def admin_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if session.get('user_rol') != 1:
            flash('Solo el administrador puede acceder', 'error')
            return redirect(url_for('dashboard'))
        return f(*args, **kwargs)
    return decorated

# ── HEALTH ─────────────────────────────────────────────────────────────────
@app.route('/health')
def health():
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM omnistock.INFORMATION_SCHEMA.TABLES")
        tables = cur.fetchone()[0]; conn.close()
        return jsonify({"status": "healthy", "tables": tables})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# ── LOGIN ──────────────────────────────────────────────────────────────────
@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        usuario  = request.form.get('usuario', '').strip()
        password = request.form.get('password', '').strip()
        if not usuario or not password:
            flash('Completa todos los campos', 'error')
            return render_template('login.html')
        try:
            conn = get_db(); cur = conn.cursor()
            cur.execute("""
                SELECT u.id_usuario, u.nombre_completo, u.password_hash,
                       u.id_rol, r.nombre_rol
                FROM Usuarios u
                JOIN Roles r ON u.id_rol = r.id_rol
                WHERE u.nombre_usuario = ? AND u.activo = 1
            """, usuario)
            user = cur.fetchone(); conn.close()
            if user and check_password_hash(user.password_hash, password):
                session['user_id']         = user.id_usuario
                session['user_nombre']     = user.nombre_completo
                session['user_rol']        = user.id_rol
                session['user_rol_nombre'] = user.nombre_rol
                flash(f'Bienvenido, {user.nombre_completo}', 'success')
                return redirect(url_for('dashboard'))
            flash('Usuario o contraseña incorrectos', 'error')
        except Exception as e:
            flash(f'Error de conexión: {str(e)}', 'error')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

# ── DASHBOARD ──────────────────────────────────────────────────────────────
@app.route('/dashboard')
@login_required
def dashboard():
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM Productos WHERE activo=1"); tp = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM Clientes WHERE activo=1");  tc = cur.fetchone()[0]
        cur.execute("SELECT COUNT(*) FROM Ventas");                   tv = cur.fetchone()[0]
        cur.execute("SELECT ISNULL(SUM(total),0) FROM Ventas");       sv = cur.fetchone()[0]
        cur.execute("""
            SELECT TOP 5 nombre_producto, stock_actual, stock_minimo
            FROM Productos WHERE activo=1 AND stock_actual <= stock_minimo
            ORDER BY stock_actual ASC
        """)
        alertas = cur.fetchall()
        cur.execute("""
            SELECT TOP 5 v.id_venta, ISNULL(c.nombre_completo,'Cliente general') as cliente,
                   v.total, v.fecha_venta
            FROM Ventas v LEFT JOIN Clientes c ON v.id_cliente=c.id_cliente
            ORDER BY v.fecha_venta DESC
        """)
        ultimas_ventas = cur.fetchall(); conn.close()
    except Exception as e:
        flash(f'Error: {str(e)}', 'error')
        tp=tc=tv=sv=0; alertas=ultimas_ventas=[]
    return render_template('dashboard.html',
        total_productos=tp, total_clientes=tc,
        total_ventas=tv, suma_ventas=sv,
        alertas=alertas, ultimas_ventas=ultimas_ventas)

# ── PRODUCTOS ──────────────────────────────────────────────────────────────
@app.route('/productos')
@login_required
def productos():
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            SELECT p.id_producto, p.nombre_producto, p.descripcion,
                   p.precio_venta, p.stock_actual, p.stock_minimo,
                   ISNULL(c.nombre_categoria,'Sin categoría') as categoria,
                   p.id_categoria
            FROM Productos p
            LEFT JOIN Categorias c ON p.id_categoria=c.id_categoria
            WHERE p.activo=1 ORDER BY p.nombre_producto
        """)
        lista = cur.fetchall()
        cur.execute("SELECT id_categoria, nombre_categoria FROM Categorias ORDER BY nombre_categoria")
        cats = cur.fetchall(); conn.close()
    except Exception as e:
        flash(f'Error: {str(e)}', 'error'); lista=cats=[]
    return render_template('productos.html', productos=lista, categorias=cats)

@app.route('/productos/crear', methods=['POST'])
@login_required
def crear_producto():
    nombre = request.form.get('nombre','').strip()
    if not nombre: flash('Nombre obligatorio','error'); return redirect(url_for('productos'))
    try:
        conn = get_db(); cur = conn.cursor()
        import random, string
        codigo = 'PROD-' + ''.join(random.choices(string.digits, k=6))
        cur.execute("""
            INSERT INTO Productos (codigo_producto, nombre_producto, descripcion, precio_venta,
                                   precio_compra, stock_actual, stock_minimo, id_categoria)
            VALUES (?,?,?,?,?,?,?,?)
        """, codigo, nombre,
             request.form.get('descripcion',''),
             request.form.get('precio_venta', 0),
             request.form.get('precio_compra', 0),
             request.form.get('stock_actual', 0),
             request.form.get('stock_minimo', 5),
             request.form.get('id_categoria') or None)
        conn.commit(); conn.close()
        flash(f'Producto "{nombre}" creado', 'success')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('productos'))

@app.route('/productos/editar/<int:id>', methods=['POST'])
@login_required
def editar_producto(id):
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            UPDATE Productos SET nombre_producto=?, descripcion=?,
                   precio_venta=?, precio_compra=?, stock_actual=?,
                   stock_minimo=?, id_categoria=?
            WHERE id_producto=?
        """, request.form.get('nombre'),
             request.form.get('descripcion',''),
             request.form.get('precio_venta',0),
             request.form.get('precio_compra',0),
             request.form.get('stock_actual',0),
             request.form.get('stock_minimo',5),
             request.form.get('id_categoria') or None, id)
        conn.commit(); conn.close()
        flash('Producto actualizado','success')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('productos'))

@app.route('/productos/eliminar/<int:id>')
@login_required
def eliminar_producto(id):
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("UPDATE Productos SET activo=0 WHERE id_producto=?", id)
        conn.commit(); conn.close()
        flash('Producto eliminado','info')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('productos'))

# ── CLIENTES ───────────────────────────────────────────────────────────────
@app.route('/clientes')
@login_required
def clientes():
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            SELECT id_cliente, tipo_documento, numero_documento,
                   nombre_completo, email, telefono, direccion, ciudad
            FROM Clientes WHERE activo=1 ORDER BY nombre_completo
        """)
        lista = cur.fetchall(); conn.close()
    except Exception as e: flash(f'Error: {str(e)}','error'); lista=[]
    return render_template('clientes.html', clientes=lista)

@app.route('/clientes/crear', methods=['POST'])
@login_required
def crear_cliente():
    nombre = request.form.get('nombre','').strip()
    if not nombre: flash('Nombre obligatorio','error'); return redirect(url_for('clientes'))
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            INSERT INTO Clientes (tipo_documento, numero_documento, nombre_completo,
                                  email, telefono, direccion, ciudad)
            VALUES (?,?,?,?,?,?,?)
        """, request.form.get('tipo_documento','CC'),
             request.form.get('numero_documento',''),
             nombre,
             request.form.get('email',''),
             request.form.get('telefono',''),
             request.form.get('direccion',''),
             request.form.get('ciudad',''))
        conn.commit(); conn.close()
        flash(f'Cliente "{nombre}" registrado','success')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('clientes'))

@app.route('/clientes/editar/<int:id>', methods=['POST'])
@login_required
def editar_cliente(id):
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            UPDATE Clientes SET tipo_documento=?, numero_documento=?,
                   nombre_completo=?, email=?, telefono=?, direccion=?, ciudad=?
            WHERE id_cliente=?
        """, request.form.get('tipo_documento'),
             request.form.get('numero_documento'),
             request.form.get('nombre'),
             request.form.get('email'),
             request.form.get('telefono'),
             request.form.get('direccion'),
             request.form.get('ciudad'), id)
        conn.commit(); conn.close()
        flash('Cliente actualizado','success')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('clientes'))

@app.route('/clientes/eliminar/<int:id>')
@login_required
def eliminar_cliente(id):
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("UPDATE Clientes SET activo=0 WHERE id_cliente=?", id)
        conn.commit(); conn.close()
        flash('Cliente eliminado','info')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('clientes'))

# ── VENTAS ─────────────────────────────────────────────────────────────────
@app.route('/ventas')
@login_required
def ventas():
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            SELECT v.id_venta, v.numero_factura,
                   ISNULL(c.nombre_completo,'Cliente general') as cliente,
                   u.nombre_completo as vendedor,
                   v.total, v.estado, v.fecha_venta
            FROM Ventas v
            LEFT JOIN Clientes c ON v.id_cliente=c.id_cliente
            JOIN Usuarios u ON v.id_usuario=u.id_usuario
            ORDER BY v.fecha_venta DESC
        """)
        lista = cur.fetchall()
        cur.execute("SELECT id_cliente, nombre_completo FROM Clientes WHERE activo=1 ORDER BY nombre_completo")
        cls = cur.fetchall()
        cur.execute("""
            SELECT id_producto, nombre_producto, precio_venta, stock_actual
            FROM Productos WHERE activo=1 AND stock_actual>0 ORDER BY nombre_producto
        """)
        prods = cur.fetchall(); conn.close()
    except Exception as e: flash(f'Error: {str(e)}','error'); lista=cls=prods=[]
    return render_template('ventas.html', ventas=lista, clientes=cls, productos=prods)

@app.route('/ventas/crear', methods=['POST'])
@login_required
def crear_venta():
    id_cliente = request.form.get('id_cliente') or None
    pids       = request.form.getlist('producto_id[]')
    qtys       = request.form.getlist('cantidad[]')
    if not pids: flash('Agrega al menos un producto','error'); return redirect(url_for('ventas'))
    try:
        conn = get_db(); cur = conn.cursor()
        total=0; items=[]
        for pid, qty in zip(pids, qtys):
            qty = int(qty)
            if qty <= 0: continue
            cur.execute("SELECT precio_venta, stock_actual FROM Productos WHERE id_producto=? AND activo=1", pid)
            prod = cur.fetchone()
            if not prod: continue
            if prod.stock_actual < qty:
                flash(f'Stock insuficiente para producto #{pid}','error')
                conn.close(); return redirect(url_for('ventas'))
            sub = float(prod.precio_venta) * qty
            total += sub
            items.append((int(pid), qty, float(prod.precio_venta), sub))
        if not items: flash('No hay productos válidos','error'); return redirect(url_for('ventas'))

        # Número de factura automático
        cur.execute("SELECT ISNULL(MAX(id_venta),0)+1 FROM Ventas")
        num = cur.fetchone()[0]
        numero_factura = f"FAC-{num:04d}"

        cur.execute("""
            INSERT INTO Ventas (numero_factura, id_cliente, id_usuario, total, estado)
            VALUES (?,?,?,?,'COMPLETADA'); SELECT SCOPE_IDENTITY();
        """, numero_factura, id_cliente, session['user_id'], total)
        cur.nextset()
        vid = int(cur.fetchone()[0])

        for pid, qty, precio, sub in items:
            cur.execute("""
                INSERT INTO Detalles_Venta (id_venta, id_producto, cantidad, precio_unitario, subtotal)
                VALUES (?,?,?,?,?)
            """, vid, pid, qty, precio, sub)
            cur.execute("UPDATE Productos SET stock_actual=stock_actual-? WHERE id_producto=?", qty, pid)

        conn.commit(); conn.close()
        flash(f'Venta {numero_factura} registrada — Total: ${total:,.2f}','success')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('ventas'))

@app.route('/ventas/<int:id>/detalle')
@login_required
def detalle_venta(id):
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            SELECT v.id_venta, v.numero_factura,
                   ISNULL(c.nombre_completo,'Cliente general') as cliente,
                   u.nombre_completo as vendedor,
                   v.total, v.estado, v.fecha_venta
            FROM Ventas v
            LEFT JOIN Clientes c ON v.id_cliente=c.id_cliente
            JOIN Usuarios u ON v.id_usuario=u.id_usuario
            WHERE v.id_venta=?
        """, id)
        venta = cur.fetchone()
        cur.execute("""
            SELECT p.nombre_producto, dv.cantidad, dv.precio_unitario, dv.subtotal
            FROM Detalles_Venta dv
            JOIN Productos p ON dv.id_producto=p.id_producto
            WHERE dv.id_venta=?
        """, id)
        detalle = cur.fetchall(); conn.close()
    except Exception as e:
        flash(f'Error: {str(e)}','error'); return redirect(url_for('ventas'))
    return render_template('detalle_venta.html', venta=venta, detalle=detalle)

# ── USUARIOS ───────────────────────────────────────────────────────────────
@app.route('/usuarios')
@login_required
@admin_required
def usuarios():
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            SELECT u.id_usuario, u.nombre_completo, u.nombre_usuario,
                   u.email, r.nombre_rol
            FROM Usuarios u JOIN Roles r ON u.id_rol=r.id_rol
            WHERE u.activo=1 ORDER BY u.nombre_completo
        """)
        lista = cur.fetchall()
        cur.execute("SELECT id_rol, nombre_rol FROM Roles ORDER BY id_rol")
        roles = cur.fetchall(); conn.close()
    except Exception as e: flash(f'Error: {str(e)}','error'); lista=roles=[]
    return render_template('usuarios.html', usuarios=lista, roles=roles)

@app.route('/usuarios/crear', methods=['POST'])
@login_required
@admin_required
def crear_usuario():
    nombre   = request.form.get('nombre','').strip()
    usuario  = request.form.get('usuario','').strip()
    password = request.form.get('password','').strip()
    if not all([nombre, usuario, password]):
        flash('Nombre, usuario y contraseña son obligatorios','error')
        return redirect(url_for('usuarios'))
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            INSERT INTO Usuarios (nombre_usuario, email, password_hash, nombre_completo, id_rol)
            VALUES (?,?,?,?,?)
        """, usuario,
             request.form.get('email',''),
             generate_password_hash(password, method='pbkdf2:sha256'),
             nombre,
             request.form.get('id_rol', 2))
        conn.commit(); conn.close()
        flash(f'Usuario "{usuario}" creado','success')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('usuarios'))

@app.route('/usuarios/eliminar/<int:id>')
@login_required
@admin_required
def eliminar_usuario(id):
    if id == session.get('user_id'):
        flash('No puedes eliminar tu propio usuario','error')
        return redirect(url_for('usuarios'))
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("UPDATE Usuarios SET activo=0 WHERE id_usuario=?", id)
        conn.commit(); conn.close()
        flash('Usuario desactivado','info')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('usuarios'))

# ── CATEGORÍAS ─────────────────────────────────────────────────────────────
@app.route('/categorias')
@login_required
def categorias():
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("""
            SELECT c.id_categoria, c.nombre_categoria, COUNT(p.id_producto) as total
            FROM Categorias c
            LEFT JOIN Productos p ON c.id_categoria=p.id_categoria AND p.activo=1
            GROUP BY c.id_categoria, c.nombre_categoria
            ORDER BY c.nombre_categoria
        """)
        lista = cur.fetchall(); conn.close()
    except Exception as e: flash(f'Error: {str(e)}','error'); lista=[]
    return render_template('categorias.html', categorias=lista)

@app.route('/categorias/crear', methods=['POST'])
@login_required
def crear_categoria():
    nombre = request.form.get('nombre','').strip()
    if not nombre: flash('Nombre obligatorio','error'); return redirect(url_for('categorias'))
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("INSERT INTO Categorias (nombre_categoria) VALUES (?)", nombre)
        conn.commit(); conn.close()
        flash(f'Categoría "{nombre}" creada','success')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('categorias'))

@app.route('/categorias/eliminar/<int:id>')
@login_required
@admin_required
def eliminar_categoria(id):
    try:
        conn = get_db(); cur = conn.cursor()
        cur.execute("DELETE FROM Categorias WHERE id_categoria=?", id)
        conn.commit(); conn.close()
        flash('Categoría eliminada','info')
    except Exception as e: flash(f'Error: {str(e)}','error')
    return redirect(url_for('categorias'))

if __name__ == '__main__':
    print("🚀 Iniciando OmniStock...")
    print("🌐 http://localhost:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)