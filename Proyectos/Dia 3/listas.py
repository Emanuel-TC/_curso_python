# En este archivo veremos el uso de listas
mi_lista = ['a','b','c']
otra_lista = ['Hola', 12, 7.1]
# podemos ver la longitud de la lista
resultado = len(mi_lista)
# imprimimos el tipo de dato
print(type(mi_lista))
print(resultado)
# podemos ver el elemento de la lista en la posición 0
resultado = mi_lista[0]
print(resultado)
# en la variable guardamos todos los elementos de la lista tomando de uno en uno
resultado = mi_lista[::1]
print(resultado)
# podemos unir dos listas de esta forma
print(mi_lista+otra_lista)
mi_lista3 = mi_lista+otra_lista
# Podemos agregar alementos a la lista, en este caso, en la primer posición, agremamos la cadena "Cabeza"
mi_lista3[0] = "Cabeza"
print(mi_lista3)
# añade un elemento, por defecto, al final de la lista
mi_lista3.append('cola')
print(mi_lista3)
# por defecto elimina el último, en este caso, eliminaría cola
mi_lista3.pop()
print(mi_lista3)
# se indica el indice que se va a elminiar, en este caso, cabeza
mi_lista3.pop(0)
print(mi_lista3)
b = mi_lista3.pop(0) #se indica el indice que se va a elminiar, en este caso, se guarda
print(f"Se eliminó la letra {b} de la lista {mi_lista3}")
nueva_lista = ['d','c','b','a']
nueva_lista.sort() #se ordena la lista en orden
print(nueva_lista)
nueva_lista.reverse() #ordena la lista del ultimo al primero
print(nueva_lista)

'''Práctica Listas 1
Crea una lista con 5 elementos, dentro de la variable mi_lista. Puedes incluir strings, booleanos, números, etc.'''
mi_lista = ['a', 'b',3, 4.0, "Cola"]

'''agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.'''
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)

'''Práctica Listas 3
Utiliza el método pop() para quitar el tercer elemento de la siguiente lista llamada frutas, y almacénalo en una variable llamada eliminado. Utiliza métodos de listas sin alterar la línea de código ya suministrada.

manzana

banana

mango

cereza

sandía'''
frutas = ["manzana", "banana", "mango", "cereza", "sandía"]
eliminado = frutas.pop(2)