from tkinter import *
ventana = Tk()

ventana.title('trabajando con formularios')

ventana.geometry('700x700')

ventana.config(
    bg='grey',
)
def getDato():
    resultado.set(dato.get())

    if len(resultado.get()) >=1 :
        texto_recogido.config(
            bg='green',
            fg='white'  
            )

dato = StringVar() #variable para recojer lo que dice el text
resultado = StringVar()

label = Label(ventana, text='pon tu comentario').pack(anchor=NW)

campo = Entry(ventana, textvariable= dato).pack(anchor=NW) #le indicamos que se guardara el texto en dato

Label(ventana, text='Dato recogido:').pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.config(
    bg='grey',
    fg='white'
)
texto_recogido.pack()

Button(ventana, text='mostrar dato', command=getDato).pack(anchor=NW) #le paso con comand la funcion a ejecutar con el click

ventana.mainloop()