"""
Crear un programa que tenga : 
-ventana
-tamaño fijo
-no redimensionable
-un menu (inicio, añadir, informacion)
-distintas pantallas
-formulario añadir productos
-guardar datos temporalmente.
-mostrar datos listados en home
-poner tamaño minimo
-treview
-opcion de salir
"""

import collections
from tkinter import *
from tkinter import ttk

#VENTANA

ventana = Tk()

ventana.title('GESTOR DE PRODUCTOS')
#ventana.geometry('800x400')
ventana.minsize(500, 500)
ventana.config(
    bd= 70
)

ventana.resizable(0,0)

#FUNCIONES

def home():
    homeLabel.config(
        font=('arial', 30),
        fg='white',
        bg='black',
        padx=200,
        pady=5,
        anchor=CENTER
    )
    homeLabel.grid(row=0, column=0, columnspan=2)

    listaProductos.grid(row=1, column= 0)

    for product in productos: 
        if len(product) > 1 :
            listaProductos.insert('', 0, text=product[0], values= (
                product[1], product[2],product[3]))

    addLabel.grid_remove()
    formulario.grid_remove()
    infoLabel.grid_remove()
    creado.grid_remove()
    proyecto.grid_remove()

def add():
    addLabel.config(
        font=('arial', 30),
        fg='white',
        bg='black',
        padx=90,
        pady=5,
    )
    
    addLabel.grid(row=0, column=0)

    formulario.grid(row=1)
    nombre.grid(row=1, column=0, sticky=W, padx=2, pady=5 )
    nombretexto.grid(row=1, column=1, columnspan =1, padx=2, pady=5)
    nombretexto.config(justify='left') 

    descripcion.grid(row=2, column=0, sticky=W, padx=2, pady=5 )
    descripciontexto.grid(row=2, column=1, columnspan =1, padx=2, pady=5)
    descripciontexto.config(justify='left') 

    precio.grid(row=3, column=0, sticky=W, padx=2, pady=5 )
    preciotexto.grid(row=3, column=1, columnspan =1, padx=2, pady=5)
    preciotexto.config(justify='left')

    cant.grid(row=4, column=0, sticky=W, padx=2, pady=5 )
    canttexto.grid(row=4, column=1, columnspan =1, padx=2, pady=5)
    canttexto.config(justify='left')  

    boton.grid(row=5, column=1, sticky=W)
    boton.config(
    fg='white',
    bg='green'
)
    
    homeLabel.grid_remove()
    listaProductos.grid_remove()
    infoLabel.grid_remove()
    creado.grid_remove()
    proyecto.grid_remove()

def info():
    infoLabel.config(
        font=('arial', 30),
        fg='white',
        bg='black',
        padx=100,
        pady=5
    )

    infoLabel.grid(row=0, column=1)
    creado.grid(row=1, column=1)
    proyecto.grid(row=2, column=1)
 
    homeLabel.grid_remove()
    listaProductos.grid_remove()
    formulario.grid_remove()
    addLabel.grid_remove()

def guardarInfo():
    productos.append([
        nombreData.get(),
        descripcionData.get(),
        precioData.get(),
        cantData.get(),
    ])

    nombreData.set('')
    descripcionData.set('')
    precioData.set('')
    cantData.set('')

    home()

#ocultar otras pantallas
#para esto debo dejar mis campos afuera de mis funciones para poder acceder a las variables

homeLabel = Label(ventana, text='INICIO')
addLabel = Label(ventana, text='AÑADIR PRODUCTOS')
infoLabel = Label(ventana, text='INFORMACION')
creado = Label(ventana, text='creado por valentina carrillo')
proyecto = Label(ventana, text='proyecto de practica')

#VARIABLES FORMULARIO
nombreData = StringVar()
descripcionData = StringVar()
precioData = IntVar()
cantData = IntVar()
productos = []
#Formulario campos

formulario = Frame(ventana)

label = Label(formulario, text='INGRESA LOS SIGUIENTES DATOS')

nombre = Label(formulario, text='NOMBRE PRODUCTO')
nombretexto = Entry(formulario, textvariable= nombreData)

descripcion = Label(formulario, text='DESCRIPCION')
descripciontexto = Entry(formulario, textvariable= descripcionData)

precio = Label(formulario, text='PRECIO')
preciotexto = Entry(formulario, textvariable= precioData)

cant = Label(formulario, text='CANTIDAD DE UNIDADES DISPONIBLE')
canttexto = Entry(formulario, textvariable= cantData)

boton = Button(formulario, text='enviar', command=guardarInfo)

#frame lista productos

listaProductos  = ttk.Treeview(height=12, columns=('#1','#2', '#3', '#4'))
listaProductos.grid(row=2, column=0, columnspan=2)
listaProductos.heading('#0', text='producto', anchor=W)
listaProductos.heading('#1', text='descripcion', anchor=W)
listaProductos.heading('#2', text='precio', anchor=W)
listaProductos.heading('#3', text='cantidad', anchor=W)

#MENU

miMenu = Menu(ventana) 

miMenu.add_command(label='Inicio',command=home)
miMenu.add_command(label='Añadir productos',command=add)
miMenu.add_command(label='Informacion',command=info)
miMenu.add_command(label='Salir', command=ventana.quit)

ventana.config(menu = miMenu)

home()



ventana.mainloop()