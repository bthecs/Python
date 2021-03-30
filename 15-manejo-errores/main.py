#Capturar excepciones y manejar errores en codigo
#susceptible a fallos/errores


try:
    nombre = input("Cual es tu nombre?: ")

    if len(nombre) > 1:
        nombre_user = "El nombre es: " + nombre
        

    print(nombre_user)
except:
    print("Nombre invalido :D :/")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin de la iteracion")
