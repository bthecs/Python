"""
Hacer el programa que tenga una lista de 8 numeros enteros y haga lo siguiente:
-Recorrer la lista y mostrarla
-Ordenarla y mostrarla
-Mostrar su longitud
-Buscar algun elemento (que el usuario pida por teclado)
"""

numeros = [1,3,4,2,5,6,2,8]

#Recorrer y mostrarla
for num in numeros:
    print(num)

#Ordenarla y mostrarla
numeros.sort()
print(numeros)

#Mostrar su longitud
print(len(numeros))

#Buscar algun elemento (que el usuario pida por teclado)
data = int(input("Numero que desea verificar en la lista: "))

comprobar = isinstance(data, int)
while not comprobar or data <=0:
    data = int(input("Numero que desea verificar en la lista: "))
else:
    print(f"Has introducido el {data}")

print(f"Buscar en la lista el numero {data}")

search = numeros.index(data)
print(f"El numero buscado existe en la lista es el indice: {search}")