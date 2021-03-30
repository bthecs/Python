"""
Ejercicio 3:
    Escribir un programa que muestre los cuadrados (un numero multiplicado por si mismo) de los 60
    primeros numeros naturales. Resolver con for y con while
"""
numero = 0

for numero in range(1,61):
    cuadrado = numero*numero
    print(f"{cuadrado}")

while numero <= 60:
    cuadrado_while = numero*numero
    numero +=1
    print(f"{cuadrado_while}")
    