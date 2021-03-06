from tkinter import * 
ventana = Tk()

ventana.title('trabajando con marcos')

ventana.geometry('700x700')

marco = Frame(ventana, width=250, height=250) # le indico donde cargar el marco y sus dimensiones

marco.config(
    bg= 'red',
    bd=12,
    relief='solid'
)

marco.pack(side=BOTTOM) # O PUEDO USAR ANCHOR

marco2 = Frame(ventana, width=250, height=250)
marco2.config(
    bg= 'green',
    bd=12,
    relief='solid'
)

marco2.pack(side=BOTTOM, anchor=SE)

#cargar marco dentro de otro 

marcoPadre = Frame(ventana, width=250, height=250)
marcoPadre.config(
    bg= 'lightblue',
    bd=12,
)

marcoPadre.pack(side=TOP, anchor=CENTER)

marcoHijo = Frame(marcoPadre, width=150, height=150)#cargo el marco hijo en el marco padre
marcoHijo .config(
    bg= 'blue',
    bd=12,
    relief='solid'
)

#poner texto en el centro con heigh y width
marcoChiquito = Label(marcoHijo, text='marco chiquito')
marcoChiquito.config(
    bg= 'blue',
    bd=1,
    font = ('Arial', 10),
    fg='white',
    height=10,
    width=10,
)
marcoChiquito.pack(anchor=CENTER)
marcoHijo.pack(side=TOP, anchor=CENTER)
marcoHijo.pack_propagate(False)

ventana.mainloop()