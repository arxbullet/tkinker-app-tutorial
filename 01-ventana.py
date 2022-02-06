#tkinter
#modulo para crear interfaces graficas de usuario

from tkinter import * 
import os.path 

#crear clase para el programa(molde para crear distintas ventanas y paginas)

class Programa:

    def __init__(self ):
        self.title = 'app de tinker'
        self.icon = './imagenes/piton.ico'
        self.size = '700x500'
        self.resiable = False
        
    def cargar (self):

        #crear la ventana raiz

        ventana = Tk()

        #cambio del tamaño de la ventana
        ventana.geometry(self.size)

        #bloquear tamaño ventana
        
        if self.resiable : 
            ventana.resizable(1,1) #los dos argumentos son ancho y alto

        else: 
            ventana.resizable(0,0)

        #ponerle imagen a la ventana(logotipo), debe ser en .ico

        ventana.iconbitmap(self.icon)

        #ponerle titulo a la ventana

        ventana.title(self.title)

        #comprobar ruta absoluta

        ruta = os.path.abspath('./imagenes/piton.ico')

        #mostrar texto en el programa
        texto = Label(ventana, text=ruta)
        texto.pack()

        #arrancaar y mostrar la ventana hasta que yo decida cerrarla
        #este metodo debe ser el ultimo 

        ventana.mainloop() 

#instanciar mi programa

programa = Programa()
programa.cargar()