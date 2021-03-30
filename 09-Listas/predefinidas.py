cantantes = ['2pac','julio','bud bany']
numeros = [1,2,10,9,5,6,7]

#Ordenar lista
print(numeros)
numeros.sort()
print(numeros)

#Agregar elementos a lista
cantantes.append("Chino y nacho")
cantantes.insert(1,"David bisbal")
print(cantantes)

#Eliminar elementos
cantantes.pop(1)
cantantes.remove("2pac")
print(cantantes)

# Dar la vuelta
numeros.reverse()
print(numeros)

# Buscar dentro de una lista
print("julio" in cantantes)


#contar elementos
print(len(cantantes))

#cuantas veces aparece un elemento
numeros.append(8)
numeros.append(8)
print(numeros.count(8))

#conseguir indice
print(cantantes.index("julio"))

#unir listas
cantantes.extend(numeros)
print(cantantes)