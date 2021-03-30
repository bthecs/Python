# Importar modulo
import sqlite3

#Conexion
conexion = sqlite3.connect('19-Base-de-datos/pruebas.db')

#Crear cursor
cursor = conexion.cursor()

#Crear tabla
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos(
    id INTEGER PRIMARY KEY AUTOINCREMENT, 
    titulo VARCHAR(255), 
    descripcion text, 
    precio int(255) 
)""")

#Guardar cambios
conexion.commit()

#Insertar datos
"""
cursor.execute("INSERT INTO productos VALUES (null, 'producto 1', 'descripcion de mi producto', '550')")
conexion.commit()
"""

#Borrar registros
#cursor.execute("DELETE FROM productos")
#conexion.commit()


#insertar muchos registros de golpe
productos = [
    ("Ordenador portatil", "buen pc", 700),
    ("Samsung A51", "Buen cel", 750),
    ("Admiral 43°", "buen Tele", 1000),
    ("Heladera", "buen heladera", 500),
    ("cocina", "buen cocina", 300),
]
cursor.executemany("INSERT INTO productos VALUES (null, ?, ?, ?)", productos)
conexion.commit()

#Listar datos
cursor.execute("SELECT * FROM productos WHERE precio >=700")
productos = cursor.fetchall()

for producto in productos:
    print("ID: ", producto[0])
    print("Titulo: ", producto[1])
    print("Descripcion: ", producto[2])
    print("Precio: ", producto[3])
    print("\n")

print("-------------------------------")    
cursor.execute("SELECT titulo FROM productos")
producto = cursor.fetchone()
print(producto)

#Cerrar conexion
conexion.close()