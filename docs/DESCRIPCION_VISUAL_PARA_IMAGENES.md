# Descripción Visual Detallada para Generar Imágenes - OmniStock

Este documento contiene descripciones detalladas de cada pantalla del sistema OmniStock para usar con generadores de imágenes AI (DALL-E, Midjourney, Stable Diffusion, etc.).

## Estilo General

**Estilo Visual**: Moderno, limpio, profesional, minimalista, similar a aplicaciones SaaS modernas como Stripe, Linear, o Notion.

**Paleta de Colores**:
- Azul primario: #007bff (azul brillante)
- Fondo: Blanco (#ffffff) y gris muy claro (#f8f9fa)
- Texto: Gris oscuro (#212529) y gris medio (#6c757d)
- Acentos: Verde (#28a745), Amarillo (#ffc107), Rojo (#dc3545)

**Tipografía**: Sans-serif moderna, similar a Inter o SF Pro Display

---

## 1. PANTALLA DE LOGIN

**Prompt para generador de imágenes**:
```
Diseño de pantalla de login moderna y profesional. Fondo con gradiente azul suave (de #007bff a #0056b3). 
Centrado en la pantalla hay una tarjeta blanca redondeada con sombra suave. 
En la parte superior de la tarjeta está el título "OMNISTOCK" en letras grandes azules, 
y debajo "Sistema de Gestión" en texto gris más pequeño. 
En el centro hay dos campos de entrada: uno para "Usuario" y otro para "Contraseña", 
ambos con bordes grises claros y esquinas redondeadas. 
Debajo hay un checkbox pequeño con texto "Recordar sesión". 
En la parte inferior hay un botón azul grande con texto blanco "INGRESAR". 
Al final hay un enlace pequeño azul "¿Olvidaste tu contraseña?". 
Todo está centrado y con espaciado generoso. Estilo moderno, limpio, minimalista.
```

**Elementos visuales**:
- Fondo: Gradiente azul diagonal (arriba izquierda #007bff, abajo derecha #0056b3)
- Tarjeta: Blanca, 400px de ancho, esquinas redondeadas (8px), sombra suave
- Título: "OMNISTOCK" en azul, 32px, bold
- Subtítulo: "Sistema de Gestión" en gris, 16px
- Inputs: Rectángulos blancos con borde gris claro, 320px de ancho, 40px de alto
- Botón: Azul sólido (#007bff), 320px de ancho, 44px de alto, texto blanco, bold

---

## 2. DASHBOARD / PANEL PRINCIPAL

**Prompt para generador de imágenes**:
```
Dashboard moderno de sistema de gestión. En la parte superior hay una barra de navegación blanca 
con el logo "OmniStock" a la izquierda en azul, un menú horizontal en el centro con opciones 
(Inicio, Productos, Clientes, Ventas, Inventario, Reportes), y a la derecha información del usuario. 
Debajo hay un título grande "Dashboard - Resumen General". 
Luego hay una cuadrícula de 4 tarjetas de métricas, cada una con un icono circular de color 
(verde, azul, azul claro, amarillo) a la izquierda y números grandes (como $2,500, 125, 45, 3) 
con etiquetas pequeñas debajo (Ventas Hoy, Productos Activos, Clientes Activos, Stock Bajo). 
Más abajo hay una tarjeta grande blanca con un gráfico de barras azules mostrando "Ventas del Mes" 
con barras de diferentes alturas. 
Al final hay otra tarjeta con título "Productos con Stock Bajo" y una lista de 3 items 
con iconos de advertencia amarillos. Todo con fondo gris muy claro, diseño limpio y moderno.
```

**Elementos visuales**:
- Navbar: Blanca, 64px de alto, sombra sutil, fija arriba
- Grid de métricas: 4 columnas, cada tarjeta 280x120px, iconos circulares 56px
- Gráfico: Tarjeta blanca, gráfico de barras con 7 barras azules de diferentes alturas
- Lista de alertas: Tarjeta blanca, items con fondo amarillo claro, borde izquierdo amarillo

---

## 3. LISTADO DE PRODUCTOS

**Prompt para generador de imágenes**:
```
Pantalla de listado de productos moderna. Barra de navegación blanca arriba. 
Título "Productos" grande a la izquierda, botones "Buscar" y "Nuevo Producto" a la derecha. 
Debajo hay dos dropdowns pequeños para filtros (Categoría y Stock). 
Luego una tabla grande blanca con encabezados grises oscuros: 
Código, Nombre, Categoría, Stock, Precio, Acciones. 
La tabla tiene 3 filas de datos: 
- PROD001, Laptop HP, Electrónica, badge verde "15", $850.00, iconos de editar y eliminar
- PROD002, Camiseta M, Ropa, badge verde "50", $25.00, iconos
- PROD003, Arroz 1kg, Alimentos, badge amarillo "8 ⚠️", $3.00, iconos
La tercera fila tiene fondo amarillo muy claro indicando stock bajo. 
Abajo de la tabla hay paginación centrada con botones "Anterior" y "Siguiente" 
y texto "Página 1 de 5" en el medio. Fondo gris muy claro, diseño limpio.
```

**Elementos visuales**:
- Tabla: Filas alternadas blanco y gris muy claro, hover gris medio
- Badges: Círculos pequeños, verde para stock normal, amarillo para stock bajo
- Iconos de acción: Pequeños, grises, alineados horizontalmente
- Fila de advertencia: Fondo #fff3cd (amarillo muy claro)

---

## 4. FORMULARIO DE PRODUCTO

**Prompt para generador de imágenes**:
```
Formulario moderno para crear/editar producto. Modal o página centrada, 
tarjeta blanca de 600px de ancho. Título "NUEVO PRODUCTO" arriba a la izquierda, 
botones "Guardar" y "Cancelar" arriba a la derecha. 
El formulario tiene campos en dos columnas:
Columna izquierda:
- Código Producto: [PROD___] (input gris)
- Nombre: [________________] (input largo)
- Descripción: [área de texto grande]
- Categoría: [Dropdown "Electrónica ▼"]
- Precio Venta: [$______]
- Precio Compra: [$______]

Columna derecha:
- Stock Actual: [____]
- Stock Mínimo: [____]
- Unidad Medida: [Dropdown "UNIDAD ▼"]
- Estado: Radio buttons "○ Activo" y "○ Inactivo"

Abajo hay botones grandes "Guardar" (azul) y "Cancelar" (gris con borde). 
Campos requeridos tienen asterisco rojo. Diseño limpio, espaciado generoso.
```

**Elementos visuales**:
- Layout: 2 columnas en desktop, 1 columna en mobile
- Inputs: Rectángulos con bordes grises, focus azul con sombra
- Radio buttons: Círculos pequeños
- Botones: Azul primario y gris secundario, 44px de alto

---

## 5. NUEVA VENTA

**Prompt para generador de imágenes**:
```
Pantalla de nueva venta moderna con layout de dos columnas. 
Columna izquierda (más ancha):
- Tarjeta blanca arriba con campo "Cliente" (input de búsqueda + botón "Seleccionar"), 
  "Número de Factura: FAC-2025-001" y "Fecha: 15/03/2025"
- Tarjeta blanca grande con título "Productos", 
  input de búsqueda "Buscar producto por código o nombre..." con botón "Buscar"
- Tabla con columnas: Producto, Cantidad, Precio, Descuento, Subtotal, Acciones
  Mostrando 2 filas: "Laptop HP" (cantidad 1, $850) y "Camiseta M" (cantidad 2, $25, descuento $5)
- Botón "+ Agregar Producto" debajo de la tabla
- Área de texto "Observaciones" al final

Columna derecha (estrecha, 320px):
- Tarjeta blanca fija con título "Resumen"
- Lista de totales:
  Subtotal: $895.00
  Impuesto (19%): $170.05
  Descuento: $0.00
  ────────────────
  TOTAL: $1,065.05 (en grande, azul, bold)
- Botones "Cancelar" y "Guardar Venta" (azul) abajo

Fondo gris muy claro, diseño profesional.
```

**Elementos visuales**:
- Layout: Grid 2 columnas (70% / 30%)
- Resumen: Tarjeta sticky, fondo ligeramente gris, total destacado
- Tabla: Filas con inputs pequeños para cantidad y descuento
- Botones de acción: Full width en resumen

---

## 6. HISTORIAL DE VENTAS

**Prompt para generador de imágenes**:
```
Pantalla de historial de ventas. Barra de navegación arriba. 
Título "Historial de Ventas" a la izquierda, botón "Nueva Venta" azul a la derecha. 
Dos inputs de fecha pequeños "Desde: __/__/____" y "Hasta: __/__/____" para filtros. 
Tabla blanca grande con columnas: Factura, Cliente, Fecha, Total, Estado, Acciones. 
Mostrando filas:
- FAC-001, Juan Pérez, 15/03/25, $1,065, checkmark verde ✓, iconos Ver/Anular/Imprimir
- FAC-002, María García, 14/03/25, $450, checkmark verde ✓, iconos
Estado "COMPLETADA" mostrado con icono verde. 
Botones de acción pequeños al final de cada fila. 
Fondo gris claro, diseño limpio y organizado.
```

---

## 7. GESTIÓN DE CLIENTES

**Prompt para generador de imágenes**:
```
Pantalla de gestión de clientes. Navbar arriba. 
Título "Clientes" y botones "Nuevo" y "Buscar" en el header. 
Tabla blanca con columnas: Documento, Nombre, Email, Teléfono, Acciones. 
Filas de ejemplo:
- 123456789, Juan Pérez, juan@email.com, 300-123-4567, iconos Editar/Eliminar/Ver Historial
- 987654321, María García, maria@email.com, 301-234-5678, iconos
Cada fila tiene hover gris claro. Botones de acción pequeños al final. 
Fondo gris muy claro, diseño moderno y limpio.
```

---

## 8. CONTROL DE INVENTARIO

**Prompt para generador de imágenes**:
```
Pantalla de control de inventario. Título "Control de Inventario" grande. 
Tabla blanca con columnas: Producto, Stock Actual, Stock Mínimo, Estado, Acciones. 
Filas mostrando:
- Laptop HP, 15, 5, badge verde "Normal", botón "Ajustar"
- Arroz 1kg, 8, 10, badge amarillo "⚠ Bajo", botón "Ajustar"
- Camiseta M, 50, 20, badge verde "Normal", botón "Ajustar"
Fila con stock bajo tiene fondo amarillo muy claro. 
Botones "Ver Movimientos" y "Reporte" arriba de la tabla. 
Diseño limpio, colores suaves, fácil de leer.
```

---

## INSTRUCCIONES PARA USAR CON GENERADORES DE IMÁGENES

### Con DALL-E (ChatGPT Plus):
1. Copia el prompt de la pantalla que quieres
2. Agrega al inicio: "UI/UX design, web application interface,"
3. Agrega al final: "high quality, professional, clean design, 4k resolution"

### Con Midjourney:
1. Usa el prompt base
2. Agrega: ":: UI design, web interface, modern SaaS application, clean, professional --ar 16:9 --style raw"

### Con Stable Diffusion:
1. Usa el prompt
2. Agrega: "ui design, web interface, modern, clean, professional, high quality, detailed"

### Con herramientas web (Mockup generators):
- **Figma**: Crea frames y usa los prompts como guía
- **Balsamiq**: Para wireframes rápidos
- **Whimsical**: Para diagramas y mockups
- **Canva**: Para diseños visuales rápidos

---

## COLORES EXACTOS PARA REFERENCIA

```
Primario: #007bff (RGB: 0, 123, 255)
Primario Oscuro: #0056b3 (RGB: 0, 86, 179)
Éxito: #28a745 (RGB: 40, 167, 69)
Advertencia: #ffc107 (RGB: 255, 193, 7)
Peligro: #dc3545 (RGB: 220, 53, 69)
Fondo: #f8f9fa (RGB: 248, 249, 250)
Blanco: #ffffff (RGB: 255, 255, 255)
Texto: #212529 (RGB: 33, 37, 41)
Texto Secundario: #6c757d (RGB: 108, 117, 125)
Borde: #dee2e6 (RGB: 222, 226, 230)
```

---

## TIPS PARA MEJORES RESULTADOS

1. **Especifica el estilo**: Siempre menciona "moderno", "limpio", "profesional"
2. **Menciona la paleta**: "azul primario #007bff, fondo blanco y gris claro"
3. **Detalla el layout**: "dos columnas", "grid de 4 tarjetas", "tabla con 6 columnas"
4. **Especifica tamaños relativos**: "tarjeta de 400px", "botón grande", "texto pequeño"
5. **Menciona estados**: "hover", "focus", "activo", "deshabilitado"
