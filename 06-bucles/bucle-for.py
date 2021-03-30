"""
#FOR
for variable in elemento iterable (LISTA, RANGO, ETC)
    BLOQUE DE INSTRUCCIONES
"""

contador = 0
resultado = 0

for contador in range(0,10):
    print("Voy por el "+ str(contador))

    resultado = resultado + contador
    resultado += contador

print(f"El resultado es : {resultado}")

#ejemplo tablas de multiplicar

print("###################### EJEMPLO################")

numero_user = int(input("De que numero quieres la tabla?: "))

if numero_user < 1:
    numero_user = 1

print(f"#### Tabla de multiplicar del numero {numero_user}####")

for numero_tabla in range(1,11):
    print(f"{numero_user}x{numero_tabla} = {numero_user*numero_tabla}")

