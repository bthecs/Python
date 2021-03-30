from tkinter import *

ventana = Tk()
#ventana.geometry("500x500")



texto = Label(ventana, text ="Hola Brave")
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
texto.pack(side=TOP, fill=X, expand=YES)

texto = Label(ventana, text ="Hola Brave")
texto.config(
            fg="white",
            bg="orange",
            padx=20,
            pady=20,
            font=("Consolas", 30),
            justify=RIGHT,
            width=50,
            height=5,
            cursor="circle"
)
texto.pack(side=LEFT)


texto = Label(ventana, text ="Hola Brave")
texto.config(
            fg="white",
            bg="green",
            padx=20,
            pady=20,
            font=("Consolas", 30),
            justify=RIGHT,
            width=50,
            height=5,
            cursor="circle"
)
texto.pack(side=RIGHT)


ventana.mainloop()