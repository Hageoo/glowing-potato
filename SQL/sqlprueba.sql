# create database prueba;
# If the database already exists, it will throw an error when trying to execute it again.
# To execute a specific block of code, select it with the left click.

use prueba; # This loads the "prueba" database into memory.
# All the code executed from this point will be saved in the "prueba" database.

CREATE TABLE Alumnos
(
IdAlumno int primary key not null,
Nombre varchar (45) not null,
Apellidos varchar (45) not null,
Edad int not null, # not null = cannot be left empty, does not accept null values.
Direccion_Residencia varchar (50) # Names cannot have a space (use all together or with _).
# Since this is the last column, there is no comma at the end of the statement.
); 

# Click the button located on the right side of SCHEMAS to refresh.
# To view the table, go to Tables - alumnos (table name) - click the button on the right side.
# You can also create tables graphically in Workbench.
# First, go to Schemas, find the database, right-click on Tables, and create a new table.
# You can add comments to tables, and then proceed to create the table as needed.
# PK = primary key, NN = not null, UQ = unique index, B = binary column.
# UN = unsigned data type, FZ = fills up values for that column with 0's if it's numeric.
# AI = auto-increment, G = generated column.
