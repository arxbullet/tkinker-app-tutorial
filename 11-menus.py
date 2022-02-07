from cProfile import label
from tkinter import *
from tkinter import messagebox  as MessageBox

ventana = Tk()

ventana.title('formularios 2')
ventana.geometry('300x120')
ventana.config(
    bd= 70
)

miMenu = Menu(ventana) 
ventana.config(menu = miMenu)

#crear sub menu 

archivo=Menu(miMenu, tearoff= 0)
archivo.add_command(label = 'nuevo')
archivo.add_separator
archivo.add_command(label='abrir archivo')

#vincular con cascade
miMenu.add_cascade(label='archivo', menu = archivo)
miMenu.add_command(label='editar')
miMenu.add_command(label='seleccion')

ventana.mainloop()