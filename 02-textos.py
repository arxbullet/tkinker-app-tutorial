from tkinter import *

ventana = Tk()
ventana.geometry('500x500')

texto = Label(ventana, text = 'bienvenido a mi programa')

#keyword arguments 

def pruebas(nombre, apellidos):
    return f'hola {nombre}{apellidos}'

nuevoTexto = Label(ventana, text=pruebas(apellidos='carrillo',nombre='vale'))
#aca lo importante o los keyword aguments son apellido y nombre, y al pasarlos 
#con el nombre del parametro, da lo mismo el orden.

nuevoTexto.pack()

#pasar colores y otras configuraciones de estilo
texto.config(
    fg ='white',
    bg ='#000000',
    padx = 20,
    pady = 20,
    font = ('Arial', 30),
    cursor = 'spider'
)

#para mostrarlo debo empaquetarlo y ejecutarlo 
texto.pack()

texto = Label(ventana, text = 'soy vale, sigueme para mas contenido')
texto.pack(anchor=CENTER)#el movimiento del texto se lo tenemos que indicar dentro de pack


ventana.mainloop()
