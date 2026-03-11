# Especificaciones de Diseño para Figma - OmniStock

## Guía de Estilo

### Colores

#### Colores Primarios
```
Azul Primario: #007bff
- Usado para: Botones principales, enlaces, elementos activos
- RGB: rgb(0, 123, 255)
- HSL: hsl(211, 100%, 50%)

Azul Oscuro: #0056b3
- Usado para: Hover de botones primarios, estados activos
- RGB: rgb(0, 86, 179)

Azul Claro: #cce5ff
- Usado para: Fondos sutiles, highlights
- RGB: rgb(204, 229, 255)
```

#### Colores de Estado
```
Éxito (Verde): #28a745
- Usado para: Confirmaciones, estados exitosos
- RGB: rgb(40, 167, 69)

Advertencia (Amarillo): #ffc107
- Usado para: Alertas de stock bajo, advertencias
- RGB: rgb(255, 193, 7)

Peligro (Rojo): #dc3545
- Usado para: Eliminaciones, errores
- RGB: rgb(220, 53, 69)

Info (Azul Claro): #17a2b8
- Usado para: Información, tooltips
- RGB: rgb(23, 162, 184)
```

#### Colores Neutros
```
Fondo Principal: #f8f9fa
- RGB: rgb(248, 249, 250)

Fondo Secundario: #ffffff
- RGB: rgb(255, 255, 255)

Texto Principal: #212529
- RGB: rgb(33, 37, 41)

Texto Secundario: #6c757d
- RGB: rgb(108, 117, 125)

Bordes: #dee2e6
- RGB: rgb(222, 226, 230)
```

### Tipografía

#### Fuente Principal
```
Familia: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif
Tamaños:
- H1: 32px / 40px line-height (Bold)
- H2: 24px / 32px line-height (SemiBold)
- H3: 20px / 28px line-height (SemiBold)
- H4: 18px / 24px line-height (Medium)
- Body: 16px / 24px line-height (Regular)
- Small: 14px / 20px line-height (Regular)
- Caption: 12px / 16px line-height (Regular)
```

### Espaciado

```
Sistema de 8px:
- xs: 4px
- sm: 8px
- md: 16px
- lg: 24px
- xl: 32px
- xxl: 48px
- xxxl: 64px
```

### Componentes Base

#### Botones

**Botón Primario**
```
- Fondo: #007bff
- Texto: #ffffff
- Padding: 12px 24px
- Border-radius: 6px
- Font-size: 16px
- Font-weight: 500
- Hover: #0056b3
- Active: #004085
- Disabled: #6c757d (fondo), #adb5bd (texto)
```

**Botón Secundario**
```
- Fondo: transparente
- Borde: 1px solid #007bff
- Texto: #007bff
- Padding: 12px 24px
- Border-radius: 6px
- Hover: #007bff (fondo), #ffffff (texto)
```

**Botón Peligro**
```
- Fondo: #dc3545
- Texto: #ffffff
- Hover: #c82333
```

#### Inputs

```
- Altura: 40px
- Padding: 12px 16px
- Border: 1px solid #dee2e6
- Border-radius: 6px
- Font-size: 16px
- Focus: border-color #007bff, box-shadow 0 0 0 3px rgba(0,123,255,.25)
- Error: border-color #dc3545
- Disabled: background #e9ecef, color #6c757d
```

#### Cards

```
- Fondo: #ffffff
- Border-radius: 8px
- Box-shadow: 0 2px 4px rgba(0,0,0,0.1)
- Padding: 24px
- Margin-bottom: 16px
```

#### Tablas

```
- Header: fondo #f8f9fa, texto #212529, font-weight 600
- Filas alternadas: fondo #ffffff y #f8f9fa
- Border: 1px solid #dee2e6
- Padding celdas: 12px 16px
- Hover fila: fondo #e9ecef
```

### Layout

#### Grid System
```
- Container máximo: 1200px
- Columnas: 12
- Gutter: 24px
- Breakpoints:
  - Mobile: 320px - 767px
  - Tablet: 768px - 1023px
  - Desktop: 1024px+
```

#### Header/Navbar
```
- Altura: 64px
- Fondo: #ffffff
- Box-shadow: 0 2px 4px rgba(0,0,0,0.1)
- Padding horizontal: 24px
- Logo: izquierda
- Menú: centro
- Usuario info: derecha
```

#### Sidebar (si aplica)
```
- Ancho: 240px
- Fondo: #ffffff
- Border-right: 1px solid #dee2e6
- Altura: 100vh
- Padding: 16px
```

## Pantallas Detalladas

### 1. Login

**Dimensiones**: 400px x 500px (centrado)

**Elementos**:
- Logo/Título: 48px desde arriba
- Formulario centrado
- Input Usuario: 320px ancho
- Input Contraseña: 320px ancho
- Checkbox "Recordar sesión"
- Botón "INGRESAR": 320px ancho, altura 44px
- Link "¿Olvidaste tu contraseña?": centrado, 14px

**Espaciado**:
- Entre inputs: 16px
- Entre checkbox y botón: 24px
- Entre botón y link: 16px

### 2. Dashboard

**Layout**:
- Header fijo arriba
- Grid de 4 cards (métricas) arriba: 280px x 120px cada una
- Gráfico de barras: 100% ancho, 300px alto
- Lista de productos con stock bajo: 100% ancho

**Cards de Métricas**:
- Icono: 32px x 32px (izquierda)
- Número grande: 32px bold
- Etiqueta: 14px secondary
- Fondo: degradado sutil o color sólido claro

### 3. Listado de Productos

**Layout**:
- Barra de acciones: 64px alto
  - Título izquierda
  - Botones derecha (Nuevo, Buscar)
- Filtros: 56px alto
  - Dropdowns lado a lado
- Tabla: 100% ancho
  - Columnas: Código (120px), Nombre (flex), Categoría (150px), Stock (100px), Precio (120px), Acciones (120px)
- Paginación: 48px alto, centrado

### 4. Formulario de Producto

**Layout**: Modal o página completa
- Ancho máximo: 600px (centrado)
- Título: "NUEVO PRODUCTO" o "EDITAR PRODUCTO"
- Formulario en 2 columnas (responsive a 1 columna en mobile)
- Botones de acción: fijos abajo, 64px alto

**Campos**:
- Label arriba, input abajo
- Espaciado entre campos: 20px
- Campos requeridos: asterisco rojo (*)

### 5. Nueva Venta

**Layout**:
- Sección Cliente: 100% ancho, 80px alto
- Sección Factura: 100% ancho, 60px alto
- Tabla de productos: 100% ancho, altura variable
- Resumen de totales: 320px ancho (derecha), sticky
- Botones de acción: abajo, 64px alto

**Tabla de Productos**:
- Columnas: Producto (flex), Cantidad (100px), Precio (120px), Desc. (100px), Subtotal (120px), Acciones (80px)
- Botón "+ Agregar Producto" arriba de la tabla

**Resumen**:
- Fondo: #f8f9fa
- Padding: 20px
- Border-radius: 8px
- Total destacado: 24px bold, color primario

## Iconos

**Biblioteca recomendada**: Material Icons, Font Awesome, o Heroicons

**Tamaños**:
- Pequeño: 16px
- Mediano: 24px
- Grande: 32px
- Extra grande: 48px

**Iconos principales**:
- Productos: 📦 / package / box
- Clientes: 👥 / users / user-group
- Ventas: 💰 / dollar-sign / shopping-cart
- Inventario: 📊 / bar-chart / inventory
- Reportes: 📈 / chart-line / analytics
- Configuración: ⚙️ / settings / cog
- Usuarios: 👤 / user / users
- Alertas: ⚠️ / alert-triangle / exclamation

## Estados y Animaciones

### Estados de Botones
- Default
- Hover (elevación +2px)
- Active (presionado)
- Disabled (opacidad 0.5)
- Loading (spinner)

### Transiciones
- Duración: 200ms
- Easing: ease-in-out
- Propiedades: color, background-color, transform, box-shadow

### Loading States
- Spinner: 24px, color primario
- Skeleton screens para contenido cargando

## Responsive Design

### Mobile (< 768px)
- Menú hamburguesa
- Tablas con scroll horizontal
- Formularios en 1 columna
- Botones full-width
- Cards apiladas verticalmente

### Tablet (768px - 1023px)
- Menú colapsable
- Grid de 2 columnas
- Tablas con scroll horizontal opcional

### Desktop (1024px+)
- Layout completo
- Grid de 3-4 columnas
- Sidebar visible (si aplica)

## Accesibilidad

- Contraste mínimo: 4.5:1 para texto normal, 3:1 para texto grande
- Focus visible: outline 2px solid #007bff
- Tamaño mínimo de área táctil: 44px x 44px
- Labels asociados a inputs
- ARIA labels donde sea necesario

## Archivos a Crear en Figma

1. **Design System**
   - Colores
   - Tipografía
   - Espaciado
   - Componentes base (botones, inputs, cards)

2. **Pantallas**
   - Login
   - Dashboard
   - Listado de Productos
   - Formulario de Producto
   - Listado de Clientes
   - Formulario de Cliente
   - Nueva Venta
   - Historial de Ventas
   - Control de Inventario
   - Gestión de Usuarios

3. **Componentes Reutilizables**
   - Header/Navbar
   - Sidebar
   - Tabla
   - Formulario
   - Modal
   - Card de métrica
   - Botones
   - Inputs

## Notas para Figma

- Usar Auto Layout para componentes flexibles
- Crear variantes para estados (hover, active, disabled)
- Usar Constraints para responsive
- Crear componentes maestros para reutilización
- Usar estilos de texto y colores compartidos
- Agregar prototipos con interacciones básicas
