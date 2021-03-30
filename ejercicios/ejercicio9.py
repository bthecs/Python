"""
Hacer un programa que pida numeros al usuario indefinidamente hasta meter el numero 111
"""

while True:
    numero = int(input("ingrese numero: "))
    if numero != 111:
        print(f"{numero}")
    else:
        break