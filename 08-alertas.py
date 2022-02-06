from email import message
from tkinter import *
from tkinter import messagebox  as MessageBox
ventana = Tk()

ventana.title('trabajando con alertas')

ventana.config(
    bd= 70
)

def MostrarAlertaError():
    MessageBox.showerror('alerta , ha ocurrido un error')


Button(ventana, text='mostrar alerta', command=MostrarAlertaError).pack(anchor=NW)

def MostrarAlertaSalir():
   resultado = MessageBox.askquestion('seguro que quieres salir ?')
   if resultado != 'yes' :
       ventana.destroy()


Button(ventana, text='salir', command=MostrarAlertaSalir).pack(anchor=NW)

def MostrarAlertainfo():
    MessageBox.showinfo('esto es una alerta')


Button(ventana, text='mostrar info', command=MostrarAlertainfo).pack(anchor=NW)

ventana.mainloop()