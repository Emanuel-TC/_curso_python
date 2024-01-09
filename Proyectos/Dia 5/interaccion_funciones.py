from random import shuffle
from random import randint

#lista inicial
palitos = ["-","--","---","----"]

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#print(mezclar(palitos))

#pediler intento
def probar_suerte():
    intento = ""
    while intento not in ["1","2","3","4"]:
        intento = input("Escoge un numero del 1 al 4:\n ")
    return int(intento)
#intentos = probar_suerte()
#print(intentos)

#comprobar intento
def revisar_intento(lista,intento):
    # se resta menos uno porque las listan empiezan en 0
    if lista[intento - 1] == "-":
        print("Lava los platos ja, ja")
    else:
        print("Esta vez te has salvado")
    print(f"Te tocó el palito {lista[intento - 1]}\n")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
revisar_intento(palitos_mezclados,seleccion)

# Ejercicios
'''Práctica sobre Interacción entre Funciones 1
Crea una función (lanzar_dados) que arroje dos dados al azar y devuelva sus resultados:

La función debe retornar dos valores resultado, que se encuentren entre 1 y 6).

Dicha función no debe requerir argumentos para funcionar, sino que debe generar internamente los valores aleatorios.

Proporciona el resultado de estos dos dados a una función que se llame evaluar_jugada (es decir, esta segunda función debe recibir dos argumentos) y que retorne -sin imprimirlo- un mensaje según la suma de estos valores:

Si la suma es menor o igual a 6:

"La suma de tus dados es {suma_dados}. Lamentable"

Si la suma es mayor a 6 y menor a 10:

"La suma de tus dados es {suma_dados}. Tienes buenas chances"

Si la suma es mayor o igual a 10:

"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"'''
def lanzar_dados():
    primer_dado = randint(1, 6)
    segundo_dado = randint(1, 6)
    return primer_dado, segundo_dado


def evaluar_jugada(dado_uno,dado_dos):

    suma_dados = dado_uno + dado_dos
    if suma_dados <= 6:
        return f"La suma de tus dados es {suma_dados}. Lamentable"
    elif (suma_dados > 6) and (suma_dados < 10):
        return f"La suma de tus dados es {suma_dados}. Tienes buenas chances"
    else:
        return f"La suma de tus dados es {suma_dados}. Parece una jugada ganadora"

dado_uno, dado_dos = lanzar_dados()
resultado = evaluar_jugada(dado_uno,dado_dos)
print(resultado)

'''Práctica sobre Interacción entre Funciones 2
Crea una función llamada reducir_lista() que tome una lista como argumento (crea también la variable lista_numeros), y devuelva la misma lista, pero eliminando duplicados (dejando uno solo de los números si hay repetidos) y eliminando el valor más alto. El orden de los elementos puede modificarse.

Por ejemplo, si se le proporciona la lista [1,2,15,7,2] debe devolver [1,2,7].

Crea una función llamada promedio() que pueda recibir como argumento la lista devuelta por la anterior función, y que calcule el promedio de los valores de la misma. Debe devolver el resultado, sin imprimirlo.'''

def reducir_lista(lista):
    mi_set = set(lista)
    mi_lista = list(mi_set)
    mi_lista.sort()
    mi_lista.pop(-1)
    return mi_lista
def promedio(lista):
    contador = 0
    suma = 0
    for numero in lista:
        contador += 1
        suma += numero
    promedio = suma / contador
    return promedio
lista_numeros = [1,2,15,7,2]

lista_reducida = reducir_lista(lista_numeros)
prom = promedio(lista_reducida)
print(prom)

'''Práctica sobre Interacción entre Funciones 3
Crea una función (llamada lanzar_moneda) que devuelva el resultado de lanzar una moneda (al azar). Dicha función debe poder devolver los resultados "Cara" o "Cruz", y no debe recibir argumentos para funcionar.

Crea una segunda función (llamada probar_suerte), que tome dos argumentos: el primero, debe ser el resultado del lanzamiento de la moneda. El segundo argumento, será una lista de números cualquiera (debes crear una lista con valores y llamarla lista_numeros).

Si se le proporciona una "Cara", debe mostrar el mensaje al usuario: "La lista se autodestruirá", y eliminarla (devolverla como lista vacía []).

Si se le proporciona una "Cruz", debe imprimir en pantalla: "La lista fue salvada" y devolver la lista intacta.'''

def lanzar_moneda():
    lanzamiento = {"Cara", "Cruz"}
    sorteo = lanzamiento.pop()
    return sorteo

def probar_suerte(moneda, lista):
    if moneda == "Cara":
        print("La lista se autodestruirá")
        lista = []
        return lista
    else:
        print("La lista fue salvada")
        return lista

lista_numeros = list(range(1, 11))