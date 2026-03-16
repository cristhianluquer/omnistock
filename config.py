import platform
import pyodbc
 
# ── Cadenas de conexión ─────────────────────────────────────────────────────
 
# Mac M4 — SQL Server corriendo en Docker
CONN_STRING_MAC = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost,1433;'
    'DATABASE=OmniStock;'
    'UID=sa;'
    'PWD=OmniStock2024!;'
    'TrustServerCertificate=yes;'
    'Encrypt=no;'
)
 
# Windows — SQL Server Express local
CONN_STRING_WIN = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost\\SQLEXPRESS;'
    'DATABASE=OmniStock;'
    'Trusted_Connection=yes;'
    'TrustServerCertificate=yes;'
)
 
# Detecta automáticamente el SO
CONN_STRING = CONN_STRING_MAC if platform.system() == 'Darwin' else CONN_STRING_WIN
 
# ── Función de conexión ─────────────────────────────────────────────────────
def get_db():
    return pyodbc.connect(CONN_STRING)
 
# ── Configuración Flask ─────────────────────────────────────────────────────
SECRET_KEY = 'omnistock_clave_secreta_2024'
 
# ── Roles ───────────────────────────────────────────────────────────────────
ROLES = {
    'ADMINISTRADOR': 1,
    'VENDEDOR': 2,
    'ALMACENISTA': 3,
}
 