use TiendaDeInformatica;

#1.- Get the names of the products in the store
SELECT nombre FROM articulo;

#2.- Get the names and prices of the products in the store
SELECT nombre, precio FROM articulo;

#3.- Get the names of products whose price is less than or equal to $###
SELECT nombre FROM articulo WHERE precio > 100000;

#4.- Get all the data of articles whose price is between $## and $### (both amounts included)
SELECT * FROM articulo WHERE precio BETWEEN 1000 AND 30000;

#5.- Get the name and price in USD (i.e., the price in pesos divided by the exchange rate of the day entered manually)
SELECT nombre, precio * .67 FROM articulo;

#6.- Select the average price of all products (AVG)
SELECT AVG(precio) FROM articulo;

#7.- Get the average price of articles whose manufacturer code is 2
SELECT AVG(precio) FROM articulo WHERE id_fabricante = 2;

#8.- Get the number of articles whose price is greater than or equal to $## (COUNT)
SELECT COUNT(*) FROM articulo WHERE precio >=180;

#9.- Get the name and price of articles whose price is greater than or equal to $## and order them descending by price, then ascending by name

#10.- Get a complete list of articles, including for each article the article data and its manufacturer data
SELECT * FROM articulo, fabricante WHERE articulo.id_fabricante = fabricante.id_fabricante;

#11.- Get a list of articles, including the name of the article, its price, and the name of its manufacturer
SELECT articulo.nombre, precio, fabricante.nombre
FROM articulo, fabricante
WHERE articulo.id_fabricante = fabricante.id_fabricante;

#12.- Get the average price of products from each manufacturer, showing only the manufacturer codes
SELECT AVG(precio), id_fabricante FROM articulo
GROUP BY id_fabricante;

#13.- Get the average price of products from each manufacturer, showing the manufacturer's name
SELECT AVG(precio), id_fabricante FROM articulo
GROUP BY fabricante.nombre;

#14.- Get the names of manufacturers offering products whose average price is greater than or equal to $###

#15.- Get the name and price of the cheapest article

#16.- Get a list with the name and price of the most expensive articles from each supplier (including the supplier's name)

#17.- Add a new product: Speakers for $### (from manufacturer x)
#INSERT INTO articulo(nombre, precio, id_fabricante); 
# VALUES ("Speakers", 2000, x)

#18.- Change the name of product # to 'Laser Printer'

#19.- Apply a 10% discount to all products
UPDATE articulo SET precio = precio * 0.9;

#20.- Apply a $## discount to all products whose price is greater than or equal to $###.
