mi_lista = ['a','b','c']
otra_lista = ['Hola', 12, 7.1]
resultado = len(mi_lista)
print(type(mi_lista))
print(resultado)
resultado = mi_lista[0]
print(resultado)
resultado = mi_lista[::1]
print(resultado)
print(mi_lista+otra_lista)
mi_lista3 = mi_lista+otra_lista
mi_lista3[0] = "Cabeza"
print(mi_lista3)
mi_lista3.append('cola') #añade un elemento, por defecto, al final de la lista
print(mi_lista3)
mi_lista3.pop() #por defecto elimina el último, en este caso, eliminaría cola
print(mi_lista3)
mi_lista3.pop(0) #se indica el indice que se va a elminiar, en este caso, cabeza
print(mi_lista3)
b = mi_lista3.pop(0) #se indica el indice que se va a elminiar, en este caso, se guarda
print(f"Se eliminó la letra {b} de la lista {mi_lista3}")
nueva_lista = ['d','c','b','a']
nueva_lista.sort() #se ordena la lista en orden
print(nueva_lista)
nueva_lista.reverse() #ordena la lista del ultimo al primero
print(nueva_lista)

#agrega el elemento "motocicleta" a la siguiente lista de medios de transporte:
#medios_transporte = ["avión", "auto", "barco", "bicicleta"]
#No debes modificar la línea de código ya suministrada, sino que debes emplear el método apropiado de listas para añadir un nuevo elemento.
medios_transporte = ["avión", "auto", "barco", "bicicleta"]
medios_transporte.append("motocicleta")
print(medios_transporte)
