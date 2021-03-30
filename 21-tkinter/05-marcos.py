from tkinter import *

ventana = Tk()
ventana.title("Marcos Tk")
ventana.geometry("700x400")

marco_padre = Frame(ventana, width=250, height=250)
marco_padre.config(
    bg="green",
    bd=12,
    relief="groove"
)
marco_padre.pack(side=TOP, fill=X, expand=YES)

marco = Frame(marco_padre, width=50, height=50)
marco.config(
    bg="orange",
    bd=12,
    relief="sunken"
)
marco.pack(side=LEFT, fill=X, expand=YES)
marco.pack_propagate(False)

texto = Label(marco, text="Primer marco")
texto.config(
    bg = "red",
    fg = "white",
    font = ("Arial", 20),
    height = 10,
    width = 10,
    bd=3,
    relief=SOLID,
    anchor=CENTER
)
texto.pack()



ventana.mainloop()