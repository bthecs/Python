from tkinter import *
from PIL import Image, ImageTk


ventana = Tk()
ventana.geometry("1280x720")

imagen = Image.open('./21-tkinter/imagenes/brave-og.png')
render = ImageTk.PhotoImage(imagen)

Label(ventana, image=render).pack(anchor=CENTER)



ventana.mainloop()