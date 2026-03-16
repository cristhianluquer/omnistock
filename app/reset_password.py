import pyodbc
import hashlib

conn_str = (
    'DRIVER={ODBC Driver 18 for SQL Server};'
    'SERVER=localhost;'
    'DATABASE=omnistock;'
    'UID=sa;'
    'PWD=OmniStock2024!;'
    'TrustServerCertificate=yes;'
)

def reset_password():
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        
        email = 'admin@omnistock.com'
        new_password = 'admin123'  # Nueva contraseña
        
        password_hash = hashlib.sha256(new_password.encode()).hexdigest()
        
        cursor.execute("""
            UPDATE Usuarios 
            SET password_hash = ?
            WHERE email = ?
        """, (password_hash, email))
        
        conn.commit()
        print("✅ Contraseña actualizada exitosamente")
        print(f"Email: {email}")
        print(f"Nueva password: {new_password}")
        
    except Exception as e:
        print(f"❌ Error: {e}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == '__main__':
    reset_password()
