# OmniStock - Sistema de Gestión de Inventario y Ventas

Sistema de gestión integral para administración de productos, clientes, ventas y control de inventario desarrollado en **Python** con base de datos **SQL Server**.

## 📋 Descripción del Proyecto

OmniStock es una solución completa para la gestión de inventario y ventas de pequeñas y medianas empresas. El sistema permite:

- ✅ Gestión completa de productos (CRUD)
- ✅ Gestión de clientes (CRUD)
- ✅ Registro y gestión de ventas
- ✅ Control automático de inventario
- ✅ Sistema de usuarios con roles y permisos
- ✅ Reportes y análisis de datos

## 🗂️ Estructura del Proyecto

```
omnistock/
├── database/
│   ├── schema.sql              # Script SQL completo para SQL Server
│   ├── diagrama_er.md          # Diagrama ER en texto
│   ├── diagrama_mermaid.md     # Diagrama ER en Mermaid
│   ├── diagrama_plantuml.puml  # Diagrama ER en PlantUML
│   └── ejemplo_conexion.py     # Ejemplos de conexión Python-SQL Server
├── config/
│   └── config.example.py       # Configuración de ejemplo
├── docs/
│   ├── MODELO_DATOS.md         # Documentación técnica del modelo
│   ├── RESUMEN_EJECUTIVO.md    # Resumen ejecutivo
│   ├── MOCKUPS.md              # Mockups y wireframes de la interfaz
│   ├── ESPECIFICACIONES_DISENO_FIGMA.md  # Guía para diseñar en Figma
│   ├── GUIA_INSTALACION.md     # Guía de instalación
│   └── INDICE.md               # Índice de documentación
├── prototipos/
│   ├── index.html              # Prototipo: Login
│   ├── dashboard.html           # Prototipo: Dashboard
│   ├── productos.html          # Prototipo: Listado de Productos
│   ├── venta.html              # Prototipo: Nueva Venta
│   ├── styles.css              # Estilos compartidos
│   └── README.md               # Guía de prototipos
└── README.md                   # Este archivo
```

## 🗄️ Modelo de Base de Datos

El sistema utiliza las siguientes entidades principales:

- **Roles**: Define los roles de usuario (Administrador, Vendedor, Almacenista)
- **Usuarios**: Información de usuarios con autenticación
- **Categorias**: Categorización de productos
- **Productos**: Información de productos con control de stock
- **Clientes**: Información de clientes
- **Ventas**: Encabezado de transacciones de venta
- **Detalles_Venta**: Detalle de productos vendidos
- **Movimientos_Inventario**: Historial de movimientos de inventario

## 🚀 Instalación y Configuración

### Requisitos Previos

- Python 3.8 o superior
- SQL Server 2019 o superior
- pyodbc o pymssql (driver para SQL Server)

### Configuración de la Base de Datos

1. Ejecutar el script `database/schema.sql` en SQL Server Management Studio
2. Configurar la cadena de conexión en la aplicación Python

## 📚 Documentación

- [Índice de Documentación](docs/INDICE.md) - Índice completo de toda la documentación
- [Modelo de Datos](docs/MODELO_DATOS.md) - Documentación completa del modelo de datos
- [Resumen Ejecutivo](docs/RESUMEN_EJECUTIVO.md) - Resumen general del proyecto
- [Mockups](docs/MOCKUPS.md) - Diseño de interfaces y wireframes
- [Especificaciones para Figma](docs/ESPECIFICACIONES_DISENO_FIGMA.md) - Guía completa para diseñar en Figma
- [Guía de Instalación](docs/GUIA_INSTALACION.md) - Instrucciones paso a paso
- [Diagrama ER](database/diagrama_er.md) - Diagrama entidad-relación

## 🎨 Prototipos Visuales

El proyecto incluye prototipos HTML/CSS funcionales que puedes visualizar directamente en el navegador:

1. **Login** (`prototipos/index.html`) - Pantalla de autenticación
2. **Dashboard** (`prototipos/dashboard.html`) - Panel principal con métricas
3. **Productos** (`prototipos/productos.html`) - Listado de productos
4. **Nueva Venta** (`prototipos/venta.html`) - Formulario de venta

Para visualizar:
```bash
cd prototipos
python -m http.server 8000
# Abre http://localhost:8000 en tu navegador
```

Ver [README de Prototipos](prototipos/README.md) para más detalles.

## 🎯 Funcionalidades Principales

### Gestión de Productos
- Crear, editar, eliminar y consultar productos
- Control de stock con alertas de stock mínimo
- Gestión de precios (venta y compra)
- Categorización de productos

### Gestión de Clientes
- CRUD completo de clientes
- Soporte para diferentes tipos de documento
- Historial de compras por cliente

### Gestión de Ventas
- Registro de nuevas ventas
- Cálculo automático de totales e impuestos
- Generación de números de factura
- Actualización automática de inventario

### Control de Inventario
- Actualización automática de stock al realizar ventas
- Registro histórico de movimientos
- Alertas de stock bajo
- Ajustes manuales de inventario

### Gestión de Usuarios
- Sistema de autenticación
- Control de acceso basado en roles (RBAC)
- Auditoría de acciones

## 🔒 Seguridad

- Contraseñas hasheadas (bcrypt recomendado)
- Consultas parametrizadas para prevenir inyección SQL
- Control de acceso basado en roles
- Validación de datos en aplicación y base de datos

## 📝 Notas de Desarrollo

Este proyecto es parte del Trabajo Final de la asignatura **Programación Avanzada**.

**Tecnologías**:
- Backend: Python
- Base de Datos: SQL Server
- Interfaz: Por definir (Desktop o Web)

## 👥 Autores

[Agregar nombres de los integrantes del equipo]

## 📄 Licencia

Este proyecto es parte de un trabajo académico.
