-- =============================================
-- OmniStock - Sistema de Gestión de Inventario y Ventas
-- Base de Datos: SQL Server
-- =============================================

-- Crear base de datos
IF NOT EXISTS (SELECT * FROM sys.databases WHERE name = 'OmniStock')
BEGIN
    CREATE DATABASE OmniStock;
END
GO

USE OmniStock;
GO

-- =============================================
-- TABLA: Roles
-- Descripción: Define los roles de usuario del sistema
-- =============================================
CREATE TABLE Roles (
    id_rol INT PRIMARY KEY IDENTITY(1,1),
    nombre_rol VARCHAR(50) NOT NULL UNIQUE,
    descripcion VARCHAR(255),
    activo BIT DEFAULT 1,
    fecha_creacion DATETIME DEFAULT GETDATE()
);
GO

-- =============================================
-- TABLA: Usuarios
-- Descripción: Almacena información de usuarios del sistema
-- =============================================
CREATE TABLE Usuarios (
    id_usuario INT PRIMARY KEY IDENTITY(1,1),
    nombre_usuario VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password_hash VARCHAR(255) NOT NULL, -- Contraseña hasheada
    nombre_completo VARCHAR(100) NOT NULL,
    id_rol INT NOT NULL,
    activo BIT DEFAULT 1,
    fecha_creacion DATETIME DEFAULT GETDATE(),
    ultimo_acceso DATETIME,
    FOREIGN KEY (id_rol) REFERENCES Roles(id_rol)
);
GO

-- =============================================
-- TABLA: Categorias
-- Descripción: Categorías de productos
-- =============================================
CREATE TABLE Categorias (
    id_categoria INT PRIMARY KEY IDENTITY(1,1),
    nombre_categoria VARCHAR(100) NOT NULL UNIQUE,
    descripcion VARCHAR(255),
    activo BIT DEFAULT 1,
    fecha_creacion DATETIME DEFAULT GETDATE()
);
GO

-- =============================================
-- TABLA: Productos
-- Descripción: Información de productos del inventario
-- =============================================
CREATE TABLE Productos (
    id_producto INT PRIMARY KEY IDENTITY(1,1),
    codigo_producto VARCHAR(50) NOT NULL UNIQUE,
    nombre_producto VARCHAR(200) NOT NULL,
    descripcion VARCHAR(500),
    id_categoria INT NOT NULL,
    precio_venta DECIMAL(10,2) NOT NULL CHECK (precio_venta >= 0),
    precio_compra DECIMAL(10,2) NOT NULL CHECK (precio_compra >= 0),
    stock_actual INT NOT NULL DEFAULT 0 CHECK (stock_actual >= 0),
    stock_minimo INT NOT NULL DEFAULT 0 CHECK (stock_minimo >= 0),
    unidad_medida VARCHAR(20) DEFAULT 'UNIDAD',
    activo BIT DEFAULT 1,
    fecha_creacion DATETIME DEFAULT GETDATE(),
    fecha_actualizacion DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_categoria) REFERENCES Categorias(id_categoria)
);
GO

-- =============================================
-- TABLA: Clientes
-- Descripción: Información de clientes
-- =============================================
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY IDENTITY(1,1),
    tipo_documento VARCHAR(10) NOT NULL CHECK (tipo_documento IN ('CC', 'NIT', 'CE', 'PASAPORTE')),
    numero_documento VARCHAR(20) NOT NULL UNIQUE,
    nombre_completo VARCHAR(200) NOT NULL,
    email VARCHAR(100),
    telefono VARCHAR(20),
    direccion VARCHAR(255),
    ciudad VARCHAR(100),
    activo BIT DEFAULT 1,
    fecha_creacion DATETIME DEFAULT GETDATE(),
    fecha_actualizacion DATETIME DEFAULT GETDATE()
);
GO

-- =============================================
-- TABLA: Ventas
-- Descripción: Encabezado de ventas
-- =============================================
CREATE TABLE Ventas (
    id_venta INT PRIMARY KEY IDENTITY(1,1),
    numero_factura VARCHAR(50) NOT NULL UNIQUE,
    id_cliente INT NOT NULL,
    id_usuario INT NOT NULL, -- Usuario que realizó la venta
    fecha_venta DATETIME NOT NULL DEFAULT GETDATE(),
    subtotal DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (subtotal >= 0),
    impuesto DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (impuesto >= 0),
    descuento DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (descuento >= 0),
    total DECIMAL(10,2) NOT NULL CHECK (total >= 0),
    estado VARCHAR(20) NOT NULL DEFAULT 'COMPLETADA' CHECK (estado IN ('COMPLETADA', 'CANCELADA', 'ANULADA')),
    observaciones VARCHAR(500),
    fecha_creacion DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario)
);
GO

-- =============================================
-- TABLA: Detalles_Venta
-- Descripción: Detalle de productos vendidos
-- =============================================
CREATE TABLE Detalles_Venta (
    id_detalle INT PRIMARY KEY IDENTITY(1,1),
    id_venta INT NOT NULL,
    id_producto INT NOT NULL,
    cantidad INT NOT NULL CHECK (cantidad > 0),
    precio_unitario DECIMAL(10,2) NOT NULL CHECK (precio_unitario >= 0),
    descuento DECIMAL(10,2) NOT NULL DEFAULT 0 CHECK (descuento >= 0),
    subtotal DECIMAL(10,2) NOT NULL CHECK (subtotal >= 0),
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta) ON DELETE CASCADE,
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);
GO

-- =============================================
-- TABLA: Movimientos_Inventario
-- Descripción: Registro de movimientos de inventario
-- =============================================
CREATE TABLE Movimientos_Inventario (
    id_movimiento INT PRIMARY KEY IDENTITY(1,1),
    id_producto INT NOT NULL,
    tipo_movimiento VARCHAR(20) NOT NULL CHECK (tipo_movimiento IN ('ENTRADA', 'SALIDA', 'AJUSTE')),
    cantidad INT NOT NULL,
    cantidad_anterior INT NOT NULL,
    cantidad_nueva INT NOT NULL,
    motivo VARCHAR(255),
    id_usuario INT NOT NULL,
    id_venta INT NULL, -- Si el movimiento es por venta
    fecha_movimiento DATETIME DEFAULT GETDATE(),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto),
    FOREIGN KEY (id_usuario) REFERENCES Usuarios(id_usuario),
    FOREIGN KEY (id_venta) REFERENCES Ventas(id_venta)
);
GO

-- =============================================
-- ÍNDICES para mejorar el rendimiento
-- =============================================

-- Índices en Usuarios
CREATE INDEX IX_Usuarios_Rol ON Usuarios(id_rol);
CREATE INDEX IX_Usuarios_Email ON Usuarios(email);

-- Índices en Productos
CREATE INDEX IX_Productos_Categoria ON Productos(id_categoria);
CREATE INDEX IX_Productos_Codigo ON Productos(codigo_producto);
CREATE INDEX IX_Productos_Stock ON Productos(stock_actual);

-- Índices en Clientes
CREATE INDEX IX_Clientes_Documento ON Clientes(numero_documento);

-- Índices en Ventas
CREATE INDEX IX_Ventas_Cliente ON Ventas(id_cliente);
CREATE INDEX IX_Ventas_Usuario ON Ventas(id_usuario);
CREATE INDEX IX_Ventas_Fecha ON Ventas(fecha_venta);
CREATE INDEX IX_Ventas_NumeroFactura ON Ventas(numero_factura);

-- Índices en Detalles_Venta
CREATE INDEX IX_DetallesVenta_Venta ON Detalles_Venta(id_venta);
CREATE INDEX IX_DetallesVenta_Producto ON Detalles_Venta(id_producto);

-- Índices en Movimientos_Inventario
CREATE INDEX IX_MovimientosInventario_Producto ON Movimientos_Inventario(id_producto);
CREATE INDEX IX_MovimientosInventario_Fecha ON Movimientos_Inventario(fecha_movimiento);
CREATE INDEX IX_MovimientosInventario_Venta ON Movimientos_Inventario(id_venta);

GO

-- =============================================
-- TRIGGERS para actualización automática de stock
-- =============================================

-- Trigger para actualizar stock cuando se inserta un detalle de venta
CREATE TRIGGER TRG_ActualizarStock_InsertDetalle
ON Detalles_Venta
AFTER INSERT
AS
BEGIN
    SET NOCOUNT ON;
    
    DECLARE @id_producto INT;
    DECLARE @cantidad INT;
    DECLARE @id_venta INT;
    DECLARE @id_usuario INT;
    DECLARE @stock_anterior INT;
    DECLARE @stock_nuevo INT;
    
    DECLARE cursor_detalles CURSOR FOR
    SELECT id_producto, cantidad, id_venta
    FROM inserted;
    
    OPEN cursor_detalles;
    FETCH NEXT FROM cursor_detalles INTO @id_producto, @cantidad, @id_venta;
    
    WHILE @@FETCH_STATUS = 0
    BEGIN
        -- Obtener stock actual y usuario de la venta
        SELECT @stock_anterior = stock_actual FROM Productos WHERE id_producto = @id_producto;
        SELECT @id_usuario = id_usuario FROM Ventas WHERE id_venta = @id_venta;
        
        -- Calcular nuevo stock
        SET @stock_nuevo = @stock_anterior - @cantidad;
        
        -- Validar que haya stock suficiente
        IF @stock_nuevo < 0
        BEGIN
            RAISERROR('Stock insuficiente para el producto', 16, 1);
            ROLLBACK TRANSACTION;
            RETURN;
        END
        
        -- Actualizar stock del producto
        UPDATE Productos
        SET stock_actual = @stock_nuevo,
            fecha_actualizacion = GETDATE()
        WHERE id_producto = @id_producto;
        
        -- Registrar movimiento de inventario
        INSERT INTO Movimientos_Inventario (
            id_producto, tipo_movimiento, cantidad,
            cantidad_anterior, cantidad_nueva, motivo,
            id_usuario, id_venta
        )
        VALUES (
            @id_producto, 'SALIDA', @cantidad,
            @stock_anterior, @stock_nuevo,
            'Venta registrada', @id_usuario, @id_venta
        );
        
        FETCH NEXT FROM cursor_detalles INTO @id_producto, @cantidad, @id_venta;
    END
    
    CLOSE cursor_detalles;
    DEALLOCATE cursor_detalles;
END;
GO

-- Trigger para actualizar fecha_actualizacion en Productos
CREATE TRIGGER TRG_Productos_ActualizarFecha
ON Productos
AFTER UPDATE
AS
BEGIN
    SET NOCOUNT ON;
    UPDATE Productos
    SET fecha_actualizacion = GETDATE()
    WHERE id_producto IN (SELECT id_producto FROM inserted);
END;
GO

-- =============================================
-- DATOS INICIALES (Seed Data)
-- =============================================

-- Insertar Roles
INSERT INTO Roles (nombre_rol, descripcion) VALUES
('Administrador', 'Acceso completo al sistema'),
('Vendedor', 'Puede realizar ventas y consultar información'),
('Almacenista', 'Gestiona productos e inventario');

-- Insertar Usuario Administrador por defecto
-- Password: admin123 (debe ser hasheado en la aplicación)
INSERT INTO Usuarios (nombre_usuario, email, password_hash, nombre_completo, id_rol) VALUES
('admin', 'admin@omnistock.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqJ5q5q5q5', 'Administrador del Sistema', 1);

-- Insertar Categorías de ejemplo
INSERT INTO Categorias (nombre_categoria, descripcion) VALUES
('Electrónica', 'Dispositivos y componentes electrónicos'),
('Ropa', 'Prendas de vestir y accesorios'),
('Alimentos', 'Productos alimenticios'),
('Hogar', 'Artículos para el hogar'),
('Deportes', 'Artículos deportivos');

GO

-- =============================================
-- VISTAS ÚTILES
-- =============================================

-- Vista: Productos con información de categoría
CREATE VIEW VW_Productos_Completo AS
SELECT 
    p.id_producto,
    p.codigo_producto,
    p.nombre_producto,
    p.descripcion,
    c.nombre_categoria,
    p.precio_venta,
    p.precio_compra,
    p.stock_actual,
    p.stock_minimo,
    p.unidad_medida,
    CASE 
        WHEN p.stock_actual <= p.stock_minimo THEN 'BAJO'
        WHEN p.stock_actual <= (p.stock_minimo * 1.5) THEN 'MEDIO'
        ELSE 'NORMAL'
    END AS estado_stock,
    p.activo,
    p.fecha_creacion,
    p.fecha_actualizacion
FROM Productos p
INNER JOIN Categorias c ON p.id_categoria = c.id_categoria;
GO

-- Vista: Ventas con información completa
CREATE VIEW VW_Ventas_Completo AS
SELECT 
    v.id_venta,
    v.numero_factura,
    v.fecha_venta,
    c.nombre_completo AS nombre_cliente,
    c.numero_documento AS documento_cliente,
    u.nombre_completo AS nombre_vendedor,
    v.subtotal,
    v.impuesto,
    v.descuento,
    v.total,
    v.estado,
    v.observaciones
FROM Ventas v
INNER JOIN Clientes c ON v.id_cliente = c.id_cliente
INNER JOIN Usuarios u ON v.id_usuario = u.id_usuario;
GO

-- Vista: Resumen de inventario
CREATE VIEW VW_Resumen_Inventario AS
SELECT 
    c.nombre_categoria,
    COUNT(p.id_producto) AS total_productos,
    SUM(p.stock_actual) AS stock_total,
    SUM(CASE WHEN p.stock_actual <= p.stock_minimo THEN 1 ELSE 0 END) AS productos_bajo_stock,
    SUM(p.stock_actual * p.precio_compra) AS valor_inventario
FROM Categorias c
LEFT JOIN Productos p ON c.id_categoria = p.id_categoria AND p.activo = 1
GROUP BY c.id_categoria, c.nombre_categoria;
GO

PRINT 'Base de datos OmniStock creada exitosamente!';
GO
