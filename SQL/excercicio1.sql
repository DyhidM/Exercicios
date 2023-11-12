/* ## EXCERCICIO 1
1. Crear una tabla llamada "Clientes" con las columnas: id (entero, clave primaria), nombre (texto) y email (texto). */
CREATE TABLE Clientes(
    id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	email VARCHAR(255)
)

/* 2. Insertar un nuevo cliente en la tabla "Clientes" con id=1, nombre="Juan" y email="juan@example.com".*/
INSERT INTO Clientes(id, name, email)
VALUES (1, 'Juan', 'juan@gmailexample.com');	

/* 3. Actualizar el email del cliente con id=1 a "juan@gmail.com".*/
UPDATE Clientes
SET email = 'juan@gmail.com'
WHERE id = 1;

/* 4. Eliminar el cliente con id=1 de la tabla "Clientes".*/
DELETE FROM Clientes
WHERE id = 1;

/* 5. Crear una tabla llamada "Pedidos" con las columnas: id (entero, clave primaria),cliente_id (entero, 
clave externa referenciando a la tabla "Clientes"), producto (texto) y cantidad (entero).*/
CREATE TABLE Pedidos(
    id SERIAL PRIMARY KEY,
	cliente_id INT,
	producto VARCHAR(255),
	cantidad INT,
	CONSTRAINT fk_cliente_id FOREIGN KEY(cliente_id) REFERENCES Clientes(id)
	
)

/* 6. Insertar un nuevo pedido en la tabla "Pedidos" con id=1, cliente_id=1, producto="Camiseta" y cantidad=2.*/
INSERT INTO Pedidos(id, producto, cantidad)
VALUES (1, 'Camiseta', 2);

/* 7. Actualizar la cantidad del pedido con id=1 a 3. */
UPDATE Pedidos
SET cantidad = 3
WHERE id = 1;

/* 8. Eliminar el pedido con id=1 de la tabla "Pedidos".*/
DELETE FROM Pedidos
WHERE id = 1;
	
/* 9. Crear una tabla llamada "Productos" con las columnas: id (entero, clave primaria), nombre (texto) y precio (decimal).*/
 CREATE TABLE Productos(
    id SERIAL PRIMARY KEY,
	NAME VARCHAR(255),
	PRECIO DECIMAL
)
	
/* 10. Insertar varios productos en la tabla "Productos" con diferentes valores.*/
 INSERT INTO Productos(name, precio)
VALUES 
('harina', 1.35),
('huevos', 2.35),
('pan', 2.50),
('manzanas', 5.00),
('leche', 3.30);

/* 11. Consultar todos los clientes de la tabla "Clientes". */
SELECT NAME FROM public.clientes

/* 12. Consultar todos los pedidos de la tabla "Pedidos" junto con los nombres de los clientes correspondientes.*/
SELECT c.name as nombre_cliente, p.*
FROM public.clientes c
INNER JOIN public.pedidos p
ON p.cliente_id = c.id;
	
 /* 13. Consultar los productos de la tabla "Productos" cuyo precio sea mayor a $50. */
 SELECT p.name as producto, precio
FROM public.productos p 
WHERE precio > 50;

/*14. Consultar los pedidos de la tabla "Pedidos" que tengan una cantidad mayor o igual a 5. */
SELECT p.producto, p.cantidad
FROM public.pedidos p 
WHERE cantidad >= 5;

/* 15. Consultar los clientes de la tabla "Clientes" cuyo nombre empiece con la letra "A".*/
SELECT c.name
FROM public.clientes c
WHERE  name LIKE 'A%';

/* 16. Realizar una consulta que muestre el nombre del cliente y el total de pedidos realizados por cada cliente.*/
SELECT Clientes.name, COUNT(Pedidos.id) AS total_pedidos
FROM Clientes
LEFT JOIN Pedidos ON Clientes.id = Pedidos.cliente_id
GROUP BY Clientes.name;


/*17. Realizar una consulta que muestre el nombre del producto y la cantidad total de pedidos de ese producto. */
SELECT Productos.name, SUM(Pedidos.cantidad) AS cantidad_total
FROM Productos
LEFT JOIN Pedidos ON Productos.id = Pedidos.producto
GROUP BY Productos.name;

/* 18. Agregar una columna llamada "fecha" a la tabla "Pedidos" de tipo fecha.*/
ALTER TABLE Pedidos
ADD fecha DATE;

/*19. Agregar una clave externa a la tabla "Pedidos" que haga referencia a la tabla "Productos" en la columna "producto".*/
ALTER TABLE Pedidos
DROP COLUMN producto;

ALTER TABLE Pedidos
ADD producto INTEGER;

ALTER TABLE public.pedidos 
ADD CONSTRAINT producto_fk
FOREIGN KEY(producto)
REFERENCES Productos(id);
ALTER TABLE public.pedidos
ALTER COLUMN producto 
SET NOT NULL;

/*20. Realizar una consulta que muestre los nombres de los clientes, los nombres de los productos y las cantidades de los 
pedidos */
SELECT p.name, public.pedidos.cantidad, public.productos.name
FROM public.clientes p
INNER JOIN Pedidos ON p.id = Pedidos.cliente_id
INNER JOIN Productos ON productos.id = Pedidos.producto;