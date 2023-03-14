# #Contador de numeros para cada área
# #Decorador de funciones con selección mediante if-else

def contador_perfumeria():
    numero = 1
    while True:
        yield f"P-{numero}"
        numero += 1


def contador_farmacia():
    turno = 1
    while True:
        yield f"F-{turno}"
        turno += 1


def contador_cosmetica():
    turno = 1
    while True:
        yield f"C-{turno}"
        turno += 1


generador_perfumeria = contador_perfumeria()
generador_farmacia = contador_farmacia()
genenerador_cosmetica = contador_cosmetica()


def saludo_y_adios(opcion):
    print("\n" + "*"*23)
    print("Hola, su turno es el:")
    if opcion == "P":
        print(next(generador_perfumeria))
    elif opcion == "F":
        print(next(generador_farmacia))
    elif opcion == "C":
        print(next(genenerador_cosmetica))
    print("Aguarde y será atentido")
    print("*"*23)


