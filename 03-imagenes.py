from email.mime import image
from tkinter import *
from PIL import Image, ImageTk

ventana = Tk()
ventana.geometry('500x500')

#cargar una imagen dentro de la ventana, para esto usaremos un modulo llamado pillow
#para eso ejecutaremos py -m pip install --upgrade pillow

Label(ventana, text='hola, esto es una imagen').pack()

imagen = Image.open('./imagenes/piton.ico')

render = ImageTk.PhotoImage(imagen)

Label(ventana, image = render).pack() #renderizar imagen en un label dentro de la ventana

ventana.mainloop() 