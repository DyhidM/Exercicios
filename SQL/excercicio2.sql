                         /*Ejercicio 2
Nivel de dificultad: Fácil

1. Crea una base de datos llamada "MiBaseDeDatos".*/
CREATE DATABASE IF NOT EXISTS "MiBaseDeDatos";

/*2. Crea una tabla llamada "Usuarios" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "edad" (entero).*/
CREATE TABLE IF NOT EXISTS Usuarios(
    id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL,
	edad INT
)
/*3. Inserta dos registros en la tabla "Usuarios".*/
 INSERT INTO public.usuarios(name,age)
 VALUES
	( 'Mariia',30),
	( 'Taras',36);

/*4. Actualiza la edad de un usuario en la tabla "Usuarios".*/
 UPDATE public.usuarios
 SET age = 35
 WHERE id = 2;

 /*5. Elimina un usuario de la tabla "Usuarios". */
 DELETE FROM public.usuarios
 WHERE id = 2;

                    /*Nivel de dificultad: Moderado
1. Crea una tabla llamada "Ciudades" con las columnas: "id" (entero, clave primaria), "nombre" (texto) y "pais" (texto).*/
 CREATE TABLE IF NOT EXISTS ciudad(
 id SERIAL PRIMARY KEY,
	 name VARCHAR(255) NOT NULL,
	 pais VARCHAR(255)
 )

 /*2. Inserta al menos tres registros en la tabla "Ciudades".*/
 INSERT INTO public.ciudades (name,pais)
VALUES
('Ternopil','Ucrania'),
('Barcelona','España'),
('París','Francia'),
('Varsovia','Polonia')

/*3. Crea una foreign key en la tabla "Usuarios" que se relacione con la columna "id" de la tabla "Ciudades".*/
 ALTER TABLE public.usuarios
 ADD COLUMN ciudad_id INT,
   ADD CONSTRAINT fk_ciudad
   FOREIGN KEY(ciudad_id) REFERENCES public.ciudades(id);

/*4. Realiza una consulta que muestre los nombres de los usuarios junto con el nombre de su ciudad y país (utiliza un LEFT JOIN).*/
SELECT u.name, public.ciudades.name, public.ciudades.pais
FROM public.usuarios u
LEFT JOIN public.ciudades ON
u.cuidad_id = public.ciudades.id;

/*5. Realiza una consulta que muestre solo los usuarios que tienen una ciudad asociada (utiliza un INNER JOIN).*/
SELECT u.name, ciudades.name as ciudad
FROM public.usuarios u
INNER JOIN public.ciudades ON u.ciudad_id = ciudades.id;






