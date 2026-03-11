# Diagrama Entidad-Relación - OmniStock (Mermaid)

Este diagrama puede visualizarse en cualquier editor que soporte Mermaid (GitHub, GitLab, VS Code con extensión, etc.)

```mermaid
erDiagram
    Roles ||--o{ Usuarios : "tiene"
    Categorias ||--o{ Productos : "contiene"
    Clientes ||--o{ Ventas : "realiza"
    Usuarios ||--o{ Ventas : "registra"
    Usuarios ||--o{ Movimientos_Inventario : "registra"
    Ventas ||--o{ Detalles_Venta : "contiene"
    Ventas ||--o{ Movimientos_Inventario : "genera"
    Productos ||--o{ Detalles_Venta : "incluye"
    Productos ||--o{ Movimientos_Inventario : "tiene"

    Roles {
        int id_rol PK
        varchar nombre_rol
        varchar descripcion
        bit activo
        datetime fecha_creacion
    }

    Usuarios {
        int id_usuario PK
        varchar nombre_usuario
        varchar email
        varchar password_hash
        varchar nombre_completo
        int id_rol FK
        bit activo
        datetime fecha_creacion
        datetime ultimo_acceso
    }

    Categorias {
        int id_categoria PK
        varchar nombre_categoria
        varchar descripcion
        bit activo
        datetime fecha_creacion
    }

    Productos {
        int id_producto PK
        varchar codigo_producto
        varchar nombre_producto
        varchar descripcion
        int id_categoria FK
        decimal precio_venta
        decimal precio_compra
        int stock_actual
        int stock_minimo
        varchar unidad_medida
        bit activo
        datetime fecha_creacion
        datetime fecha_actualizacion
    }

    Clientes {
        int id_cliente PK
        varchar tipo_documento
        varchar numero_documento
        varchar nombre_completo
        varchar email
        varchar telefono
        varchar direccion
        varchar ciudad
        bit activo
        datetime fecha_creacion
        datetime fecha_actualizacion
    }

    Ventas {
        int id_venta PK
        varchar numero_factura
        int id_cliente FK
        int id_usuario FK
        datetime fecha_venta
        decimal subtotal
        decimal impuesto
        decimal descuento
        decimal total
        varchar estado
        varchar observaciones
        datetime fecha_creacion
    }

    Detalles_Venta {
        int id_detalle PK
        int id_venta FK
        int id_producto FK
        int cantidad
        decimal precio_unitario
        decimal descuento
        decimal subtotal
    }

    Movimientos_Inventario {
        int id_movimiento PK
        int id_producto FK
        varchar tipo_movimiento
        int cantidad
        int cantidad_anterior
        int cantidad_nueva
        varchar motivo
        int id_usuario FK
        int id_venta FK
        datetime fecha_movimiento
    }
```

## Cómo Visualizar

1. **GitHub/GitLab**: Copia el código Mermaid y pégalo en un archivo `.md`
2. **VS Code**: Instala la extensión "Markdown Preview Mermaid Support"
3. **Online**: Usa [Mermaid Live Editor](https://mermaid.live/)
