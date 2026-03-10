# Documentación del Modelo de Datos - OmniStock

## 1. Introducción

Este documento describe el modelo de datos del sistema OmniStock, un sistema de gestión de inventario y ventas desarrollado en Python con SQL Server como base de datos.

## 2. Objetivos del Modelo

- **Normalización**: El modelo está normalizado hasta la tercera forma normal (3NF)
- **Integridad**: Uso de claves foráneas y restricciones para mantener la integridad referencial
- **Rendimiento**: Índices estratégicos para optimizar consultas frecuentes
- **Trazabilidad**: Registro de movimientos de inventario y auditoría de operaciones

## 3. Entidades Principales

### 3.1. Roles
**Propósito**: Define los roles de usuario del sistema para control de acceso.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_rol | INT (PK) | Identificador único del rol |
| nombre_rol | VARCHAR(50) | Nombre del rol (Administrador, Vendedor, Almacenista) |
| descripcion | VARCHAR(255) | Descripción del rol |
| activo | BIT | Estado del rol (1=activo, 0=inactivo) |
| fecha_creacion | DATETIME | Fecha de creación del registro |

**Roles por defecto**:
- Administrador: Acceso completo al sistema
- Vendedor: Puede realizar ventas y consultar información
- Almacenista: Gestiona productos e inventario

---

### 3.2. Usuarios
**Propósito**: Almacena información de usuarios del sistema con autenticación.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_usuario | INT (PK) | Identificador único del usuario |
| nombre_usuario | VARCHAR(50) | Nombre de usuario único para login |
| email | VARCHAR(100) | Correo electrónico único |
| password_hash | VARCHAR(255) | Contraseña hasheada (usar bcrypt o similar) |
| nombre_completo | VARCHAR(100) | Nombre completo del usuario |
| id_rol | INT (FK) | Referencia al rol del usuario |
| activo | BIT | Estado del usuario |
| fecha_creacion | DATETIME | Fecha de registro |
| ultimo_acceso | DATETIME | Última vez que el usuario accedió al sistema |

**Seguridad**: 
- Las contraseñas deben ser hasheadas antes de almacenarse
- Implementar validación de email único
- Registrar último acceso para auditoría

---

### 3.3. Categorias
**Propósito**: Organiza los productos en categorías.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_categoria | INT (PK) | Identificador único de la categoría |
| nombre_categoria | VARCHAR(100) | Nombre único de la categoría |
| descripcion | VARCHAR(255) | Descripción de la categoría |
| activo | BIT | Estado de la categoría |
| fecha_creacion | DATETIME | Fecha de creación |

---

### 3.4. Productos
**Propósito**: Almacena información de productos del inventario.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_producto | INT (PK) | Identificador único del producto |
| codigo_producto | VARCHAR(50) | Código único del producto (SKU) |
| nombre_producto | VARCHAR(200) | Nombre del producto |
| descripcion | VARCHAR(500) | Descripción detallada |
| id_categoria | INT (FK) | Categoría a la que pertenece |
| precio_venta | DECIMAL(10,2) | Precio de venta al público |
| precio_compra | DECIMAL(10,2) | Precio de compra al proveedor |
| stock_actual | INT | Cantidad actual en inventario |
| stock_minimo | INT | Nivel mínimo de stock (alerta) |
| unidad_medida | VARCHAR(20) | Unidad de medida (UNIDAD, KG, LITRO, etc.) |
| activo | BIT | Estado del producto |
| fecha_creacion | DATETIME | Fecha de creación |
| fecha_actualizacion | DATETIME | Última actualización |

**Validaciones**:
- Precios deben ser >= 0
- Stock actual y mínimo deben ser >= 0
- Código de producto debe ser único

---

### 3.5. Clientes
**Propósito**: Almacena información de clientes.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_cliente | INT (PK) | Identificador único del cliente |
| tipo_documento | VARCHAR(10) | Tipo: CC, NIT, CE, PASAPORTE |
| numero_documento | VARCHAR(20) | Número de documento único |
| nombre_completo | VARCHAR(200) | Nombre completo o razón social |
| email | VARCHAR(100) | Correo electrónico |
| telefono | VARCHAR(20) | Teléfono de contacto |
| direccion | VARCHAR(255) | Dirección |
| ciudad | VARCHAR(100) | Ciudad |
| activo | BIT | Estado del cliente |
| fecha_creacion | DATETIME | Fecha de registro |
| fecha_actualizacion | DATETIME | Última actualización |

---

### 3.6. Ventas
**Propósito**: Encabezado de las transacciones de venta.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_venta | INT (PK) | Identificador único de la venta |
| numero_factura | VARCHAR(50) | Número de factura único |
| id_cliente | INT (FK) | Cliente que realiza la compra |
| id_usuario | INT (FK) | Usuario que registra la venta |
| fecha_venta | DATETIME | Fecha y hora de la venta |
| subtotal | DECIMAL(10,2) | Subtotal antes de impuestos |
| impuesto | DECIMAL(10,2) | Valor de impuestos |
| descuento | DECIMAL(10,2) | Descuento aplicado |
| total | DECIMAL(10,2) | Total a pagar |
| estado | VARCHAR(20) | COMPLETADA, CANCELADA, ANULADA |
| observaciones | VARCHAR(500) | Notas adicionales |
| fecha_creacion | DATETIME | Fecha de registro |

**Cálculo**: total = subtotal + impuesto - descuento

---

### 3.7. Detalles_Venta
**Propósito**: Detalle de productos vendidos en cada venta.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_detalle | INT (PK) | Identificador único del detalle |
| id_venta | INT (FK) | Venta a la que pertenece |
| id_producto | INT (FK) | Producto vendido |
| cantidad | INT | Cantidad vendida |
| precio_unitario | DECIMAL(10,2) | Precio unitario al momento de la venta |
| descuento | DECIMAL(10,2) | Descuento aplicado al detalle |
| subtotal | DECIMAL(10,2) | Subtotal del detalle |

**Cálculo**: subtotal = (cantidad * precio_unitario) - descuento

**Cascada**: Si se elimina una venta, se eliminan sus detalles automáticamente.

---

### 3.8. Movimientos_Inventario
**Propósito**: Registro histórico de todos los movimientos de inventario.

| Campo | Tipo | Descripción |
|-------|------|-------------|
| id_movimiento | INT (PK) | Identificador único del movimiento |
| id_producto | INT (FK) | Producto afectado |
| tipo_movimiento | VARCHAR(20) | ENTRADA, SALIDA, AJUSTE |
| cantidad | INT | Cantidad del movimiento |
| cantidad_anterior | INT | Stock antes del movimiento |
| cantidad_nueva | INT | Stock después del movimiento |
| motivo | VARCHAR(255) | Razón del movimiento |
| id_usuario | INT (FK) | Usuario que registra el movimiento |
| id_venta | INT (FK) | Si el movimiento es por venta |
| fecha_movimiento | DATETIME | Fecha y hora del movimiento |

**Tipos de movimiento**:
- **ENTRADA**: Aumento de stock (compra, devolución)
- **SALIDA**: Disminución de stock (venta, pérdida)
- **AJUSTE**: Corrección de inventario

---

## 4. Relaciones

### 4.1. Diagrama de Relaciones

```
Roles (1) ────────< (N) Usuarios
Usuarios (1) ──────< (N) Ventas
Usuarios (1) ──────< (N) Movimientos_Inventario
Clientes (1) ──────< (N) Ventas
Ventas (1) ────────< (N) Detalles_Venta
Ventas (1) ────────< (N) Movimientos_Inventario
Productos (1) ─────< (N) Detalles_Venta
Productos (1) ─────< (N) Movimientos_Inventario
Categorias (1) ────< (N) Productos
```

### 4.2. Integridad Referencial

- Todas las relaciones usan claves foráneas con restricciones
- Eliminación en cascada solo en Detalles_Venta cuando se elimina una Venta
- Los demás casos requieren eliminación lógica (campo `activo`)

---

## 5. Triggers y Automatizaciones

### 5.1. TRG_ActualizarStock_InsertDetalle
**Propósito**: Actualiza automáticamente el stock cuando se registra una venta.

**Funcionamiento**:
1. Se dispara al insertar un detalle de venta
2. Valida que haya stock suficiente
3. Actualiza el stock del producto
4. Registra el movimiento en Movimientos_Inventario

**Validaciones**:
- No permite ventas si el stock resultante es negativo
- Registra automáticamente el movimiento de inventario

### 5.2. TRG_Productos_ActualizarFecha
**Propósito**: Actualiza automáticamente la fecha de actualización de productos.

---

## 6. Índices

### 6.1. Índices Primarios
- Todas las tablas tienen índice primario en su ID

### 6.2. Índices Secundarios
- **Usuarios**: id_rol, email
- **Productos**: id_categoria, codigo_producto, stock_actual
- **Clientes**: numero_documento
- **Ventas**: id_cliente, id_usuario, fecha_venta, numero_factura
- **Detalles_Venta**: id_venta, id_producto
- **Movimientos_Inventario**: id_producto, fecha_movimiento, id_venta

---

## 7. Vistas

### 7.1. VW_Productos_Completo
Muestra productos con información de categoría y estado de stock.

### 7.2. VW_Ventas_Completo
Muestra ventas con información completa de cliente y vendedor.

### 7.3. VW_Resumen_Inventario
Resumen de inventario por categoría con totales y alertas.

---

## 8. Consideraciones de Seguridad

1. **Contraseñas**: Siempre usar hash (bcrypt recomendado)
2. **Inyección SQL**: Usar consultas parametrizadas
3. **Validación**: Validar todos los datos en la aplicación antes de insertar
4. **Roles**: Implementar control de acceso basado en roles (RBAC)
5. **Auditoría**: El campo `ultimo_acceso` en Usuarios permite auditoría

---

## 9. Datos Iniciales (Seed)

El script incluye datos iniciales:
- 3 roles básicos
- 1 usuario administrador (cambiar contraseña en producción)
- 5 categorías de ejemplo

---

## 10. Mejoras Futuras

- Tabla de Proveedores
- Tabla de Compras
- Tabla de Configuración (impuestos, parámetros)
- Tabla de Auditoría más detallada
- Soporte para múltiples almacenes
- Historial de precios

---

## 11. Convenciones de Nomenclatura

- **Tablas**: PascalCase (ej: `Detalles_Venta`)
- **Campos**: snake_case (ej: `id_producto`, `fecha_creacion`)
- **Claves Primarias**: `id_[tabla]`
- **Claves Foráneas**: `id_[tabla_referenciada]`
- **Índices**: `IX_[Tabla]_[Campo]`
- **Triggers**: `TRG_[Tabla]_[Accion]`
- **Vistas**: `VW_[Nombre]`
