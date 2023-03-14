'''
Turnero para dar turnos:
-Perfumeria
-Farmacia
-Cosmética
'''

import numeros
areas = ['Perfumeria', 'Farmacia', 'Cosmética']
def preguntar():

    print("Hola, bienvenido a Farmacia Python, ¿a qué área vas a pasar?")
    while True:
        try:
            opcion = input("[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmética\n").upper()
            # Verifica que el usuario ingrese una opcion valida, regresa value error si la opcion ingresa no está
            ['P', 'F', 'C'].index(opcion)

        except ValueError:
            print("Opción no válida")
        else:
            break
    numeros.saludo_y_adios(opcion)


def iniciar():
    while True:
        preguntar()
        try:
            respuesta = input("¿Desea continuar? [S/N] ").upper()
            ['S', 'N'].index(respuesta)
        except ValueError:
            print("Opción no válida")
        else:
            if respuesta == 'N':
                print("Gracias por usar Farmacia Python")
                break


iniciar()



