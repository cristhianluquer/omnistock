"""
Ejemplo de conexión a SQL Server desde Python
OmniStock - Sistema de Gestión de Inventario y Ventas

Requisitos:
    pip install pyodbc
    o
    pip install pymssql
"""

# Opción 1: Usando pyodbc (Recomendado)
import pyodbc

def conectar_sql_server_pyodbc():
    """
    Conecta a SQL Server usando pyodbc
    
    Requisitos:
    - Driver ODBC para SQL Server instalado
    - Windows: Ya viene instalado
    - Linux: sudo apt-get install unixodbc-dev
    """
    try:
        # Cadena de conexión
        connection_string = (
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=localhost;"
            "Database=OmniStock;"
            "UID=sa;"
            "PWD=TuContraseña;"
            "TrustServerCertificate=yes;"
        )
        
        # Establecer conexión
        conn = pyodbc.connect(connection_string)
        print("Conexión exitosa a SQL Server")
        
        # Crear cursor
        cursor = conn.cursor()
        
        # Ejemplo de consulta
        cursor.execute("SELECT @@VERSION")
        version = cursor.fetchone()
        print(f"Versión de SQL Server: {version[0]}")
        
        # Cerrar conexión
        cursor.close()
        conn.close()
        
        return True
        
    except pyodbc.Error as e:
        print(f"Error de conexión: {e}")
        return False


# Opción 2: Usando pymssql (Alternativa)
import pymssql

def conectar_sql_server_pymssql():
    """
    Conecta a SQL Server usando pymssql
    
    Requisitos:
    pip install pymssql
    """
    try:
        # Establecer conexión
        conn = pymssql.connect(
            server='localhost',
            user='sa',
            password='TuContraseña',
            database='OmniStock',
            port=1433
        )
        
        print("Conexión exitosa a SQL Server")
        
        # Crear cursor
        cursor = conn.cursor()
        
        # Ejemplo de consulta
        cursor.execute("SELECT COUNT(*) FROM Productos")
        count = cursor.fetchone()
        print(f"Total de productos: {count[0]}")
        
        # Cerrar conexión
        cursor.close()
        conn.close()
        
        return True
        
    except pymssql.Error as e:
        print(f"Error de conexión: {e}")
        return False


# Opción 3: Usando SQLAlchemy (ORM - Recomendado para proyectos grandes)
from sqlalchemy import create_engine, text

def conectar_sql_server_sqlalchemy():
    """
    Conecta a SQL Server usando SQLAlchemy (ORM)
    
    Requisitos:
    pip install sqlalchemy pyodbc
    """
    try:
        # Cadena de conexión para SQLAlchemy
        connection_string = (
            "mssql+pyodbc://sa:TuContraseña@localhost/OmniStock?"
            "driver=ODBC+Driver+17+for+SQL+Server&"
            "TrustServerCertificate=yes"
        )
        
        # Crear engine
        engine = create_engine(connection_string)
        
        # Probar conexión
        with engine.connect() as conn:
            result = conn.execute(text("SELECT @@VERSION"))
            version = result.fetchone()
            print(f"Conexión exitosa: {version[0]}")
        
        return engine
        
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None


# Ejemplo de uso con consultas parametrizadas (Seguro)
def ejemplo_consulta_segura():
    """
    Ejemplo de consulta parametrizada para prevenir SQL Injection
    """
    try:
        connection_string = (
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=localhost;"
            "Database=OmniStock;"
            "UID=sa;"
            "PWD=TuContraseña;"
            "TrustServerCertificate=yes;"
        )
        
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        # CORRECTO: Consulta parametrizada
        codigo_producto = "PROD001"
        cursor.execute(
            "SELECT * FROM Productos WHERE codigo_producto = ?",
            codigo_producto
        )
        producto = cursor.fetchone()
        
        # INCORRECTO: Concatenación de strings (vulnerable a SQL Injection)
        # cursor.execute(f"SELECT * FROM Productos WHERE codigo_producto = '{codigo_producto}'")
        
        cursor.close()
        conn.close()
        
        return producto
        
    except Exception as e:
        print(f"Error: {e}")
        return None


# Ejemplo de transacción
def ejemplo_transaccion():
    """
    Ejemplo de uso de transacciones para operaciones atómicas
    """
    try:
        connection_string = (
            "Driver={ODBC Driver 17 for SQL Server};"
            "Server=localhost;"
            "Database=OmniStock;"
            "UID=sa;"
            "PWD=TuContraseña;"
            "TrustServerCertificate=yes;"
        )
        
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        
        try:
            # Iniciar transacción
            conn.autocommit = False
            
            # Operaciones
            cursor.execute(
                "INSERT INTO Productos (codigo_producto, nombre_producto, id_categoria, precio_venta, precio_compra, stock_actual, stock_minimo) VALUES (?, ?, ?, ?, ?, ?, ?)",
                "PROD999", "Producto Test", 1, 100.00, 80.00, 10, 5
            )
            
            # Si todo está bien, confirmar
            conn.commit()
            print("Transacción completada")
            
        except Exception as e:
            # Si hay error, revertir
            conn.rollback()
            print(f"Error, transacción revertida: {e}")
        
        finally:
            cursor.close()
            conn.close()
            
    except Exception as e:
        print(f"Error de conexión: {e}")


if __name__ == "__main__":
    print("=== Ejemplos de Conexión a SQL Server ===\n")
    
    print("1. Probando conexión con pyodbc...")
    # conectar_sql_server_pyodbc()
    
    print("\n2. Probando conexión con pymssql...")
    # conectar_sql_server_pymssql()
    
    print("\n3. Probando conexión con SQLAlchemy...")
    # conectar_sql_server_sqlalchemy()
    
    print("\n  IMPORTANTE: Configura las credenciales antes de ejecutar")
