from tkinter import *


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculatorinhaa")

        # Pantalla
        self.screen = Text(master, state='disabled', width=30, height=3, background="yellow", foreground="blue")

        # Ubicar la pantalla
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # Variable para almacenar el número actual
        self.equation = ''

        # Botones numericos
        button1 = self.createButton(7)
        button2 = self.createButton(8)
        button3 = self.createButton(9)
        button4 = self.createButton(u"\u232B", None)
        button5 = self.createButton(4)
        button6 = self.createButton(5)
        button7 = self.createButton(6)
        button8 = self.createButton(u"\u00F7")
        button9 = self.createButton(1)
        button10 = self.createButton(2)
        button11 = self.createButton(3)
        button12 = self.createButton('*')
        button13 = self.createButton('.')
        button14 = self.createButton(0)
        button15 = self.createButton('+')
        button16 = self.createButton('-')

        # Botón =
        button17 = Button(master, text='=', width=5, height=2, bg="yellow", command=lambda: self.calculate())
        button17.grid(row=5, column=2)

        # Limpiar pantalla
        button18 = Button(master, text='AC', width=5, height=2, bg="red", command=lambda: self.clear())
        button18.grid(row=5, column=1)

        # Agregar botones a la ventana
        buttons = [button1, button2, button3, button4, button5, button6, button7, button8, button9, button10, button11,
                   button12, button13, button14, button15, button16]
        count = 0
        for row in range(1, 5):
            for col in range(4):
                buttons[count].grid(row=row, column=col)
                count += 1

        # Ubicar el 0
        button14.grid(row=5, column=0)

    # Funcion para crear botones
    def createButton(self, val, write=True, width=7, height=2):
        return Button(self.master, text=val, command=lambda: self.click(val, write), width=width, height=height)

    # Funcion para escribir el contenido de los botones
    def click(self, text, write):
        if write == None:
            # Eliminar ultimo caracter
            self.equation = self.equation[:-1]
        else:
            # Agregar texto al final de la pantalla
            self.equation += str(text)
        self.updateScreen()

    # Funcion para borrar el contenido de la pantalla
    def clear(self):
        self.equation = ''
        self.updateScreen()

    # Funcion de actualización de la pantalla
    def updateScreen(self):
        # Habilitar la pantalla para editar su contenido
        self.screen.configure(state='normal')
        # Borrar todo el contenido de la pantalla
        self.screen.delete('1.0', END)
        # Insertar contenido nuevo en la pantalla
        self.screen.insert(END, self.equation)
        # Deshabilitar la pantalla para que no pueda ser editada
        self.screen.configure(state='disabled')

    # Funcion para calcular el resultado
    def calculate(self):
        # Tomar la ecuacion actualmente en pantalla
        equation = self.equation
        try:
            # Calcular el resultado utilizando la funcion eval()
            result = str(eval(equation))
            # Actualizar la pantalla con el resultado
            self.clear()
            self.equation = result
            self.updateScreen()
        except:
            # Si hay un error al calcular, borrar la pantalla y mostrar el mensaje de error
            self.clear()
            self.equation = "Error"
            self.updateScreen()


# Crear la ventana principal
root = Tk()

# Crear la calculadora
my_gui = Calculator(root)

# Mostrar la ventana principal
root.mainloop()