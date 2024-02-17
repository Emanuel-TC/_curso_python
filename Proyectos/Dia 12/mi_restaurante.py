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

# Creaciónn de panel superior
panel_superior = Frame(aplicacion, bg='RoyalBlue3', bd=1, relief=SUNKEN) # bd: grosor del borde, relief: tipo de borde
# ubicación del panel
panel_superior.pack(side=TOP)

# Etiqueta de título para el panel superior
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='snow',
                        font=('Arial', 58, 'bold'), bg='steel blue', width=27) # fg: color de la letra, font: fuente{Arial}, tamaño{58}, negrita{bold}; bg: color de fondo, width: ancho
etiqueta_titulo.grid(row=0, column=0) # ubicación de la etiqueta, fila 0, columna 0

# Creación de panel izquierdo
panel_izquierdo = Frame(aplicacion, bg='RoyalBlue3', bd=1, relief=SUNKEN)
panel_izquierdo.pack(side=LEFT)

# Panel de costos, se ubica hasta abajo del panel izquierdo
panel_costos = Frame(panel_izquierdo, bg='RoyalBlue3', bd=1, relief=SUNKEN)
panel_costos.pack(side=BOTTOM)

# Panel de comidas, se ubica arriba del panel de costos, y a la izquierda del panel izquierdo
panel_comidas = LabelFrame(panel_izquierdo, text='Comida', bg='salmon1', bd=1, relief=SUNKEN,
                           font=('Arial', 19, 'bold'), fg='RoyalBlue3')
panel_comidas.pack(side=LEFT)
# Panel de bebidas, se ubica arriba del panel de costos, y aL centro del panel izquierdo
panel_bebidas = LabelFrame(panel_izquierdo, text='Bebidas', bg='DeepSkyBlue3', bd=1, relief=SUNKEN,
                            font=('Arial', 19, 'bold'), fg='snow')
panel_bebidas.pack(side=LEFT)
# Panel de postres, se ubica arriba del panel de costos, y a la derecha del panel izquierdo
panel_postres = LabelFrame(panel_izquierdo, text='Postres', bg='PaleVioletRed1', bd=1, relief=SUNKEN,
                            font=('Arial', 19, 'bold'), fg='midnight blue')
panel_postres.pack(side=LEFT)

# Creación de panel derecho
panel_derecho = Frame(aplicacion, bg='RoyalBlue3', bd=1, relief=SUNKEN)
panel_derecho.pack(side=RIGHT)

# panel calculadora, se ubica hasta arriba del panel derecho
panel_calculadora = Frame(panel_derecho, bg='RoyalBlue3', bd=1, relief=SUNKEN)
panel_calculadora.pack() # por defecto se ubica arriba

# panel de recibos, se ubica hasta en medio del panel derecho
panel_recibos = Frame(panel_derecho, bg='RoyalBlue3', bd=1, relief=SUNKEN)
panel_recibos.pack()

# panel de botones, se ubica hasta abajo del panel derecho
panel_botones = Frame(panel_derecho, bg='RoyalBlue3', bd=1, relief=SUNKEN)
panel_botones.pack()


# evitar que la ventana se cierre
aplicacion.mainloop()