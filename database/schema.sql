-- ============================================================
--  OmniStock - Script Base de Datos SQL Server
--  Compatible: Docker (Mac ) + SQL Server Express (Windows)
-- ============================================================
 
USE master;
GO
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'OmniStock')
    DROP DATABASE OmniStock;
GO
CREATE DATABASE OmniStock;
GO
USE OmniStock;
GO
 
-- ── ROLES ──────────────────────────────────────────────────
CREATE TABLE roles (
    id     INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(50) NOT NULL UNIQUE
);
GO
 
-- ── USUARIOS ───────────────────────────────────────────────
CREATE TABLE usuarios (
    id            INT IDENTITY(1,1) PRIMARY KEY,
    nombre        NVARCHAR(100) NOT NULL,
    usuario       NVARCHAR(50)  NOT NULL UNIQUE,
    email         NVARCHAR(100),
    password_hash NVARCHAR(255) NOT NULL,
    rol_id        INT NOT NULL DEFAULT 2,
    activo        BIT NOT NULL DEFAULT 1,
    creado_en     DATETIME2 DEFAULT GETDATE(),
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);
GO
 
-- ── CATEGORÍAS ─────────────────────────────────────────────
CREATE TABLE categorias (
    id     INT IDENTITY(1,1) PRIMARY KEY,
    nombre NVARCHAR(100) NOT NULL UNIQUE
);
GO
 
-- ── PRODUCTOS ──────────────────────────────────────────────
CREATE TABLE productos (
    id           INT IDENTITY(1,1) PRIMARY KEY,
    nombre       NVARCHAR(150) NOT NULL,
    descripcion  NVARCHAR(MAX),
    precio       DECIMAL(10,2) NOT NULL DEFAULT 0,
    stock        INT NOT NULL DEFAULT 0,
    stock_minimo INT NOT NULL DEFAULT 5,
    categoria_id INT,
    activo       BIT NOT NULL DEFAULT 1,
    creado_en    DATETIME2 DEFAULT GETDATE(),
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);
GO
 
-- ── CLIENTES ───────────────────────────────────────────────
CREATE TABLE clientes (
    id             INT IDENTITY(1,1) PRIMARY KEY,
    nombre         NVARCHAR(150) NOT NULL,
    email          NVARCHAR(100),
    telefono       NVARCHAR(20),
    direccion      NVARCHAR(MAX),
    tipo_documento NVARCHAR(20) DEFAULT 'CC',
    documento      NVARCHAR(50),
    activo         BIT NOT NULL DEFAULT 1,
    creado_en      DATETIME2 DEFAULT GETDATE()
);
GO
 
-- ── VENTAS ─────────────────────────────────────────────────
CREATE TABLE ventas (
    id         INT IDENTITY(1,1) PRIMARY KEY,
    cliente_id INT,
    usuario_id INT NOT NULL,
    total      DECIMAL(10,2) NOT NULL DEFAULT 0,
    estado     NVARCHAR(20) DEFAULT 'COMPLETADA',
    fecha      DATETIME2 DEFAULT GETDATE(),
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id)
);
GO
 
-- ── DETALLE VENTAS ─────────────────────────────────────────
CREATE TABLE detalle_ventas (
    id              INT IDENTITY(1,1) PRIMARY KEY,
    venta_id        INT NOT NULL,
    producto_id     INT NOT NULL,
    cantidad        INT NOT NULL,
    precio_unitario DECIMAL(10,2) NOT NULL,
    subtotal        DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (venta_id)    REFERENCES ventas(id),
    FOREIGN KEY (producto_id) REFERENCES productos(id)
);
GO
 
-- ── DATOS INICIALES ────────────────────────────────────────
INSERT INTO roles (nombre) VALUES ('ADMINISTRADOR'), ('VENDEDOR'), ('ALMACENISTA');
GO
 
INSERT INTO categorias (nombre) VALUES
    ('Electrónica'), ('Ropa'), ('Alimentos'), ('Hogar'), ('Otros');
GO
 
-- Usuario admin — contraseña: admin123
-- Hash generado con werkzeug generate_password_hash('admin123')
INSERT INTO usuarios (nombre, usuario, email, password_hash, rol_id) VALUES
(
    'Administrador',
    'admin',
    'admin@omnistock.com',
    'pbkdf2:sha256:260000$salt$8c4c49a5b5d0c23bbf59b3d0ff43c17c2d7e9a8f1b6e4c2a0d9f7e5b3c1a8d6',
    1
);
GO
 
-- Clientes de prueba
INSERT INTO clientes (nombre, email, telefono, tipo_documento, documento) VALUES
('Juan Pérez',    'juan@email.com',  '3001234567', 'CC',  '12345678'),
('María García',  'maria@email.com', '3109876543', 'CC',  '87654321'),
('Empresa XYZ',   'xyz@empresa.com', '6012345678', 'NIT', '900123456-1');
GO
 
-- Productos de prueba
INSERT INTO productos (nombre, descripcion, precio, stock, stock_minimo, categoria_id) VALUES
('Laptop HP 15',       'Laptop 15 pulgadas 8GB RAM',   2500000, 10, 2, 1),
('Mouse Inalámbrico',  'Mouse USB inalámbrico negro',    45000,  25, 5, 1),
('Teclado Mecánico',   'Teclado mecánico RGB',          180000,  15, 3, 1),
('Camisa Polo',        'Camisa polo talla M azul',       65000,  30, 5, 2),
('Arroz 5kg',          'Arroz blanco premium 5 kilos',   18000,   8, 10,3);
GO
 