from tkinter import *
from tkinter import messagebox  as MessageBox

ventana = Tk()

ventana.title('formularios 2')
ventana.geometry('1200x800')
ventana.config(
    bd= 70
)

#VARIABLES

web=IntVar()
mobile=IntVar()
opcion = StringVar()
opcion.set(None)
opcionMenu = StringVar()
opcionMenu.set(None)

#FUNCIONES

def MostrarProfesion():
    texto = ''

    if web.get():
     texto += 'desarrollo web'
     
    if mobile.get():
        if web.get():
            texto += 'desarrollo web y movil'
        else :
            texto += 'desarrollo mobile'

    mostrar.config(
        text=texto,
        bg='pink'
    )

def Marcar():
    marcado.config(text=opcion.get())

def Seleccionar():
    seleccionado.config(text=opcionMenu.get())

encabezado = Label(ventana, text='TITULOS, CHECKBOX, RADIOBUTTONS Y OTROS')
encabezado.config(
    padx=15, 
    pady=15, 
    fg='white',
    bg='pink',
    font=('Consolas', 20)
)
encabezado.grid(row=0, column=0, columnspan=5, sticky=W)

#checkbox

Label(ventana, text='A que te dedicas?').grid(row=1, column=0)
Checkbutton(
    ventana, 
    text='desarrollo web', 
    variable=web, 
    onvalue=1, 
    command = MostrarProfesion,
    offvalue=0).grid(row=1, column=1)
Checkbutton(
    ventana, 
    text='desarrollo movil', 
    variable=mobile, 
    onvalue=1, 
    command = MostrarProfesion,
    offvalue=0).grid(row=1, column=2)

mostrar = Label(ventana)
mostrar.grid(row=1, column=4)

#radio buttons

Label(ventana, text='cual es tu sexo').grid(row=2, column=0)
Radiobutton(
    ventana, 
    text='femenino', 
    variable=opcion,
    value='femenino',
    command = Marcar).grid(row=2, column=1)
Radiobutton(
    ventana, 
    text='Masculino', 
    variable=opcion,
    value='m',
    command = Marcar).grid(row=2, column=2)

marcado = Label(ventana)
marcado.grid(row=2, column=4)

#Option Menu
Label(ventana, text='escoje una opcion').grid(row=3, column=0)
select = OptionMenu(ventana, opcionMenu, 'opcion 1', 'opcion 2', 'opcion 3' )
select.grid(row=3, column=1)
seleccionado = Label(ventana)
seleccionado.grid(row=3, column=3)
Button(ventana, text='ver',command=Seleccionar).grid(row=3, column=2)
ventana.mainloop()


