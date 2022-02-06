from tkinter import *
from turtle import width 
ventana = Tk()

ventana.title('trabajando con formularios')

ventana.geometry('700x700')

#encabezado del form

encabezado= Label(ventana, text='Formulario')
encabezado.config(
    fg='white',
    bg='black',
    font=('Comic Sans', 18),
    padx=5,
    pady=5
)

#campos Y GRID(no puedo usar grid y pack a la vez, solo uno en todo el programa)
label = Label(ventana, text='nombre')
campotexto = Entry(ventana)

encabezado.grid(row=0 , column=0, sticky=W)
label.grid(row=1, column=0, sticky=W, padx=5, pady=5 )
campotexto.grid(row=1, column=1, columnspan =6, padx=5, pady=5)
#otro campo

label = Label(ventana, text='apellido')
campotexto = Entry(ventana)
label.grid(row=2, column=0, sticky=W, padx=5, pady=5 )
campotexto.grid(row=2, column=1, columnspan =6, padx=5, pady=5)
campotexto.config(justify='left', state='disabled') # el justify indica en que lado sale el texto

#campos de texto multilineas

label = Label(ventana, text='comentarios')
campotexto = Text(ventana)
label.grid(row=3, column=0, sticky=NW, padx=5, pady=5 )
campotexto.grid(row=3, column=1, columnspan =6, padx=5, pady=5)
campotexto.config(
    width='30',
    height='30',
)

#botones 
label = Label(ventana)
campotexto = Text(ventana)
label.grid(row=4, column=1, sticky=NW, padx=5, pady=5 )
boton = Button(ventana, text='enviar')
boton.grid(row=4, column=1, sticky=W, )
boton.config(
    fg='white',
    bg='green'
)





ventana.mainloop()

