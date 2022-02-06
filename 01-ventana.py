#tkinter
#modulo para crear interfaces graficas de usuario

from tkinter import * 
import os.path 

#crear la ventana raiz

ventana = Tk()

#cambio del tamaño de la ventana
ventana.geometry('750x750')

#bloquear tamaño ventana

ventana.resizable(1,0) #los dos argumentos son ancho y alto


#ponerle imagen a la ventana(logotipo), debe ser en .ico

ventana.iconbitmap('./imagenes/piton.ico')

#ponerle titulo a la ventana

ventana.title('app de tkinker')

#comprobar ruta absoluta

ruta = os.path.abspath('./imagenes/piton.ico')

#mostrar texto en el programa
texto = Label(ventana, text=ruta)
texto.pack()

#arrancaar y mostrar la ventana hasta que yo decida cerrarla
#este metodo debe ser el ultimo 

ventana.mainloop() 