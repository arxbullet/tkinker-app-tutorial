#calculadora tkinker con clases 
from tkinter import *
from tkinter import messagebox  as MessageBox

class Calculadora:

    def __init__(self, alertas) :

        self.numero1 = StringVar()
        self.numero2 =StringVar()
        self.resultado =StringVar()
        self.alertas = alertas

    def cFloat(self, numero):
        try:
            result = float(numero)
        
        except:
            result = 0
            MessageBox.showerror('Error de tipo', 'porfavor ingresa un valor valido')

        return result

    def mostrarResultado(self):
        self.alertas.showinfo('resultado', f'el resultado de la operacion es {self.resultado.get()}')
        #self.numero1 = ''
        #self.numero2 = ''

    def Sumar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) + self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def Restar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) - self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def Multiplicar(self):
        self.resultado.set(self.cFloat(self.numero1.get()) * self.cFloat(self.numero2.get()))
        self.mostrarResultado()

    def Dividir(self):
        self.resultado.set(self.cFloat(self.numero1.get()) / self.cFloat(self.numero2.get()))
        self.mostrarResultado()

ventana = Tk()

ventana.title('trabajando con alertas')

ventana.config(
    bd= 70
)

calculadora = Calculadora (MessageBox)

marco = Frame(ventana, width=340, height=200)
marco.config(
    padx=15, 
    pady=15, 
    bd= 3, 
    relief=SOLID
)

marco.pack(side=TOP, anchor=CENTER)
marco.pack_propagate(False)

Label(marco, text='Ingresa un numero').pack(anchor=CENTER)

Entry(marco, textvariable= calculadora.numero1).pack(anchor=CENTER)

Label(marco, text='Ingresa otro numero').pack(anchor=CENTER)

Entry(marco, textvariable= calculadora.numero2).pack(anchor=CENTER)

Button(marco, text='Sumar', command=calculadora.Sumar).pack(side=LEFT, fill=X, expand=TRUE)
Button(marco, text='Restar', command=calculadora.Restar).pack(side=LEFT, fill=X, expand=TRUE)
Button(marco, text='Dividir', command=calculadora.Dividir).pack(side=LEFT, fill=X, expand=TRUE)
Button(marco, text='Multiplicar', command=calculadora.Multiplicar).pack(side=LEFT, fill=X, expand=TRUE)

ventana.mainloop()


