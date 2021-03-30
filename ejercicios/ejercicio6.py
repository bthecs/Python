"""
Mostrar todas las tablas de multiplicar del 1 al 10
"""

for numero_tabla in range(1,11):
    for numero in range(1,11):
        print(f"{numero}x{numero_tabla} = {numero_tabla * numero}")