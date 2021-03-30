"""
Listas(arrays)
Son colecciones o conjuntos de datos/valores, bajo un unico nombre
Para acceder a esos valores podemos usar un indice numerico
"""


#Definir listas
peliculas = ["Batman", "Spiderman", "El señor de los anillos"]

cantantes = list(("2pac", "Drake", "Arjona"))

years = list(range(2020,2050))

variada = ["Victor",30,2.5,True,"Texto"]
"""
print(peliculas)
print(cantantes)
print(years)
print(variada)

# Indices

peliculas[1] = "Gran Torino"
peliculas[2] = "El Hobbit"
print(peliculas[1])
print(peliculas[-2])
print(cantantes[1:3])
print(peliculas[1:])

#Añadir elementos a lista

cantantes.append("CRO")
print(cantantes)

# Recorrer listas
print("##### LISTADO PELIS ######")

nueva_pelicula = ""

while nueva_pelicula != "parar":
    nueva_pelicula = input("Introduce la nueva pelicula: ")
    if nueva_pelicula != "parar":
        peliculas.append(nueva_pelicula)

for pelicula in peliculas:
    print(f"{peliculas.index(pelicula)+1}. {pelicula}")
"""
# Lista multidimensionales

print("\n###### Contactos ######\n")
contactos = [
    [
        "Antonio",
        "antonio@antonio.com"
    ],
    [
        "Luis",
        "luis@luis.com"
    ],
    [
        "Lautaro",
        "Lautaro@lautaro.com"
    ]
]
print(contactos[1][1])

for contacto in contactos:
    for elemento in contacto:
        print(elemento)