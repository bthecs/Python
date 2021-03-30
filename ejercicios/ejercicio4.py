"""
Ejercicio 4: PEdir 2 num al user y hacer las operaciones basic de una calculadora e imprimir
"""

suma = 0
resta = 0
multi = 0
div = 0

while True:
    """
        1. Suma de numeros
        2. Resta de numeros
        3. Multi de numeros
        4. Division de numeros
        5. Salir
    """
    num1 = int(input("Ingrese el primer numero: "))
    num2 = int(input("Ingrese el segundo numero: "))

    opt = int(input("ingrese la operacion que desea realizar: "))
    if opt == 1:
        suma = num1+num2
        print(f"La Suma es {suma}")
    
    elif opt == 2:
        resta = num1-num2
        print(f"La resta es {resta}")

    elif opt == 3:
        multi = num1*num2
        print(f"La Multi es {multi}")
    
    elif opt == 4:
        div = num1/num2
        print(f"La Division es {div}")
    
    elif opt == 5:
        break
