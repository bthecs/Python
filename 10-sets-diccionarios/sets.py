"""
Set es un tipo de dato, para tener una coleccion de valores,
pero no tiene ni indice ni orden
"""
personas = {
    "Victor",
    "Manolo",
    "Lautaro"
}
personas.add("Pablo")
personas.remove("Manolo")
print(type(personas))
print(personas)