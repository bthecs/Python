"""
Ejercicio 5: Hacer un programa que muestre todos los numeros entre dos numeros que diga el usuario
"""


num1 = int(input("Ingrese numero 1: "))
num2 = int(input("Ingrese numero 2: "))

for contador in range(num1,num2-1):
    contador = contador + 1
    print(f"numeros entre medio {contador}")