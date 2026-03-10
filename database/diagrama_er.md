# Diagrama Entidad-Relación - OmniStock

## Modelo de Datos

```
┌─────────────────┐
│     Roles       │
├─────────────────┤
│ id_rol (PK)     │
│ nombre_rol      │
│ descripcion     │
│ activo          │
│ fecha_creacion   │
└────────┬────────┘
         │
         │ 1:N
         │
┌────────▼────────┐
│    Usuarios     │
├─────────────────┤
│ id_usuario (PK) │
│ nombre_usuario  │
│ email           │
│ password_hash   │
│ nombre_completo │
│ id_rol (FK)     │
│ activo          │
│ fecha_creacion   │
│ ultimo_acceso   │
└────────┬────────┘
         │
         │ 1:N
         │
┌────────▼────────┐      ┌─────────────────┐
│     Ventas      │      │  Movimientos_    │
├─────────────────┤      │   Inventario    │
│ id_venta (PK)   │◄─────┤                 │
│ numero_factura  │      ├─────────────────┤
│ id_cliente (FK) │      │ id_movimiento   │
│ id_usuario (FK) │      │ id_producto (FK)│
│ fecha_venta     │      │ tipo_movimiento │
│ subtotal        │      │ cantidad        │
│ impuesto        │      │ cantidad_anterior│
│ descuento       │      │ cantidad_nueva  │
│ total           │      │ motivo          │
│ estado          │      │ id_usuario (FK) │
│ observaciones   │      │ id_venta (FK)   │
│ fecha_creacion   │      │ fecha_movimiento│
└────────┬────────┘      └─────────────────┘
         │
         │ 1:N
         │
┌────────▼────────┐
│ Detalles_Venta  │
├─────────────────┤
│ id_detalle (PK) │
│ id_venta (FK)   │
│ id_producto (FK)│
│ cantidad        │
│ precio_unitario │
│ descuento       │
│ subtotal        │
└────────┬────────┘
         │
         │ N:1
         │
┌────────▼────────┐      ┌─────────────────┐
│   Productos     │      │   Categorias    │
├─────────────────┤      ├─────────────────┤
│ id_producto (PK)│      │ id_categoria(PK)│
│ codigo_producto │      │ nombre_categoria│
│ nombre_producto │      │ descripcion     │
│ descripcion     │      │ activo          │
│ id_categoria(FK)│◄─────│ fecha_creacion   │
│ precio_venta    │      └─────────────────┘
│ precio_compra   │
│ stock_actual    │
│ stock_minimo    │
│ unidad_medida   │
│ activo          │
│ fecha_creacion   │
│ fecha_actualizacion│
└────────┬────────┘
         │
         │ N:1
         │
┌────────▼────────┐
│    Clientes     │
├─────────────────┤
│ id_cliente (PK) │
│ tipo_documento  │
│ numero_documento│
│ nombre_completo │
│ email           │
│ telefono        │
│ direccion       │
│ ciudad          │
│ activo          │
│ fecha_creacion   │
│ fecha_actualizacion│
└─────────────────┘
```

## Relaciones

1. **Roles → Usuarios**: 1:N (Un rol puede tener muchos usuarios)
2. **Usuarios → Ventas**: 1:N (Un usuario puede realizar muchas ventas)
3. **Clientes → Ventas**: 1:N (Un cliente puede tener muchas ventas)
4. **Ventas → Detalles_Venta**: 1:N (Una venta tiene muchos detalles)
5. **Productos → Detalles_Venta**: 1:N (Un producto puede estar en muchos detalles)
6. **Categorias → Productos**: 1:N (Una categoría puede tener muchos productos)
7. **Productos → Movimientos_Inventario**: 1:N (Un producto tiene muchos movimientos)
8. **Usuarios → Movimientos_Inventario**: 1:N (Un usuario puede registrar muchos movimientos)
9. **Ventas → Movimientos_Inventario**: 1:N (Una venta puede generar movimientos)
