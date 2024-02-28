from tkinter import *

''' Este programa realizará la gestión de un restaurante usando la librería tkinter'''

operador = ''

def clic_boton(numero):
    global operador
    operador = operador + numero
    visor_calculadora.delete(0,END)
    visor_calculadora.insert(END,operador)

def borrar():
    global operador
    operador = ''
    visor_calculadora.delete(0,END)

def obtener_resultado():
    global operador
    resultado = str(eval(operador))
    visor_calculadora.delete(0, END)
    visor_calculadora.insert(0,resultado)
    operador = ''

def revisar_check():
    x = 0
    for c in cuadros_comida:
        if variables_comida[x].get() == 1:
            cuadros_comida[x].config(state=NORMAL)
            if cuadros_comida[x].get() == '0':
                cuadros_comida[x].delete(0,END)
            cuadros_comida[x].focus()
        else:
            cuadros_comida[x].config(state=DISABLED)
            texto_comida[x].set('0')
        x += 1
    x = 0
    for c in cuadros_bebida:
        if variables_bebida[x].get() == 1:
            cuadros_bebida[x].config(state=NORMAL)
            if cuadros_bebida[x].get() == '0':
                cuadros_bebida[x].delete(0,END)
            cuadros_bebida[x].focus()
        else:
            cuadros_bebida[x].config(state=DISABLED)
            texto_bebida[x].set('0')
        x += 1
    x = 0
    for c in cuadros_postres:
        if variables_postre[x].get() == 1:
            cuadros_postres[x].config(state=NORMAL)
            if cuadros_postres[x].get() == '0':
                cuadros_postres[x].delete(0,END)
            cuadros_postres[x].focus()
        else:
            cuadros_postres[x].config(state=DISABLED)
            texto_postres[x].set('0')
        x += 1

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
panel_superior = Frame(aplicacion, bg='RoyalBlue3', bd=1, relief=SUNKEN)  # bd: grosor del borde, relief: tipo de borde
# ubicación del panel
panel_superior.pack(side=TOP)

# Etiqueta de título para el panel superior
etiqueta_titulo = Label(panel_superior, text='Sistema de Facturación', fg='snow',
                        font=('Arial', 58, 'bold'), bg='steel blue',
                        width=27)  # fg: color de la letra, font: fuente{Arial}, tamaño{58}, negrita{bold}; bg: color de fondo, width: ancho
etiqueta_titulo.grid(row=0, column=0)  # ubicación de la etiqueta, fila 0, columna 0

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
panel_calculadora = Frame(panel_derecho, bg='snow', bd=1, relief=SUNKEN)
panel_calculadora.pack()  # por defecto se ubica arriba

# panel de recibos, se ubica hasta en medio del panel derecho
panel_recibos = Frame(panel_derecho, bg='RoyalBlue3', bd=1, relief=SUNKEN)
panel_recibos.pack()

# panel de botones, se ubica hasta abajo del panel derecho
panel_botones = Frame(panel_derecho, bg='RoyalBlue3', bd=1, relief=SUNKEN)
panel_botones.pack()

# lista de productos
lista_comidas = ["pollo", "cordero", "salmón", "merluza", "kebab", "pizza 1", "pizza 2", "pizza 3"]
lista_bebidas = ["agua", "coca", "coca light", "fanta", "sprite", "té", "café", "jugo"]
lista_postres = ["helado", "brownies", "fruta", "yogurt", "flan", "pay", "pastel", "galletas"]

# cargar elementos a los frames de comidas, bebidas, y postres

# generar items comida
variables_comida = []
cuadros_comida = []
texto_comida = []
contador = 0
for comida in lista_comidas:
    # crear chechbutton
    variables_comida.append('')
    variables_comida[contador] = IntVar()
    comida = Checkbutton(panel_comidas,
                         text=comida.title(),
                         bg='salmon1',
                         font=('Arial', 19, 'bold'),
                         fg='blue4',
                         onvalue=1,
                         offvalue=0,
                         variable=variables_comida[contador],
                         command=revisar_check)
    comida.grid(row=contador,
                column=0,
                sticky=W)

    # crear cuadros de entrada
    cuadros_comida.append('')
    texto_comida.append('')
    # valores por defecto
    texto_comida[contador] = StringVar()
    texto_comida[contador].set('0')
    cuadros_comida[contador] = Entry(panel_comidas,
                                     font=('Arial', 19, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_comida[contador])
    cuadros_comida[contador].grid(row=contador,
                                  column=1)

    contador += 1

# generar items bebida
variables_bebida = []
cuadros_bebida = []
texto_bebida = []
contador = 0
for bebida in lista_bebidas:
    # crear checkbutton
    variables_bebida.append('')
    variables_bebida[contador] = IntVar()
    bebida = Checkbutton(panel_bebidas,
                         text=bebida.title(),
                         bg='DeepSkyBlue3',
                         font=('Arial', 19, 'bold'),
                         fg='grey15',
                         onvalue=1,
                         offvalue=0,
                         variable=variables_bebida[contador],
                         command=revisar_check)
    bebida.grid(row=contador,
                column=0,
                sticky=W)
    # crear cuadros de entrada
    cuadros_bebida.append('')
    texto_bebida.append('')
    # valores por defecto
    texto_bebida[contador] = StringVar()
    texto_bebida[contador].set('0')
    cuadros_bebida[contador] = Entry(panel_bebidas,
                                     font=('Arial', 19, 'bold'),
                                     bd=1,
                                     width=6,
                                     state=DISABLED,
                                     textvariable=texto_bebida[contador])
    cuadros_bebida[contador].grid(row=contador,
                                  column=1)
    contador += 1

# generar items postre
variables_postre = []
cuadros_postres = []
texto_postres = []
contador = 0
for postre in lista_postres:
    # checkbutton
    variables_postre.append('')
    variables_postre[contador] = IntVar()
    postre = Checkbutton(panel_postres,
                         text=postre.title(),
                         bg='PaleVioletRed1',
                         font=('Arial', 19, 'bold'),
                         fg='grey15',
                         onvalue=1,
                         offvalue=0,
                         variable=variables_postre[contador],
                         command=revisar_check)
    postre.grid(row=contador,
                column=0,
                sticky=W)
    # crear cuadros de entrada
    cuadros_postres.append('')
    texto_postres.append('')
    # valores por defecto
    texto_postres[contador] = StringVar()
    texto_postres[contador].set('0')
    cuadros_postres[contador] = Entry(panel_postres,
                                      font=('Arial', 19, 'bold'),
                                      bd=1,
                                      width=6,
                                      state=DISABLED,
                                      textvariable=texto_postres[contador])
    cuadros_postres[contador].grid(row=contador,
                                   column=1)
    contador += 1

# variables
var_costo_comida = StringVar()
var_costo_bebida = StringVar()
var_costo_postre = StringVar()
var_subtotal = StringVar()
var_impuesto = StringVar()
var_total = StringVar()

# etiquietas de costo y campos de entrada
# comidas
etiqueta_costo_comida = Label(panel_costos,
                              text='Costo Comida',
                              font=('Arial', 12, 'bold'),
                              bg='RoyalBlue3',
                              fg='white')
# ubicación de etiqueta costo comida
etiqueta_costo_comida.grid(row=0,
                           column=0)
texto_costo_comida = Entry(panel_costos,
                           font=('Arial', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_comida)
# ubicación de etiqueta texto costo comida
texto_costo_comida.grid(row=0,
                        column=1,
                        padx=41)

# etiquietas de costo y campos de entrada
# bebidas
etiqueta_costo_bebida = Label(panel_costos,
                              text='Costo Bebidas',
                              font=('Arial', 12, 'bold'),
                              bg='RoyalBlue3',
                              fg='white')
# ubicación de etiqueta costo bebida
etiqueta_costo_bebida.grid(row=1,
                           column=0)
texto_costo_bebida = Entry(panel_costos,
                           font=('Arial', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_bebida)
# ubicación de etiqueta texto costo bebida
texto_costo_bebida.grid(row=1,
                        column=1,
                        padx=41)
# etiquietas de costo y campos de entrada
# postres
etiqueta_costo_postre = Label(panel_costos,
                              text='Costo Postres',
                              font=('Arial', 12, 'bold'),
                              bg='RoyalBlue3',
                              fg='white')
# ubicación de etiqueta costo postres
etiqueta_costo_postre.grid(row=2,
                           column=0)
texto_costo_postre = Entry(panel_costos,
                           font=('Arial', 12, 'bold'),
                           bd=1,
                           width=10,
                           state='readonly',
                           textvariable=var_costo_postre)
# ubicación de etiqueta texto costo postres
texto_costo_postre.grid(row=2,
                        column=1,
                        padx=41)

# etiquietas de costo y campos de entrada
# subtotal
etiqueta_subtotal = Label(panel_costos,
                          text='Subtotal',
                          font=('Arial', 12, 'bold'),
                          bg='RoyalBlue3',
                          fg='white')
# ubicación de etiqueta subtotal
etiqueta_subtotal.grid(row=0,
                       column=2)
texto_subtotal = Entry(panel_costos,
                       font=('Arial', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_subtotal)
# ubicación de etiqueta texto subtotal
texto_subtotal.grid(row=0,
                    column=3,
                    padx=41)

# etiquietas de costo y campos de entrada
# Impuesto
etiqueta_impuesto = Label(panel_costos,
                          text='Impuestos',
                          font=('Arial', 12, 'bold'),
                          bg='RoyalBlue3',
                          fg='white')
# ubicación de etiqueta costo impuestos
etiqueta_impuesto.grid(row=1,
                       column=2)
texto_impuesto = Entry(panel_costos,
                       font=('Arial', 12, 'bold'),
                       bd=1,
                       width=10,
                       state='readonly',
                       textvariable=var_impuesto)
# ubicación de etiqueta texto impuestos
texto_impuesto.grid(row=1,
                    column=3,
                    padx=41)
# etiquietas de costo y campos de entrada
# total
etiqueta_total = Label(panel_costos,
                       text='Total',
                       font=('Arial', 12, 'bold'),
                       bg='RoyalBlue3',
                       fg='white')
# ubicación de etiqueta costo total
etiqueta_total.grid(row=2,
                    column=2)
texto_total = Entry(panel_costos,
                    font=('Arial', 12, 'bold'),
                    bd=1,
                    width=10,
                    state='readonly',
                    textvariable=var_total)
# ubicación de etiqueta texto costo total
texto_total.grid(row=2,
                 column=3,
                 padx=41)

# botones
botones = ['total','recibo','guardar','reset']
columnas = 0
for boton in botones:
    boton = Button(panel_botones,
                   text=boton.title(),
                   font=('Arial', 14, 'bold'),
                   fg='white',
                   bg='purple3',
                   bd=1,
                   width=9)
    boton.grid(row=0,
               column=columnas)
    columnas += 1

# área de recibo
texto_recibo = Text(panel_recibos,
                    font=('Arial', 12, 'bold'),
                    bd=1,
                    width=42,
                    height=10)
texto_recibo.grid(row=0,
                  column=0)

# calculadora
visor_calculadora = Entry(panel_calculadora,
                          font=('Arial', 16, 'bold'),
                          bd=1,
                          width=32)
visor_calculadora.grid(row=0,
                       column=0,
                       columnspan=4)
botones_calculadora = ["7","8","9","+","4","5","6","-","1","2","3","x","CE","Borrar","0","/"]
botones_guardados = []

fila = 1
columna = 0
for boton in botones_calculadora:
    boton = Button(panel_calculadora,
                   text=boton.title(),
                   font=('Arial', 16, 'bold'),
                   fg='white',
                   bg='purple3',
                   bd=1,
                   width=8)

    botones_guardados.append(boton)
    boton.grid(row=fila,
               column=columna)
    if columna == 3:
        fila += 1
    columna += 1
    if columna == 4:
        columna = 0

botones_guardados[0].config(command=lambda : clic_boton('7'))
botones_guardados[1].config(command=lambda : clic_boton('8'))
botones_guardados[2].config(command=lambda : clic_boton('9'))
botones_guardados[3].config(command=lambda : clic_boton('+'))
botones_guardados[4].config(command=lambda : clic_boton('4'))
botones_guardados[5].config(command=lambda : clic_boton('5'))
botones_guardados[6].config(command=lambda : clic_boton('6'))
botones_guardados[7].config(command=lambda : clic_boton('-'))
botones_guardados[8].config(command=lambda : clic_boton('1'))
botones_guardados[9].config(command=lambda : clic_boton('2'))
botones_guardados[10].config(command=lambda : clic_boton('3'))
botones_guardados[11].config(command=lambda : clic_boton('*'))
botones_guardados[12].config(command= obtener_resultado)
botones_guardados[13].config(command= borrar)
botones_guardados[14].config(command=lambda : clic_boton('0'))
botones_guardados[15].config(command=lambda : clic_boton('/'))

# evitar que la ventana se cierre
aplicacion.mainloop()
