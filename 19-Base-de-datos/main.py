import mysql.connector

#Conexion
database = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "",
    database = "master_python"
    
)

# ¿La conexion ha sido correcta?
#print(database)

#cursor que nos permite ejecutar las consultas
cursor = database.cursor(buffered=True)
"""
cursor.execute("CREATE DATABASE IF NOT EXISTS master_python")

cursor.execute("SHOW DATABASES")

for bd in cursor:
    print(bd)
"""
# Crear tablas
cursor.execute("""
CREATE TABLE IF NOT EXISTS vehiculos(
id int(10) auto_increment not null,
marca varchar(40) not null,
modelo varchar(40) not null,
precio float(10,2) not null,
CONSTRAINT pk_vehiculo PRIMARY KEY(id)
)
""")

cursor.execute("SHOW TABLES")

for tb in cursor:
    print(tb)

#cursor.execute("INSERT INTO vehiculos VALUES(null, 'Opel', 'Astra','18500')")
coches = [
    ('Logan', 'Renault','1200000'),
    ('Argo', 'Fiat','1500000'),
    ('Mobi', 'Fiat','1200000'),
    ('Chronos', 'Fiat','1800000'),
    ('S10 full', 'Chevrolet','3200000'),
    ('Alaska', 'Renault','2200000')
]

#Para cargar varios datos en la tabla
#cursor.executemany("INSERT INTO vehiculos VALUES(null, %s,%s,%s)", coches)

#Listar elementos de la tabla
#cursor.execute("SELECT * FROM vehiculos")
#vehiculos = cursor.fetchall()

#for veh in vehiculos:
#    print(veh[0],"/",veh[1],"/",veh[3])


#Como borrar
cursor.execute("DELETE FROM vehiculos WHERE modelo = 'Chevrolet'")
database.commit()

#Muestra la cantidad de elementos que se borraron
print(cursor.rowcount, "Borrados!!")

#Como actualizar
cursor.execute("UPDATE vehiculos SET marca = 'Leon' WHERE marca = 'Mobi' ")
database.commit()
print(cursor.rowcount, "Actualizados!!")