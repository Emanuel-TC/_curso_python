''''Hoy vas a
programar El Ahorcado. El juego es muy sencillo y popular, pero por si acaso te lo explico
rápidamente.
El programa va a elegir una palabra secreta y le va a mostrar al jugador solamente una serie
de guiones que representa la cantidad de letras que tiene la palabra. El jugador en cada turno
deberá elegir una letra y si la letra se encuentra en la palabra oculta, el sistema le va a
mostrar en qué lugares se encuentra. Pero si el jugador dice una letra que no se encuentra en
la palabra oculta, pierde una vida.
le vamos a decir que tiene seis vidas y se las iremos descontando de una
en una, cada vez que el jugador elija una letra incorrecta.
Si se agotan las vidas antes de adivinar la palabra, el jugador pierde. Pero si adivina la palabra
completa antes de perder todas las vidas, el jugador gana.
    Primero vas a crear un código que importe el método choice, ya que lo vas a necesitar
para que el sistema pueda elegir una palabra al azar dentro de una lista de palabras que
también vas a crear al comienzo.
    Luego de eso, vas a crear tantas funciones como creas necesarias para que el programa
haga cosas como pedirle al usuario que elija una letra, para corroborar si lo que el usuario
ha ingresado es una letra válida, para chequear si la letra ingresada se encuentra en la
palabra o no, para verificar si ha ganado o no, etc.
    Recuerda escribir primero las funciones y luego el código que las implementa
ordenadamente.

'''
from random import choice
def seleccionar_palabras(lista):
    lista_palabra = choice(lista)
    palabra = []
    for letra in lista_palabra:
        palabra.append(letra)
    return palabra


def revisar_letra_en_palabra(letra,palabra):
    if letra in palabra:
        return letra
    else:
        return False

def espacios_vacios(palabra):
    palabra_vacia = []
    for letra in palabra:
        palabra_vacia.append("_")
    return palabra_vacia

def reemplaza_espacio_por_letra(letra_encontrada,palabra_escogida):
    palabra_nueva = []
    for index, letra in enumerate(palabra_escogida):
        if letra == letra_encontrada:
            palabra_sin_letras[index] = letra_encontrada
        else:
            pass
    palabra_nueva =palabra_sin_letras
    return palabra_nueva

def revisar_espacios(palabra):
    if "_" in palabra:
        return True
    else:
        return False

lista_palabras = ["mango","banana","cereza","ciruela"]

palabra_escogida = seleccionar_palabras(lista_palabras)
palabra_sin_letras = espacios_vacios(palabra_escogida)
print(f"La palabra escogida se ve así: {palabra_sin_letras}")
vidas = 0
while vidas < 7:
    letra = input("Ingresa una letra: \n")
    if revisar_letra_en_palabra(letra,palabra_escogida) == False:
        vidas += 1
        if vidas >= 7:
            print("Lo siento, has fallado")
        else:
            print(f"Te quedan {7-vidas} vidas")
            pass
    else:
        print("La letra escogida sí está")
        print(f"Te quedan {7 - vidas} vidas")
        letra_encontrada = revisar_letra_en_palabra(letra, palabra_escogida)
        palabra_llenada = reemplaza_espacio_por_letra(letra_encontrada, palabra_escogida)
        print(palabra_llenada)
        if revisar_espacios(palabra_llenada) == False:
            break
        else:
            pass
    #print(palabra_llenada)

print(f"Felicidades, adivinaste, la palabra escogida si es: {palabra_escogida}")





