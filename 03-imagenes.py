from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

#cargar una imagen dentro de la ventana, para esto usaremos un modulo llamado pillow
#para eso ejecutaremos pip install --upgrade pillow



Label(ventana, text='hola, esto es una imagen').pack()



ventana.mainloop() 