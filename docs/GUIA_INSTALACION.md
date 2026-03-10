# Guía de Instalación - OmniStock

## Requisitos del Sistema

### Software Necesario

1. **Python 3.8 o superior**
   - Descargar desde: https://www.python.org/downloads/
   - Verificar instalación: `python --version`

2. **SQL Server 2019 o superior**
   - SQL Server Express (gratuito): https://www.microsoft.com/sql-server/sql-server-downloads
   - SQL Server Management Studio (SSMS): https://docs.microsoft.com/sql/ssms/download-sql-server-management-studio-ssms

3. **Driver ODBC para SQL Server**
   - Windows: Ya viene incluido
   - Linux: `sudo apt-get install unixodbc-dev unixodbc`

### Librerías de Python

```bash
# Instalar dependencias
pip install pyodbc
# o alternativamente
pip install pymssql

# Para usar ORM (opcional pero recomendado)
pip install sqlalchemy
```

## Pasos de Instalación

### 1. Configurar SQL Server

#### 1.1. Instalar SQL Server
- Descargar e instalar SQL Server Express o Developer Edition
- Durante la instalación, configurar:
  - Modo de autenticación: **Mixta (SQL Server y Windows)**
  - Contraseña del usuario `sa`
  - Puerto: 1433 (por defecto)

#### 1.2. Crear la Base de Datos

**Opción A: Usando SQL Server Management Studio (SSMS)**

1. Abrir SSMS
2. Conectarse al servidor (usando autenticación SQL Server)
3. Abrir el archivo `database/schema.sql`
4. Ejecutar el script completo (F5)
5. Verificar que la base de datos `OmniStock` fue creada

**Opción B: Usando línea de comandos (sqlcmd)**

```bash
# Windows
sqlcmd -S localhost -U sa -P TuContraseña -i database\schema.sql

# Linux/Mac
sqlcmd -S localhost -U sa -P TuContraseña -i database/schema.sql
```

#### 1.3. Verificar la Instalación

```sql
USE OmniStock;
GO

-- Verificar tablas creadas
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_TYPE = 'BASE TABLE';
GO

-- Verificar datos iniciales
SELECT * FROM Roles;
SELECT * FROM Usuarios;
SELECT * FROM Categorias;
GO
```

### 2. Configurar Python

#### 2.1. Crear Entorno Virtual (Recomendado)

```bash
# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate
# Linux/Mac:
source venv/bin/activate
```

#### 2.2. Instalar Dependencias

```bash
# Instalar pyodbc (recomendado)
pip install pyodbc

# O instalar pymssql (alternativa)
pip install pymssql

# Para desarrollo con ORM
pip install sqlalchemy
```

#### 2.3. Verificar Instalación del Driver

**Windows:**
```bash
# Listar drivers ODBC instalados
odbcinst -q -d
```

**Linux:**
```bash
# Verificar driver
odbcinst -q -d
```

Si no aparece "ODBC Driver 17 for SQL Server" o similar, instalar:
- Windows: Descargar desde Microsoft
- Linux: `sudo apt-get install msodbcsql17`

### 3. Configurar la Aplicación

#### 3.1. Crear Archivo de Configuración

```bash
# Copiar archivo de ejemplo
cp config/config.example.py config/config.py
```

#### 3.2. Editar Configuración

Editar `config/config.py` con tus datos:

```python
DATABASE_CONFIG = {
    'server': 'localhost',  # o la IP de tu servidor
    'database': 'OmniStock',
    'username': 'sa',  # o tu usuario
    'password': 'TuContraseñaReal',  # Cambiar esto
    'driver': 'ODBC Driver 17 for SQL Server',
    'trust_server_certificate': True,
    'port': 1433
}
```

#### 3.3. Probar Conexión

```bash
# Ejecutar script de prueba
python database/ejemplo_conexion.py
```

Deberías ver: `Conexión exitosa a SQL Server`

## Solución de Problemas

### Error: "No se puede encontrar el controlador ODBC"

**Solución:**
1. Verificar que el driver está instalado: `odbcinst -q -d`
2. Si no está, instalar el driver correspondiente
3. En Windows, verificar en: Panel de Control → Herramientas administrativas → Orígenes de datos ODBC

### Error: "Login failed for user"

**Solución:**
1. Verificar que SQL Server acepta autenticación SQL Server
2. Verificar usuario y contraseña
3. Verificar que el usuario tiene permisos en la base de datos

### Error: "Cannot open database"

**Solución:**
1. Verificar que la base de datos existe: `SELECT name FROM sys.databases;`
2. Verificar que el usuario tiene permisos: `USE OmniStock;`
3. Ejecutar el script `schema.sql` nuevamente

### Error: "Connection timeout"

**Solución:**
1. Verificar que SQL Server está corriendo
2. Verificar firewall (puerto 1433)
3. Verificar que el servidor acepta conexiones remotas (si aplica)

## Verificación Final

### Checklist de Instalación

- [ ] SQL Server instalado y corriendo
- [ ] Base de datos `OmniStock` creada
- [ ] Tablas creadas correctamente
- [ ] Datos iniciales insertados (Roles, Usuario admin, Categorías)
- [ ] Python 3.8+ instalado
- [ ] pyodbc o pymssql instalado
- [ ] Driver ODBC configurado
- [ ] Archivo `config.py` creado y configurado
- [ ] Conexión de prueba exitosa

### Prueba Rápida

```python
import pyodbc

conn = pyodbc.connect(
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=localhost;"
    "Database=OmniStock;"
    "UID=sa;"
    "PWD=TuContraseña;"
    "TrustServerCertificate=yes;"
)

cursor = conn.cursor()
cursor.execute("SELECT COUNT(*) FROM Productos")
print(f"Productos en la base de datos: {cursor.fetchone()[0]}")

conn.close()
print("Instalación verificada correctamente")
```

## Próximos Pasos

1.  Base de datos configurada
2.  Implementar modelos de datos en Python
3.  Crear módulos de negocio
4.  Desarrollar interfaz de usuario
5.  Implementar autenticación
6.  Realizar pruebas

## Recursos Adicionales

- [Documentación de pyodbc](https://github.com/mkleehammer/pyodbc/wiki)
- [Documentación de SQL Server](https://docs.microsoft.com/sql/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)

---

**Nota**: Si encuentras problemas durante la instalación, revisa los logs de SQL Server y los mensajes de error específicos para diagnosticar el problema.
