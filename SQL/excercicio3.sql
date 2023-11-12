/*
Ejercicio 3
                                    Nivel de dificultad: Difícil
1. Crea una tabla llamada "Productos" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "precio" (numérico).*/
CREATE TABLE productos(
    id SERIAL PRIMARY KEY,
	name VARCHAR(255),
	price DECIMAL
);

/*2. Inserta al menos cinco registros en la tabla "Productos".*/
INSERT INTO Productos (name,price)
VALUES
('mesa', 200),
('silla', 65),
('armario', 1365),
('cama', 1200),
('estanteria', 25);

/*3. Actualiza el precio de un producto en la tabla "Productos".*/
UPDATE Productos p
SET price = 1215
WHERE p.name = 'cama';

/*4. Elimina un producto de la tabla "Productos".*/
DELETE FROM public.productos p
WHERE p.name = 'estanteria';

/*5. Realiza una consulta que muestre los nombres de los usuarios junto con los nombres de los productos que han comprado 
(utiliza un INNER JOIN con la tabla "Productos").*/
CREATE TABLE pedidos (
	id SERIAL PRIMARY KEY,
	producto_id INT,
	cantidad INT,
	usuario_id INT,
	CONSTRAINT fk_producto_id 
	  FOREIGN KEY(producto_id) REFERENCES Productos(id),
	CONSTRAINT fk_usuario_id 
	  FOREIGN KEY(usuario_id) REFERENCES Usuarios(id)
);

INSERT INTO public.pedidos(producto_id,cantidad,usuario_id)
VALUES
(2,12,7),(2,6,5),(2,8,6),
(3,1,3),
(4,2,4),(4,2,3);

SELECT u.name as usuario, public.productos.name as producto, public.pedidos.cantidad
FROM public.usuarios u
INNER JOIN public.pedidos ON public.pedidos.usuario_id = u.id
INNER JOIN public.productos on pedidos.producto_id = productos.id;