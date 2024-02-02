"""
En este módulo tendremos los generadores y decoradores para el programa principal
"""

def turno(opcion, contador):
    while True:
        if opcion == "c":
            yield f"\tC-{contador['c']}\n"
        elif opcion == "f":
            yield f"\tF-{contador['f']}\n"
        elif opcion == "p":
            yield f"\tP-{contador['p']}\n"

def indicar_turno(opcion,contadores):
    print("Su turno es:\n")
    print(next(turno(opcion, contadores)))
    print("Aguarde y será atendido")


