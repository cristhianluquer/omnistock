import pyodbc
from werkzeug.security import generate_password_hash

conn_str = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=omnistock;'
    'UID=sa;'
    'PWD=OmniStock2024!;'
    'TrustServerCertificate=yes;'
)

conn = pyodbc.connect(conn_str)
cur = conn.cursor()

# Generar hash compatible con Werkzeug (método pbkdf2:sha256)
password_hash = generate_password_hash('admin123', method='pbkdf2:sha256')

# Actualizar el usuario admin
cur.execute("""
    UPDATE Usuarios 
    SET password_hash = ? 
    WHERE nombre_usuario = 'admin'
""", (password_hash,))

conn.commit()
conn.close()
print("✅ Contraseña actualizada")
print(f"Hash generado: {password_hash[:50]}...")
