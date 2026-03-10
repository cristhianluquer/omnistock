# Índice de Documentación - OmniStock

##  Documentación del Proyecto

### 1. Documentación Técnica

#### [Modelo de Datos](MODELO_DATOS.md)
Documentación completa del modelo de datos:
- Descripción de todas las entidades
- Relaciones entre tablas
- Triggers y automatizaciones
- Índices y optimizaciones
- Vistas predefinidas
- Consideraciones de seguridad

#### [Resumen Ejecutivo](RESUMEN_EJECUTIVO.md)
Resumen general del proyecto:
- Visión general del sistema
- Arquitectura
- Funcionalidades principales
- Flujos de proceso
- Métricas y reportes
- Próximos pasos

### 2. Diagramas y Modelos

#### [Diagrama ER (Texto)](../database/diagrama_er.md)
Diagrama entidad-relación en formato texto ASCII.

#### [Diagrama ER (Mermaid)](../database/diagrama_mermaid.md)
Diagrama entidad-relación en formato Mermaid (visualizable en GitHub, GitLab, VS Code).

#### [Diagrama ER (PlantUML)](../database/diagrama_plantuml.puml)
Diagrama entidad-relación en formato PlantUML (usar con editor PlantUML).

### 3. Diseño de Interfaz

#### [Mockups y Wireframes](MOCKUPS.md)
Diseño de interfaces de usuario:
- Pantallas de login
- Módulo de productos
- Módulo de clientes
- Módulo de ventas
- Módulo de inventario
- Módulo de usuarios
- Dashboard y reportes
- Flujos de usuario

### 4. Instalación y Configuración

#### [Guía de Instalación](GUIA_INSTALACION.md)
Guía paso a paso para instalar y configurar el sistema:
- Requisitos del sistema
- Instalación de SQL Server
- Configuración de Python
- Configuración de la aplicación
- Solución de problemas
- Verificación de instalación

### 5. Scripts y Código

#### [Script SQL Principal](../database/schema.sql)
Script completo para crear la base de datos:
- Creación de base de datos
- Creación de tablas
- Índices
- Triggers
- Vistas
- Datos iniciales

#### [Ejemplo de Conexión](../database/ejemplo_conexion.py)
Ejemplos de código para conectar Python con SQL Server:
- Conexión con pyodbc
- Conexión con pymssql
- Conexión con SQLAlchemy
- Consultas parametrizadas
- Manejo de transacciones

#### [Configuración de Ejemplo](../config/config.example.py)
Archivo de configuración de ejemplo con todas las opciones.

##  Estructura de Archivos

```
omnistock/
├── database/
│   ├── schema.sql                    # Script SQL principal
│   ├── diagrama_er.md                # Diagrama ER (texto)
│   ├── diagrama_mermaid.md           # Diagrama ER (Mermaid)
│   ├── diagrama_plantuml.puml        # Diagrama ER (PlantUML)
│   └── ejemplo_conexion.py           # Ejemplos de conexión
├── config/
│   └── config.example.py             # Configuración de ejemplo
├── docs/
│   ├── INDICE.md                     # Este archivo
│   ├── MODELO_DATOS.md               # Documentación del modelo
│   ├── RESUMEN_EJECUTIVO.md          # Resumen ejecutivo
│   ├── MOCKUPS.md                    # Mockups y wireframes
│   └── GUIA_INSTALACION.md           # Guía de instalación
└── README.md                         # Documentación principal
```

##  Inicio Rápido

1. **Leer primero**: [Resumen Ejecutivo](RESUMEN_EJECUTIVO.md)
2. **Revisar modelo**: [Modelo de Datos](MODELO_DATOS.md)
3. **Ver diagramas**: [Diagrama ER (Mermaid)](../database/diagrama_mermaid.md)
4. **Instalar**: [Guía de Instalación](GUIA_INSTALACION.md)
5. **Ver diseño**: [Mockups](MOCKUPS.md)

##  Checklist de Desarrollo

### Fase 1: Base de Datos 
- [x] Diseño del modelo de datos
- [x] Scripts SQL completos
- [x] Triggers y automatizaciones
- [x] Vistas y reportes
- [x] Documentación técnica

### Fase 2: Backend (Pendiente)
- [ ] Conexión a SQL Server
- [ ] Modelos de datos en Python
- [ ] Lógica de negocio
- [ ] Autenticación y autorización
- [ ] API o servicios

### Fase 3: Frontend (Pendiente)
- [ ] Diseño de interfaz
- [ ] Formularios CRUD
- [ ] Módulo de ventas
- [ ] Dashboard y reportes
- [ ] Validaciones y mensajes

### Fase 4: Testing y Despliegue (Pendiente)
- [ ] Pruebas unitarias
- [ ] Pruebas de integración
- [ ] Documentación de usuario
- [ ] Despliegue

##  Enlaces Útiles

- [Documentación de pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
- [Documentación de SQL Server](https://docs.microsoft.com/sql/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Mermaid Live Editor](https://mermaid.live/)
- [PlantUML Online](http://www.plantuml.com/plantuml/uml/)

##  Notas

- Todos los diagramas están en múltiples formatos para facilitar la visualización
- Los scripts SQL están listos para ejecutarse en SQL Server
- Los ejemplos de código Python incluyen buenas prácticas de seguridad
- La documentación sigue las mejores prácticas de desarrollo

---

**Última actualización**: 2025
**Versión**: 1.0
