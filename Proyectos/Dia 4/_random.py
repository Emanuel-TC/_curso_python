#from random import randint
#para importar todos los metodos de random,después de import escribimos un asterisco
from random import *
aleatorio = randint(1,50) #randint es para un valor random pero del tipo entero
print(aleatorio)

aleatorio = round(uniform(1,5),1)# arroja un valor random flotante muuuy grande, lo que se puede solucionar con un round, la camtidad de decimales que se quieren
print(aleatorio)

#el metodo random no requiere un parametro, pero arroja un valor random entre 0 y 1
aleatorio = random()
print(aleatorio)

#despues vemos choice, que escoge de una lista, un diccionario, tupple un valor al azar

colores = ['red','green','blue','purple']
aleatorio = choice(colores)
print(aleatorio)

#veremos el metodo shuffle, que es para mezclar de manera aleatoria el orden de la lista, diccionario, tupple, pero no se aplican en el orden de un string

numeros = list(range(5,50,5))
shuffle(numeros)
print(numeros)

#Implementa la función randint() de la librería random que te permita obtener un número entero del 1 al 10,
# y almacena dicho valor en una variable llamada aleatorio

#from random import randint
aleatorio = randint(1,10)

#Práctica Random 2
#Implementa la función random() de la librería random que te permita obtener un número decimal entre 0 y 1,
# y almacena dicho valor en una variable llamada aleatorio
#from random import *
aleatorio = random()

#Práctica Random 3
#Utiliza el método choice() de la librería random para obtener un elemento al azar de la lista de nombres a continuación,
#y almacena el nombre escogido en una variable llamada sorteo.
#nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]

nombres = ["Carlos", "Julia", "Nicole", "Laura", "Mailen"]
sorteo = choice(nombres)
print(sorteo)
