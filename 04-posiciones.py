from ctypes import sizeof
from telnetlib import EC
from tkinter import *

ventana = Tk()
#ventana.geometry('500x500')

texto1 = Label(ventana, text = 'bienvenido a mi programa')

texto1.config(
    fg ='white',
    bg ='red',
    padx = 20,
    pady = 20,
    font = ('Arial', 30),
    cursor = 'spider' 
)

texto1.pack(side=TOP)

def pruebas(nombre, apellidos):
    return f'hola {nombre}{apellidos}'

nuevoTexto = Label(ventana, text=pruebas(apellidos='carrillo',nombre='vale'))
nuevoTexto.config(
    fg ='black',
    bg ='green',
    padx = 20,
    pady = 20,
    font = ('Arial', 10),
    cursor = 'spider'
)

nuevoTexto.pack(side=TOP, fill =X, expand=YES)



texto = Label(ventana, text = 'soy vale, sigueme para mas contenido')
texto.config(
    fg ='black',
    bg ='blue',
    padx = 20,
    pady = 20,
    font = ('Arial', 10),
    cursor = 'spider'
)

texto.pack(anchor=W)

ventana.mainloop()

#practica con elementos de pack side, fill , expand, otros