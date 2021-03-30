"""
Variable local: Se define dentro de la funcion y no se puede usar fuera de ella, solo estan disponibles dentro.
A no ser que hagamos un return

Variable global: Son las que se declaran fuera de una funcion y estan disponibles dentro y fuera de ellas

"""

#Variable Global
frase = "Hola"

print(frase)


#Variable Local

def holaMundo():
    frase = "Hola mundo"
    print("Dentro de la funcion: ")
    print(frase)

    global instagram
    instagram = "lautaro.c.gimenez"
    print("Dentro: ", instagram)

    year = 2021
    print(year)

    return "Dato devuelto: " + str(year)

print(holaMundo())
print(instagram)
