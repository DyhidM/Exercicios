/*Ejercicio 5

1. Crea una tabla llamada "Clientes" con las columnas id (entero) y nombre (cadena de texto).*/
CREATE TABLE IF NOT EXISTS clientes(
    id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL
)

/*2. Inserta un cliente con id=1 y nombre='John' en la tabla "Clientes".*/
INSERT INTO clientes(id,name)
VALUES(1,'John');

/*3. Actualiza el nombre del cliente con id=1 a 'John Doe' en la tabla "Clientes".*/
UPDATE clientes
SET name = 'John Doe'
WHERE id =1;

/*4. Elimina el cliente con id=1 de la tabla "Clientes".*/
DELETE FROM clientes
WHERE id = 1;

/*5. Lee todos los clientes de la tabla "Clientes".*/
SELECT * FROM public.clientes;

/*6. Crea una tabla llamada "Pedidos" con las columnas id (entero) y cliente_id (entero).*/
CREATE TABLE IF NOT EXISTS pedidos(
    id SERIAL PRIMARY KEY,
    cliente_id INT
);
/*7. Inserta un pedido con id=1 y cliente_id=1 en la tabla "Pedidos".*/
INSERT INTO pedidos(id,cliente_id)
VALUES(1,1);

/*8. Actualiza el cliente_id del pedido con id=1 a 2 en la tabla "Pedidos".*/
UPDATE pedidos
SET cliente_id =2
WHERE id = 1;

/*9. Elimina el pedido con id=1 de la tabla "Pedidos".*/
DELETE FROM  pedidos
WHERE id = 1;

/*10. Lee todos los pedidos de la tabla "Pedidos".*/
SELECT * FROM public.pedidos;

/*11. Crea una tabla llamada "Productos" con las columnas id (entero) y nombre (cadena de texto).*/
CREATE TABLE IF NOT EXISTS productos(
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

/*12. Inserta un producto con id=1 y nombre='Camisa' en la tabla "Productos".*/
INSERT INTO Productos (id,name)
VALUES(1,'Camisa');

/*13. Actualiza el nombre del producto con id=1 a 'Pantalón' en la tabla "Productos".*/
UPDATE Productos
SET name = 'Pantalon'
WHERE id = 1;

/*14. Elimina el producto con id=1 de la tabla "Productos".*/
DELETE FROM Productos
WHERE id = 1;

/*15. Lee todos los productos de la tabla "Productos".*/
SELECT * FROM public.productos;

/*16. Crea una tabla llamada "DetallesPedido" con las columnas pedido_id (entero) y producto_id (entero).*/
CREATE TABLE DetallesPedido(
   pedido_id INT NOT NULL,
   producto_id INT NOT NULL
);

/*17. Inserta un detalle de pedido con pedido_id=1 y producto_id=1 en la tabla "DetallesPedido".*/
INSERT INTO DetallesPedido(pedido_id,producto_id)
VALUES(1,1);

/*18. Actualiza el producto_id del detalle de pedido con pedido_id=1 a 2 en la tabla "DetallesPedido".*/
UPDATE DetallesPedido
SET producto_id = 2
WHERE pedido_id =1;

/*19. Elimina el detalle de pedido con pedido_id=1 de la tabla "DetallesPedido".*/
DELETE FROM DetallesPedido
WHERE pedido_id = 1;

/*20. Lee todos los detalles de pedido de la tabla "DetallesPedido".*/
SELECT * FROM DetallesPedido;

/*21. Realiza una consulta para obtener todos los clientes y sus pedidos correspondientes utilizando un inner join.*/
INSERT INTO clientes (id, name)
VALUES
(1,'Pedro'),
(2,'Marta'),
(3,'Anna'),
(4,'Juan'),
(5,'Mila');
INSERT INTO Productos (id,name)
VALUES
(1,'mesa'),
(2,'silla'),
(3,'armario'),
(4,'cama'),
(5,'estanteria'),
(6,'espejo');
INSERT INTO Pedidos (id,cliente_id)
VALUES
(1, 2),
(2,1),
(3,2),
(4,5);
INSERT INTO Detallespedido (pedido_id,producto_id)
VALUES
(1,2),
(2,6),
(3,2),
(4,5);

ALTER TABLE public.pedidos
ADD CONSTRAINT fk_cliente_id
FOREIGN KEY (clientes_id) REFERENCES Clientes(id);

SELECT clientes.name as clientes, pedidos.id as pedido
FROM clientes
INNER JOIN Pedidos ON Pedidos.cliente_id = Clientes.id;

/*22. Realiza una consulta para obtener todos los clientes y sus pedidos correspondientes utilizando un left join.*/
SELECT clientes.name as clientes , pedidos.id as pedido
FROM Clientes
LEFT JOIN Pedidos ON Pedidos.cliente_id = Clientes.id

/*23. Realiza una consulta para obtener todos los productos y los detalles de pedido correspondientes utilizando un inner join.*/
ALTER TABLE public.DetallesPedido
ADD CONSTRAINT fk_pedido_id
FOREIGN KEY (pedido_id) REFERENCES Pedidos(id),
ADD CONSTRAINT fk_producto_id
FOREIGN KEY(producto_id) REFERENCES Productos(id);

SELECT Productos.name as productos, Clientes.name as cliente, Pedidos.id as pedido
FROM Productos
INNER JOIN DetallesPedido ON Productos.id = DetallesPedido.producto_id
INNER JOIN Pedidos ON DetallesPedido.pedido_id = Pedidos.id
INNER JOIN Clientes ON Clientes.id = Pedidos.cliente_id;

/*24. Realiza una consulta para obtener todos los productos y los detalles de pedido correspondientes utilizando un left join.*/
SELECT Productos.name as productos, Clientes.name as cliente, Pedidos.id as pedido
FROM Productos
LEFT JOIN DetallesPedido ON Productos.id = DetallesPedido.producto_id
LEFT JOIN Pedidos ON DetallesPedido.pedido_id = Pedidos.id
LEFT JOIN Clientes ON Clientes.id = Pedidos.cliente_id;

/*25. Crea una nueva columna llamada "telefono" de tipo cadena de texto en la tabla "Clientes".*/
ALTER TABLE clientes
ADD COLUMN telefono VARCHAR(255);

/*26. Modifica la columna "telefono" en la tabla "Clientes" para cambiar su tipo de datos a entero.*/ 
ALTER TABLE public.clientes
ALTER COLUMN telefono TYPE INTEGER
USING telefono::integer;

/*27. Elimina la columna "telefono" de la tabla "Clientes".*/
ALTER TABLE Clientes
DROP COLUMN telefono;

/*28. Cambia el nombre de la tabla "Clientes" a "Usuarios".*/
ALTER TABLE Clientes
RENAME TO Usuarios;

/*29. Cambia el nombre de la columna "nombre" en la tabla "Usuarios" a "nombre_completo".*/
ALTER TABLE Usuarios
RENAME COLUMN name TO nombre_completo;

/*30. Agrega una restricción de clave primaria a la columna "id" en la tabla "Usuarios".*/
ALTER TABLE public.usuarios
ADD PRIMARY KEY (id);