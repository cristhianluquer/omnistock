import platform
"""
Archivo de configuración de ejemplo para OmniStock
Copia este archivo como 'config.py' y ajusta los valores según tu entorno
"""

# Configuración de Base de Datos
DATABASE_CONFIG = {
    'server': 'localhost',
    'database': 'OmniStock',
    'username': 'sa',
    'password': 'TuContraseñaAqui',
    'driver': 'ODBC Driver 17 for SQL Server',
    'trust_server_certificate': True,
    'port': 1433
}

# Mac (SQL Server en Docker):
CONN_STRING_MAC = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost,1433;'
    'DATABASE=omnistock;'
    'UID=sa;'
    'PWD=OmniStock2024!;'
    'TrustServerCertificate=yes;'
    'Encrypt=no;'  # ← Agregar esto
)
# Windows (SQL Server Express local):
CONN_STRING_WIN = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=omnistock;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)

# Cadena de conexión completa (para pyodbc)
CONNECTION_STRING = (
    f"Driver={{{DATABASE_CONFIG['driver']}}};"
    f"Server={DATABASE_CONFIG['server']};"
    f"Database={DATABASE_CONFIG['database']};"
    f"UID={DATABASE_CONFIG['username']};"
    f"PWD={DATABASE_CONFIG['password']};"
    f"TrustServerCertificate={'yes' if DATABASE_CONFIG['trust_server_certificate'] else 'no'};"
)

# Detecta automáticamente el sistema operativo
CONN_STRING = CONN_STRING_MAC if platform.system() == 'Darwin' else CONN_STRING_WIN

# Función para obtener conexión a la base de datos
def get_db():
    import pyodbc
    return pyodbc.connect(CONN_STRING)


# Configuración de la Aplicación
APP_CONFIG = {
    'name': 'OmniStock',
    'version': '1.0.0',
    'debug': True,  # Cambiar a False en producción
    'secret_key': 'cambiar-esta-clave-secreta-en-produccion',  # Generar una clave segura
}

# Configuración de Seguridad
SECURITY_CONFIG = {
    'password_hash_algorithm': 'bcrypt',  # bcrypt, argon2, pbkdf2
    'password_salt_rounds': 12,
    'session_timeout': 3600,  # Segundos (1 hora)
    'max_login_attempts': 5,
    'lockout_duration': 900,  # Segundos (15 minutos)
}

# Configuración de Impuestos
TAX_CONFIG = {
    'default_tax_rate': 0.19,  # 19% IVA (Colombia)
    'tax_name': 'IVA',
}

# Configuración de Facturación
INVOICE_CONFIG = {
    'prefix': 'FAC',
    'number_format': '{prefix}-{year}-{number:04d}',  # FAC-2025-0001
    'reset_number_yearly': True,
}

# Configuración de Stock
STOCK_CONFIG = {
    'enable_low_stock_alerts': True,
    'low_stock_threshold_percentage': 0.2,  # 20% por encima del mínimo
    'auto_update_on_sale': True,
}

# Configuración de Reportes
REPORTS_CONFIG = {
    'default_date_range_days': 30,
    'currency_symbol': '$',
    'currency_code': 'COP',
    'date_format': '%d/%m/%Y',
    'datetime_format': '%d/%m/%Y %H:%M:%S',
}

# Configuración de Logging
LOGGING_CONFIG = {
    'level': 'INFO',  # DEBUG, INFO, WARNING, ERROR, CRITICAL
    'file': 'logs/omnistock.log',
    'max_bytes': 10485760,  # 10 MB
    'backup_count': 5,
}

# Roles del Sistema
SYSTEM_ROLES = {
    'ADMINISTRADOR': 1,
    'VENDEDOR': 2,
    'ALMACENISTA': 3,
}

# Estados de Venta
SALE_STATUS = {
    'COMPLETADA': 'COMPLETADA',
    'CANCELADA': 'CANCELADA',
    'ANULADA': 'ANULADA',
}

# Tipos de Movimiento de Inventario
INVENTORY_MOVEMENT_TYPES = {
    'ENTRADA': 'ENTRADA',
    'SALIDA': 'SALIDA',
    'AJUSTE': 'AJUSTE',
}

# Tipos de Documento
DOCUMENT_TYPES = {
    'CC': 'Cédula de Ciudadanía',
    'NIT': 'Número de Identificación Tributaria',
    'CE': 'Cédula de Extranjería',
    'PASAPORTE': 'Pasaporte',
}
