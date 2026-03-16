#!/usr/bin/env python3
"""
Ejecuta este script UNA VEZ para crear el usuario administrador.
Uso: python3 crear_admin.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
 
from werkzeug.security import generate_password_hash
from config import get_db
 
def crear_admin():
    nombre   = "Administrador"
    usuario  = "admin"
    email    = "admin@omnistock.com"
    password = "admin123"
    rol_id   = 1
 
    phash = generate_password_hash(password)
 
    try:
        conn = get_db()
        cur = conn.cursor()
 
        # Verificar si ya existe
        cur.execute("SELECT id FROM usuarios WHERE usuario = ?", usuario)
        if cur.fetchone():
            print(f"⚠️  El usuario '{usuario}' ya existe.")
            print("    Actualizando contraseña...")
            cur.execute("UPDATE usuarios SET password_hash=? WHERE usuario=?", phash, usuario)
        else:
            cur.execute("""
                INSERT INTO usuarios (nombre, usuario, email, password_hash, rol_id)
                VALUES (?, ?, ?, ?, ?)
            """, nombre, usuario, email, phash, rol_id)
            print(f"✅ Usuario administrador creado exitosamente")
 
        conn.commit()
        conn.close()
        print(f"\n📋 Credenciales de acceso:")
        print(f"   Usuario:    {usuario}")
        print(f"   Contraseña: {password}")
        print(f"\n🌐 Inicia la app con: python3 main.py")
        print(f"   Luego ve a:         http://localhost:5000")
 
    except Exception as e:
        print(f"❌ Error: {e}")
        print("\n🔍 Verifica que:")
        print("   1. Docker esté corriendo (Mac): docker start omnistock-sqlserver")
        print("   2. SQL Server Express esté iniciado (Windows)")
        print("   3. La base de datos OmniStock esté creada (database/omnistock.sql)")
        sys.exit(1)
 
if __name__ == '__main__':
    crear_admin()
 