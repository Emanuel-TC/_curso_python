from collections import Counter
from collections import defaultdict
from collections import namedtuple
from collections import deque
from random import randint

numeros = [randint(1, 10) for i in range(20)]
print(numeros)
#counter cuenta la cantidad de veces que se repite un elmento en un grupo que se ingresa como parámetro
print(Counter(numeros))
print(Counter("paragaricutirimicuaro"))
frase = "tres tristes tigres tragaban trigo en un trigal en un trigal tres tristes tigres tragaban trigo"
print(Counter(frase.split()))
serie = [randint(1, 5) for i in range(20)]
print(serie)
#primer valor el numero, segundo, las veces que se repite
print(Counter(serie).most_common())
print(list(Counter(serie)))
#si no existe un valor en el diccionario, se crea una key sin valor

mi_dic = defaultdict(lambda : "vacio")
mi_dic["uno"] = "verde"
#no he asigando una key dos, por lo tanto tampoco hay ningún valor
#pero defaultdic crea el valor vacio
print(mi_dic["uno"])
print(mi_dic["dos"])

#con namedtuple podemos acceder a valores d euna tupla desde un nombre
#creamos una namedtuple con el nombre Persona

Persona = namedtuple('Persona', ['nombre', 'edad', 'altura'])
ema = Persona('Ema', 25, 1.71)
print(ema.nombre,ema.edad,ema.altura)
#o bien
print(ema[0],ema[1],ema[2])
#pero es más fácil de indentificar con los nombres de las tuplas


'''
Práctica Módulo Collections 1
Aplica un Counter (contador) sobre la lista de números entregada a continuación, 
y almacénalo en una variable llamada contador 
'''

lista = [1, 2, 3, 6, 7, 1, 2, 4, 5, 5, 5, 5, 3, 2, 6, 7]

contador = Counter(lista)


'''
Práctica Módulo Collections 2

Crea un diccionario llamado mi_diccionario, para el cual, cuando no se halle una palabra clave buscada, 
se cargue con el string "Valor no hallado".

Carga el diccionario, al menos, con el siguiente par de datos:

    palabra clave = edad

    valor = 44

Utiliza el método defaultdict del módulo Collections.
'''
mi_diccionario = defaultdict(lambda : "Valor no hallado")
mi_diccionario["edad"] = 44
print(mi_diccionario["cedula"])
print(mi_diccionario)



'''
Una cola doblemente terminada o deque (del inglés double ended queue) es una estructura de 
datos lineal que permite insertar y eliminar elementos por ambos extremos.

Investiga más al respecto en cualquier sitio de documentación, y a continuación 
implementa una deque a partir del módulo collections. Los elementos iniciales de la lista se 
brindan a continuación.

["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"]

La lista debe tener la capacidad de incorporar elementos por la izquierda, y recibir el 
nombre lista_ciudades.
'''

lista_ciudades = deque(["Londres", "Berlin", "París", "Madrid", "Roma", "Moscú"])
print(lista_ciudades)