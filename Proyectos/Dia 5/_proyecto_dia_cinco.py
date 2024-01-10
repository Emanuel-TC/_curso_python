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
#Se define la función para seleccionar una palabra al azar dentro de una lista de palabras.
def seleccionar_palabras(lista):
    palabra = choice(lista)
    lista_palabra = [letra for letra in palabra] #definimos palabra como una lista para después tener mejor control de las letras de la palabra
    return palabra, lista_palabra # devolvemos la string como tal, y una lista formada por las letras de la string


def revisar_letra_en_palabra(letra,palabra):
    if letra in palabra:
        return letra #si la letra sí está, la regresamos, porque la vamos a usar después
    else:
        return False #si no está, devolvemos False para hacer el chequeo después


def espacios_vacios(palabra):
    # En este ciclo usamos "_" porque nunca se usa esa variable, sólo se usa para contar
    palabra_vacia = ["_" for _ in palabra]
    return palabra_vacia

def reemplaza_espacio_por_letra(letra_encontrada,palabra_escogida): # recibe la letra ingresada y la palabra que se escogió
    palabra_nueva = [] # creamos una lista para ir llenándola con letras en el lugar donde aparecen
    for index, letra in enumerate(palabra_escogida): # usamos enumerate para obtener los índices de los valores de la lista
        if letra == letra_encontrada: #si existe una letra o más en la palabra que sea igual a la letra que se ingresó
            palabra_sin_letras[index] = letra_encontrada #sustituye esa letra ingresada en el índice que le corresponde
        else:
            pass #y usamos pass porque puede haber más de una letra, y queremos que siga revisando y añadiendo
    palabra_nueva = palabra_sin_letras #a la lista nueva le asignamos los valores encontrados de la lista anterior
    return palabra_nueva #regresamos esa nueva lista para mostrar el desarrollo del jugador

def revisar_espacios(palabra):
    if "_" in palabra: # si hay espacios vacíos todavía devolvemos True
        return True
    else: #si no los hay, devolvemos False
        return False

#Creamos la lista de palabras:
lista_palabras = ["mango","banana","cereza","ciruela","manzana","durazno","sandia"]

palabra_secreta, lista_de_palabra_escogida = seleccionar_palabras(lista_palabras) #Guardamos en una variable la palabra seleccionada
palabra_sin_letras = espacios_vacios(lista_de_palabra_escogida) #Guardamos en una variable la lista que se llenó con guíones
# por cada letra de la palabra escogida
print("Bienvenido al juego 'El ahorcado'")
print(f"La palabra escogida se ve así: {palabra_sin_letras}")

vidas = 0
while vidas < 7: #mientras no se haya equivocado más de 6 veces
    letra = input("Ingresa una letra: \n") #solicitamos que ingresa una letra, y guardamos esa letra en la variable letra
    if revisar_letra_en_palabra(letra, lista_de_palabra_escogida) == False: #revisamos si la letra está o no en la palabra, si no no está, entonces
        vidas += 1 #el contador de vidas aumenta
        if vidas >= 7: #y si sus vidas sobrepasaron el límite,
            print(f"Lo siento, has fallado, la palabra era {lista_de_palabra_escogida}") #imprime que ha fallado, y le muestra la palabra que debía encontrar
        else: #pero si no se le han acabado sus vidas, le recuerda cuántas le quedan
            print(f"Te quedan {7-vidas} vidas")
            pass
    else: #si la letra sí se encuentra
        print("La letra escogida sí está") #primero le dice que sí está
        print(f"Te quedan {7 - vidas} vidas") #le recuerda cuántas vidas le quedan
        letra_encontrada = revisar_letra_en_palabra(letra, lista_de_palabra_escogida) #almacena en una variable la letra que encontró
        palabra_llenada = reemplaza_espacio_por_letra(letra_encontrada, lista_de_palabra_escogida) #llena una nueva lista con la letra(s) encontrada en el lugar que debe ir
        print(palabra_llenada) #imprime esa lista, pero esa lista ya se guarda para mostrar su progreso
        if revisar_espacios(palabra_llenada) == False: #finalmente revisa si todavía hay espacios vacíos (guíones)
            print(f"Felicidades, adivinaste, la palabra escogida si es: {palabra_secreta}") #si ya no hay guíones #lo felicita e imprime nuevamente la palabra que encontró
            break #rompe el ciclo para dejar de pedir que ingrese letras porque aún le quedan vidas
        else: #si todavía hay guíones, pasa, y continúa preguntando
            pass