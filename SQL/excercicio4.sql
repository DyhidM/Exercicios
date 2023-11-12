/*Ejercicio 4
                   Nivel de dificultad: Experto

1. Crea una tabla llamada "Pedidos" con las columnas: "id" (entero, clave primaria), 
"id_usuario" (entero, clave foránea de la tabla "Usuarios") y "id_producto" (entero, clave foránea de la tabla "Productos").*/
CREATE TABLE pedidos (
	id SERIAL PRIMARY KEY,
	producto_id INT,
	usuario_id INT,
	CONSTRAINT fk_producto_id 
	  FOREIGN KEY(producto_id) REFERENCES Productos(id),
	CONSTRAINT fk_usuario_id 
	  FOREIGN KEY(usuario_id) REFERENCES Usuarios(id)
);

/*2. Inserta al menos tres registros en la tabla "Pedidos" que relacionen usuarios con productos.*/
INSERT INTO public.pedidos(producto_id,usuario_id)
VALUES
(2,7),(2,5),(2,6),
(3,3),
(4,4),(4,3);

/*3. Realiza una consulta que muestre los nombres de los usuarios y los nombres de los productos que han comprado, 
incluidos aquellos que no han realizado ningún pedido (utiliza LEFT JOIN y COALESCE).*/
SELECT u.name as usuario, COALESCE(productos.name, 'Ningún pedido') as producto
FROM public.usuarios u
LEFT JOIN public.pedidos ON pedidos.usuario_id = u.id
LEFT JOIN public.productos ON pedidos.producto_id = productos.id;

/*4. Realiza una consulta que muestre los nombres de los usuarios que han realizado un pedido, pero también los que
 no han realizado ningún pedido (utiliza LEFT JOIN).*/
SELECT u.name as usuario, COALESCE (pedidos.id, 0) as pedido
FROM public.usuarios u
LEFT JOIN public.pedidos ON pedidos.usuario_id = u.id;

/*5. Agrega una nueva columna llamada "cantidad" a la tabla "Pedidos" y actualiza los registros existentes con 
un valor (utiliza ALTER TABLE y UPDATE)*/
ALTER TABLE public.pedidos
ADD COLUMN cantidad INT;

UPDATE public.pedidos
SET cantidad = 3
WHERE producto_id = 2;