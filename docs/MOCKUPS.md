# Mockups y Wireframes - OmniStock

## 1. Estructura General de la Aplicación

### 1.1. Menú Principal
```
┌─────────────────────────────────────────────────────────────┐
│  OmniStock - Sistema de Gestión de Inventario y Ventas     │
├─────────────────────────────────────────────────────────────┤
│  [Inicio] [Productos] [Clientes] [Ventas] [Inventario]     │
│  [Reportes] [Usuarios] [Configuración] [Salir]             │
│                                                              │
│  Usuario: [Nombre Usuario] | Rol: [Rol] | [Cerrar Sesión]  │
└─────────────────────────────────────────────────────────────┘
```

---

## 2. Módulo de Autenticación

### 2.1. Pantalla de Login
```
┌─────────────────────────────────────┐
│                                     │
│         OMNISTOCK                   │
│   Sistema de Gestión                │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Usuario: [____________]     │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Contraseña: [____________]  │   │
│  └─────────────────────────────┘   │
│                                     │
│  [ ] Recordar sesión                │
│                                     │
│        [  INGRESAR  ]               │
│                                     │
│  ¿Olvidaste tu contraseña?          │
└─────────────────────────────────────┘
```

---

## 3. Módulo de Productos

### 3.1. Listado de Productos
```
┌──────────────────────────────────────────────────────────────┐
│  PRODUCTOS                                    [Nuevo] [Buscar]│
├──────────────────────────────────────────────────────────────┤
│  Filtros: [Categoría: Todas ▼] [Stock: Todos ▼]             │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Código  │ Nombre        │ Categoría │ Stock │ Precio│   │
│  ├─────────┼───────────────┼───────────┼───────┼───────┤   │
│  │ PROD001 │ Laptop HP     │ Electrónica│  15  │ $850  │   │
│  │ PROD002 │ Camiseta M    │ Ropa      │  50  │ $25   │   │
│  │ PROD003 │ Arroz 1kg     │ Alimentos │  8   │ $3    │  │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  [< Anterior] Página 1 de 5 [Siguiente >]                   │
│                                                               │
│  ⚠ = Stock bajo                                               │
└──────────────────────────────────────────────────────────────┘
```

### 3.2. Formulario de Producto (Crear/Editar)
```
┌─────────────────────────────────────────────┐
│  NUEVO PRODUCTO                    [Guardar] [Cancelar]│
├─────────────────────────────────────────────┤
│  Código Producto: [PROD___]                │
│  Nombre:        [________________________]  │
│  Descripción:   [________________________]  │
│                [________________________]   │
│  Categoría:     [Electrónica ▼]            │
│  Precio Venta:  [$______]                   │
│  Precio Compra: [$______]                   │
│  Stock Actual:  [____]                      │
│  Stock Mínimo:  [____]                      │
│  Unidad Medida: [UNIDAD ▼]                  │
│  Estado:        [○] Activo  [ ] Inactivo    │
│                                              │
│  [Guardar] [Cancelar]                       │
└─────────────────────────────────────────────┘
```

---

## 4. Módulo de Clientes

### 4.1. Listado de Clientes
```
┌──────────────────────────────────────────────────────────────┐
│  CLIENTES                                   [Nuevo] [Buscar]  │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Documento │ Nombre          │ Email        │ Teléfono│   │
│  ├───────────┼─────────────────┼─────────────┼──────────┤   │
│  │ 123456789 │ Juan Pérez      │ juan@...    │ 300...   │   │
│  │ 987654321 │ María García    │ maria@...   │ 301...   │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  [Editar] [Eliminar] [Ver Historial]                         │
└──────────────────────────────────────────────────────────────┘
```

### 4.2. Formulario de Cliente
```
┌─────────────────────────────────────────────┐
│  NUEVO CLIENTE                   [Guardar] [Cancelar]│
├─────────────────────────────────────────────┤
│  Tipo Documento: [CC ▼]                     │
│  Número:        [________________]          │
│  Nombre Completo: [________________________]│
│  Email:         [________________________]  │
│  Teléfono:      [________________]          │
│  Dirección:     [________________________]  │
│  Ciudad:        [________________]          │
│  Estado:        [○] Activo  [ ] Inactivo   │
│                                              │
│  [Guardar] [Cancelar]                       │
└─────────────────────────────────────────────┘
```

---

## 5. Módulo de Ventas

### 5.1. Nueva Venta
```
┌──────────────────────────────────────────────────────────────┐
│  NUEVA VENTA                                    [Guardar] [Cancelar]│
├──────────────────────────────────────────────────────────────┤
│  Cliente: [Buscar cliente...] [Seleccionar]                  │
│  Factura: [FAC-2025-001]  Fecha: [15/03/2025]               │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Buscar Producto: [_____________] [Buscar]            │   │
│  ├──────────────────────────────────────────────────────┤   │
│  │ Producto        │ Cant. │ Precio │ Desc. │ Subtotal │   │
│  ├─────────────────┼───────┼────────┼───────┼──────────┤   │
│  │ Laptop HP       │   1   │ $850   │ $0    │ $850     │   │
│  │ Camiseta M      │   2   │ $25    │ $5    │ $45      │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  Subtotal:     $895.00                                        │
│  Impuesto (19%): $170.05                                      │
│  Descuento:    $[____]                                        │
│  ─────────────────────────────────                           │
│  TOTAL:        $1,065.05                                      │
│                                                               │
│  Observaciones: [________________________]                   │
│                                                               │
│  [Guardar Venta] [Cancelar]                                  │
└──────────────────────────────────────────────────────────────┘
```

### 5.2. Historial de Ventas
```
┌──────────────────────────────────────────────────────────────┐
│  HISTORIAL DE VENTAS                    [Nueva Venta] [Buscar]│
├──────────────────────────────────────────────────────────────┤
│  Filtros: [Desde: __/__/____] [Hasta: __/__/____]           │
│                                                               │
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Factura    │ Cliente      │ Fecha    │ Total │ Estado│   │
│  ├────────────┼──────────────┼──────────┼───────┼───────┤   │
│  │ FAC-001    │ Juan Pérez   │ 15/03/25 │ $1065 │ ✓     │   │
│  │ FAC-002    │ María García │ 14/03/25 │ $450  │ ✓     │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  [Ver Detalle] [Anular] [Imprimir]                           │
└──────────────────────────────────────────────────────────────┘
```

---

## 6. Módulo de Inventario

### 6.1. Control de Inventario
```
┌──────────────────────────────────────────────────────────────┐
│  CONTROL DE INVENTARIO                                        │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Producto      │ Stock Actual │ Stock Mín. │ Estado  │   │
│  ├───────────────┼──────────────┼────────────┼─────────┤   │
│  │ Laptop HP     │     15       │     5      │ Normal  │   │
│  │ Arroz 1kg     │      8       │    10      │ ⚠ Bajo  │   │
│  │ Camiseta M    │     50       │    20      │ Normal  │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  [Ajustar Stock] [Ver Movimientos] [Reporte]                  │
└──────────────────────────────────────────────────────────────┘
```

### 6.2. Movimientos de Inventario
```
┌──────────────────────────────────────────────────────────────┐
│  MOVIMIENTOS DE INVENTARIO                                    │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Fecha      │ Producto │ Tipo  │ Cant. │ Usuario      │   │
│  ├────────────┼──────────┼───────┼───────┼──────────────┤   │
│  │ 15/03/2025 │ Laptop   │ SALIDA│  -1   │ Juan Admin   │   │
│  │ 14/03/2025 │ Arroz    │ ENTRADA│ +50  │ María Vendedor│   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  [Filtrar] [Exportar]                                        │
└──────────────────────────────────────────────────────────────┘
```

---

## 7. Módulo de Usuarios

### 7.1. Gestión de Usuarios
```
┌──────────────────────────────────────────────────────────────┐
│  USUARIOS                                      [Nuevo Usuario]│
├──────────────────────────────────────────────────────────────┤
│  ┌──────────────────────────────────────────────────────┐   │
│  │ Usuario      │ Nombre        │ Email      │ Rol      │   │
│  ├──────────────┼───────────────┼───────────┼──────────┤   │
│  │ admin        │ Admin Sistema │ admin@... │ Admin    │   │
│  │ vendedor1    │ Juan Vendedor │ juan@...  │ Vendedor │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  [Editar] [Cambiar Contraseña] [Desactivar]                  │
└──────────────────────────────────────────────────────────────┘
```

---

## 8. Módulo de Reportes

### 8.1. Dashboard Principal
```
┌──────────────────────────────────────────────────────────────┐
│  DASHBOARD - RESUMEN GENERAL                                  │
├──────────────────────────────────────────────────────────────┤
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌──────────┐   │
│  │ Ventas   │  │ Productos│  │ Clientes │  │ Stock    │   │
│  │ Hoy      │  │ Activos  │  │ Activos  │  │ Bajo     │   │
│  │   $2,500 │  │   125    │  │   45     │  │    3     │   │
│  └──────────┘  └──────────┘  └──────────┘  └──────────┘   │
│                                                               │
│  Ventas del Mes (Gráfico de barras)                          │
│  ┌──────────────────────────────────────────────────────┐   │
│  │                                                       │   │
│  │     ▁▂▃▅▆▇█                                          │   │
│  │                                                       │   │
│  └──────────────────────────────────────────────────────┘   │
│                                                               │
│  Productos con Stock Bajo                                     │
│  • Arroz 1kg (8 unidades)                                    │
│  • Leche 1L (5 unidades)                                     │
│  • Pan Integral (3 unidades)                                 │
└──────────────────────────────────────────────────────────────┘
```

---

## 9. Flujo de Usuario

### 9.1. Flujo de Venta
```
1. Login
   ↓
2. Menú Principal → Ventas → Nueva Venta
   ↓
3. Seleccionar Cliente
   ↓
4. Buscar y Agregar Productos
   ↓
5. Calcular Total (con impuestos)
   ↓
6. Aplicar Descuentos (opcional)
   ↓
7. Guardar Venta
   ↓
8. Sistema actualiza stock automáticamente
   ↓
9. Mostrar confirmación y opción de imprimir
```

### 9.2. Flujo de Gestión de Productos
```
1. Menú → Productos → Listar
   ↓
2. [Nuevo] o [Editar] existente
   ↓
3. Llenar formulario
   ↓
4. Validar datos
   ↓
5. Guardar
   ↓
6. Actualizar lista
```

---

## 10. Consideraciones de Diseño

### 10.1. Colores y Estilos
- **Primario**: Azul (#007bff) para acciones principales
- **Éxito**: Verde (#28a745) para confirmaciones
- **Advertencia**: Amarillo (#ffc107) para alertas de stock
- **Peligro**: Rojo (#dc3545) para eliminaciones
- **Info**: Azul claro (#17a2b8) para información

### 10.2. Iconos Sugeridos
-  Productos
-  Clientes
-  Ventas
-  Inventario
-  Reportes
-  Configuración
-  Usuarios
-  Alertas

### 10.3. Responsive Design
- La aplicación debe ser responsive
- Considerar diseño mobile-first para futuras versiones
- Tablas con scroll horizontal en pantallas pequeñas

---

## 11. Validaciones Visuales

- Campos requeridos marcados con *
- Mensajes de error en rojo debajo del campo
- Confirmaciones de éxito en verde
- Loading spinners durante operaciones
- Confirmación antes de eliminar registros
