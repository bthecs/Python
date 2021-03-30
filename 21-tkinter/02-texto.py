from tkinter import *

ventana = Tk()
ventana.geometry("500x500")


def pruebas(nombre, apellidos, pais):
    return f"Hola {nombre} {apellidos} veo que eres de {pais}"

texto = Label(ventana, text =pruebas("Lautaro", "Gimenez","Argentina"))
texto.config(
            fg="white",
            bg="black",
            padx=20,
            pady=20,
            font=("Consolas", 30),
            justify=RIGHT,
            width=50,
            height=5,
            cursor="circle"
)
texto.pack()




ventana.mainloop()