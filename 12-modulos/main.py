"""
Modulos: son funcionalidades ya hechas para reutilizar.
Podemos conseguir modulos que ya vienen en el lenguaje, modulos en internet y modulos propios
"""
"""
#importar modulo propio
import mimodulo

#importar una funcion de mimodulo
from mimodulo import holaMundo

#importar todas las funciones de mi modulo y no tener que utilizar mimodulo.calculadora ni .holaMundo
from mimodulo import *

print(holaMundo("Lautaro"))

print(calculadora(5,10,True))

#modulo fechas
import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()
print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y, %H:%M:%S")
print("Mi fecha personalizada: ",fecha_personalizada)

print(datetime.datetime.now().timestamp())
print(datetime.datetime.now().time())
"""
#modulo matematicas
import math

print("Raiz cuadrada de 10: ",math.sqrt(10))

print("Numero pi: ", float(math.pi))

print("Redondear hacia arriba: ", math.ceil(6.92134))

print("Redondear hacia abajo: ", math.floor(6.92134))

# Modulo random
import random

print("numero aleatorio entre 15 y 67: ", random.randint(15,67))
