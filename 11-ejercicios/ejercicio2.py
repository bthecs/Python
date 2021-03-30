"""
ejercicio 2: Escribir un programa que añada valores a una lista mientras que su longitud sea menor a 8 y luego mostrar la lista
plus: Usar while y for
"""

numeros = [1,2,3,4,5,6,7]

while True:
    """
        1. Añadir valor
        2. Mostrar lista
        3. Salir
    """
    opt = int(input("Ingrese la opcion deseada: "))
    if opt==1:
        valor = int(input("Ingrese valor menor a 8 digitos: "))
        if valor < 9999999:
            if len(numeros) < 8:
                numeros.append(valor)
            else:
                print("valor invalido o lista llena")
        else:
            print("valor invalido o lista llena")
    elif opt==2:
        for num in numeros:
            print(num)
    elif opt==3:
        break
