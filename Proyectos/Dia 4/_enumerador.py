lista = ['a','b','c']

indice = 0 #a la manera tradicional
print("Enumeración de una lista de forma tradicional")
for item in lista: # se realiza
    print(indice,item) # así
    indice += 1
#con enumerate es:
print("Enumeración de una lista con enumerate:")
for item in enumerate(lista):
    print(item)
print("Con variables separadas: ")
for indice,item in enumerate(lista): # sólo agregamos la variable en donde se almacena la
    print(indice,item)
#se puede implentar con un range
print("Enumerate con range: ")
for indice,item in enumerate(range(50,56)):
    print(indice,item)
#hacemos un cast de enumerate con list
#para transformar la lista en una lista de tuples
print("Tuple de la lista")
mis_tuples = list(enumerate(lista))
print(mis_tuples)
#si queremos sacar un elemento se hace con el índice del tuple y el índice de la lista
print("Se imprime el índice 2 del tuple, y el índice 1 de la lista, y sale 'c': ")
print(mis_tuples[2][1])

#Imprime en pantalla frases como la siguiente:
#'{nombre} se encuentra en el índice {indice}'
#Donde nombre debe ser cada uno de los nombres de la lista a continuación, y el índice, obtenido mediante enumerate().
#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#Puedes modificar la línea print() otorgada como ejemplo, pero las frases entregadas deberán ser iguales.
#Tip: utiliza loops!

lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    print(f'{nombre} se encuentra en el índice {indice}')

#Crea una lista formada por las tuplas (indice, elemento), formadas a partir de obtener
# mediante enumerate() los índices de cada caracter del string "Python".
#Llama a la lista obtenida con el nombre de variable lista_indices.

lista_indices = list(enumerate("Python"))
print(lista_indices)

#Imprime en pantalla únicamente los índices de aquellos nombres de la lista a continuación, que empiecen con M:
#lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
#Puedes resolverlo de diferentes maneras, pero servirá que tengas presente todos o algunos de los siguientes elementos:
#Loops
#Condicionales if
#El método enumerate()
#Métodos de strings o indexado
#   La respuesta al ejercico es la siguiente:
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice)
#Pero si te quieres más pro puedes hacerlo así:
print("Eejercicio con indicación de aquellos indices y nombres que no cumplen también")
lista_nombres = ["Marcos", "Laura", "Mónica", "Javier", "Celina", "Marta", "Darío", "Emiliano", "Melisa"]
for indice,nombre in enumerate(lista_nombres):
    if nombre.startswith("M"):
        print(indice,nombre)
    else:
        print(f"El nombre {nombre} en el índice {indice} no empieza con 'M'")