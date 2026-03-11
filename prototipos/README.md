# Prototipos HTML/CSS - OmniStock

Estos son prototipos visuales del sistema OmniStock que puedes usar como referencia para crear los diseños en Figma o como base para el desarrollo frontend.

## Cómo Visualizar

### Opción 1: Abrir directamente en el navegador
1. Abre `index.html` en tu navegador para ver la pantalla de login
2. Abre `dashboard.html` para ver el dashboard
3. Abre `productos.html` para ver el listado de productos

### Opción 2: Usar un servidor local (recomendado)
```bash
# Con Python 3
python -m http.server 8000

# O con Node.js (si tienes http-server instalado)
npx http-server

# Luego abre en el navegador:
# http://localhost:8000
```

## Archivos Incluidos

- **index.html** - Pantalla de Login
- **dashboard.html** - Dashboard principal con métricas
- **productos.html** - Listado de productos con tabla
- **styles.css** - Estilos compartidos (sistema de diseño completo)

## Características

✅ Diseño responsive
✅ Sistema de colores completo
✅ Componentes reutilizables (botones, cards, tablas)
✅ Animaciones y transiciones suaves
✅ Estados hover y active
✅ Diseño moderno y profesional

## Colores Utilizados

- **Primario**: #007bff (Azul)
- **Éxito**: #28a745 (Verde)
- **Advertencia**: #ffc107 (Amarillo)
- **Peligro**: #dc3545 (Rojo)
- **Info**: #17a2b8 (Azul claro)

## Componentes Disponibles

- Botones (primario, secundario, peligro)
- Formularios (inputs, selects, checkboxes)
- Tablas con hover
- Cards de métricas
- Navbar responsive
- Gráficos de barras (CSS puro)
- Badges y etiquetas
- Paginación

## Notas para Figma

Estos prototipos siguen las especificaciones detalladas en `docs/ESPECIFICACIONES_DISENO_FIGMA.md`. Puedes usar estos archivos como referencia visual al crear los diseños en Figma.

## Próximos Prototipos a Agregar

- [ ] Formulario de Producto (crear/editar)
- [ ] Nueva Venta
- [ ] Historial de Ventas
- [ ] Gestión de Clientes
- [ ] Control de Inventario
- [ ] Gestión de Usuarios

## Personalización

Todos los colores, espaciados y tamaños están definidos como variables CSS en `:root` dentro de `styles.css`, por lo que es fácil personalizar el diseño completo cambiando solo esos valores.
