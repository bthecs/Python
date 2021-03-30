import os

# Crear carpeta
if not os.path.isdir("./14-sistema-archivos/mi_carpeta"):
    os.mkdir("./14-sistema-archivos/mi_carpeta")
else:
    print("Ya existe el directorio")

#Eliminar carpeta
#os.rmdir("./14-sistema-archivos/mi_carpeta")

#Listar contenido de carpeta
print("Contenido de mi carpeta: ")
contenido = os.listdir("./14-sistema-archivos/mi_carpeta")
print(contenido)