from io import open
import pathlib
import shutil
import os


"""
#abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivo = open(ruta, "a+")

#Escribir dentro de un archivo
archivo.write("*******Soy un texto metido desde python********\n")

#cerrar archivo
archivo.close()

#abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

#Leer contenido
#contenido = archivo_lectura.read()

#print(contenido)

#Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elementos in lista:
    print(elementos)

#Copiar archivo
ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado.txt"
shutil.copyfile(ruta_original, ruta_nueva)

#Mover archivo
ruta_original = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_copiado.txt"
ruta_nuevo = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto_nuevo.txt"
shutil.move(ruta_original,ruta_nuevo)


#eliminar archivos
ruta_nuevo = str(pathlib.Path().absolute()) + "/14-sistema-archivos/fichero_texto_nuevo.txt"
os.remove(ruta_nuevo)
"""
#Comprobar si existe
import os.path

#print(os.path.abspath("../"))

comprobar = os.path.abspath("./") + "/14-sistema-archivos/fichero_texto.txt"
print(comprobar)

if os.path.isfile(comprobar):
    print("El archivo existe")
else:
    print("El archivo no existe")
