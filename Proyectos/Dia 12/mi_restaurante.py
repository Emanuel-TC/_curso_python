from tkinter import *

''' Este programa realizará la gestión de un restaurante usando la librería tkinter'''


# iniciar tkinter
aplicacion = Tk()

# tamaño de la ventana
aplicacion.geometry('1200x630+0+0')

# evitar que la ventana se redimensione
aplicacion.resizable(False, False)

# título de la ventana
aplicacion.title('Mi Restaurante - Sistema de Facturación')

# color de fondo de la ventana
aplicacion.config(bg='light blue')

# evitar que la ventana se cierre
aplicacion.mainloop()