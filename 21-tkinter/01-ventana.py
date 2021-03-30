# Tkinter
# Modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path


class Programa:

    def __init__(self):
        self.titulo = "Gianca puto"
        self.icono = "./imagenes/descarga.ico"
        self.ico_alt = "./21-tkinter/imagenes/descarga.ico"
        self.size = "770x470"
        self.resizable = FALSE

    def cargar(self):
        #Crear la ventana raiz
        ventana = Tk()
        self.ventana = ventana

        #Titulo de la ventana
        ventana.title(self.titulo)

        # Comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.icono)

        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.ico_alt)

        # Icono de la ventana
        ventana.iconbitmap(ruta_icono)

        #Mostrar texto en el programa
        texto = Label(ventana, text=ruta_icono)
        texto.pack()

        #Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        #Bloquear el tamaño de la ventana
        if self.resizable:
            ventana.resizable(1, 1)
        else:
            ventana.resizable(0, 0)

        #Arrancar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()

    def addText(self, dato):
        texto = Label(self.ventana, text = dato)
        texto.pack()

    def mostrar(self):
        self.ventana.mainloop()

programa = Programa()
programa.cargar()
programa.addText("Hola soy un texto")
programa.mostrar()