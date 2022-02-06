from tkinter import *
from tkinter import messagebox  as MessageBox
ventana = Tk()

ventana.title('trabajando con alertas')

ventana.config(
    bd= 70
)

def MostrarAlertaError():
    MessageBox.showerror('error','alerta , ha ocurrido un error')


Button(ventana, text='mostrar alerta', command=MostrarAlertaError).pack(anchor=NW)

def MostrarAlertaSalir():
   resultado = MessageBox.askquestion('espera ', 'seguro que quieres salir ?')
   if resultado != 'yes' :
       ventana.destroy()


Button(ventana, text='salir ahora', command=MostrarAlertaSalir).pack(anchor=NW)

def MostrarAlertainfo():
    MessageBox.showinfo('esto es una alerta', 'alerta')


Button(ventana, text='mostrar info', command=MostrarAlertainfo).pack(anchor=NW)

def Salir(nombre):
   resultado = MessageBox.askquestion('seguro que quieres salir ?', 'espera un segundo')
   if resultado != 'yes' :
       MessageBox.showinfo('Chao', f'nos vemos {nombre}')
       ventana.destroy()


Button(ventana, text='salir', command=lambda:Salir('vale')).pack(anchor=NW)

ventana.mainloop()