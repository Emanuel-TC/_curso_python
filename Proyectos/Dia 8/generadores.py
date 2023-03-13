from PIL.XVThumbImagePlugin import g


def mi_funcion():
    lista = []
    for numero in range(1, 5):
        lista.append(numero * 10)
    return lista


def mi_generador():
    for numero in range(1, 5):
        yield numero * 10


print(mi_funcion())
print(mi_generador())
numero = mi_generador()
#genera los números hasta que se los pido, y así evita consumir espacio de memoria insuficiente
print(next(numero))
print(next(numero))
print(next(numero))
print(next(numero))

def otro_generador():
    x = 0
    yield x
    x += 1
    yield x
    x += 1
    yield x

generador = otro_generador()
print(next(generador))
print(next(generador))
#recuerda en lo que se queda si antes hay código en medio
print("Hola")
print(next(generador))

'''
Práctica Generadores 1
Crea un generador (almacenado en la variable generador) que sea capaz de devolver una 
secuencia infinita de números, iniciando desde el 1, y entregando un número consecutivo 
superior cada vez que sea llamada mediante next.
'''

def secuencia_infinita():
    numero = 1
    while True:
        yield numero
        numero += 1

infinito = secuencia_infinita()
for i in range(10):
    print(next(infinito))
print(next(infinito))

'''
Crea un generador (almacenado en la variable generador) que sea capaz de devolver de manera 
indefinida múltiplos de 7, iniciando desde el mismo 7, y que cada vez que sea llamado devuelva 
el siguiente múltiplo (7, 14, 21, 28...).
'''
def multiplo_7():
    numero = 1
    while True:
        yield numero * 7
        numero += 1


generador = multiplo_7()
for i in range(7):
    print(next(generador))

'''
Práctica Generadores 3

Crea un generador que reste una a una las vidas de un personaje de videojuego, y devuelva 
un mensaje cada vez que sea llamado:

    "Te quedan 3 vidas"

    "Te quedan 2 vidas"

    "Te queda 1 vida"

    "Game Over"

Almacena el generador en la variable perder_vida 
'''
def contador_vidas():
    yield "Te quedan 3 vidas"
    yield "Te quedan 2 vidas"
    yield "Te queda 1 vida"
    yield "Game Over"

perder_vida = contador_vidas()
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))
print(next(perder_vida))