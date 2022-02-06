from distutils import command
from tkinter import *
from tkinter import messagebox  as MessageBox

ventana = Tk()

ventana.title('formularios 2')
ventana.geometry('1200x800')
ventana.config(
    bd= 70
)

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

"""marco = Frame(ventana, width=340, height=200)
marco.config(
    padx=15, 
    pady=15, 
    bd= 3, 
    relief=SOLID
)

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)"""

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

web=IntVar()
mobile=IntVar()

Label(ventana, text='A que te dedicas?').grid(row=1, column=0)
Checkbutton(
    ventana, 
    text='desarrollo web', 
    variable=web, 
    onvalue=1, 
    offvalue=0).grid(row=1, column=1)
Checkbutton(
    ventana, 
    text='desarrollo movil', 
    variable=mobile, 
    onvalue=1, 
    offvalue=0).grid(row=1, column=2)

mostrar = Label(ventana, command=MostrarProfesion)
mostrar.grid(row=2, column=0)

#radio buttons
opcion = IntVar()
opcion.set(None)
Label(ventana, text='cual es tu sexo').grid(row=2, column=0)
Radiobutton(
    ventana, 
    text='femenino', 
    variable=opcion,
    value='femenino',
    command=Marcar).grid(row=2, column=1)
Radiobutton(
    ventana, 
    text='Masculino', 
    variable=opcion,
    value='m',
    command=Marcar).grid(row=2, column=2)

marcado = Label(ventana)
marcado.grid(row=3, column=0)

ventana.mainloop()