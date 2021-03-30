"""
Mostrar numeros impares entre dos numeros ingresados por el user
"""

num1 = int(input("num1: "))
num2 = int(input("num2: "))

for numero in range(num1,num2):
    if numero%2 != 0:
        print(f"{numero}")
    