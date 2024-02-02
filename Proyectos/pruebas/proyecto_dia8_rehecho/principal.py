"""
Este es un programa para brindar turnos a las personas que requieran el acceso a algún área de la farmacia
"""
from numeros import *

def saludar():
    """Esta función será la encargada de saludar al cliente e informarles del funcionamiento del sistema"""
    print("""Hola, bienvenido(a)\n
          ¿A qué área te vas a dirigir?
          Las áreas son las siguientes:
          \tC) Cosmética
          \tF) Farmacia
          \tP) Perfumería
          """)
contadores = {'c': 0, 'f': 0, 'p': 0}
while True:
    saludar()
    opcion = input("Ingresa la opción para la que deseas sacar turno (C/F/P):\n").lower()
    try:
        if opcion not in ["c", "f", "p"]:
            print("Ingresa una de las opciones mencionadas previamente:")
        else:
            indicar_turno(opcion, contadores)
            contadores[opcion] += 1
    except ValueError:
        print("No estás ingresando una opción válida")




