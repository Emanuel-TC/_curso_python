# primer forma de declarar el set
mi_set = set([1,2,3,4,5])
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)
# Segunda forma de declarar un set
otro_set = {1,2,3,4,1,1,1,1,2,2,2,2}
print(f"En los sets no hay repetcion de elementos, como en este {otro_set}")
otro_set = {1,2,3,4,1,1,1,1,2,2,2,2,(1,2,3)}
print(f"Pero si puede tener tuples dentro, como este {otro_set}")
print(f"El largo del set {otro_set} es {len(otro_set)}")
# podemos verificar si un elemento en específico existe en el set
print(f"¿Es verdad que 2 está en {otro_set}? {2 in otro_set}")
# usamos métodos de set
un_set_mas = mi_set.union(otro_set)
print(f"Los valores del nuevo set son : {un_set_mas}")
# metdo agregar
un_set_mas.add(6)
print(f"Los valores del nuevo set son : {un_set_mas}")
# metodo eliminiar
un_set_mas.remove(1)
print(f"Los valores del nuevo set son : {un_set_mas}")
# remover un elemento de manera aleatoria
sorteo = un_set_mas.pop() #siempre y cuando se deje vacío el argumento
print(f"El ganador es: {sorteo}")

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
ganador = sorteo.pop()
print(f"El ganador 'a' es {ganador} ")

# Usando el método clear para limpiar el set
mi_set.clear()
print(mi_set)
# Ejercicios

'''Práctica Sets 1
Une los siguientes sets en uno solo, llamado mi_set_3:

{1, 2, "tres", "cuatro"}

{"tres", 4, 5}'''

mi_set_1 = {1, 2, "tres", "cuatro"}
mi_set_2 = {"tres", 4, 5}
mi_set_3 = mi_set_1.union(mi_set_2)

'''Práctica Sets 2
Elimina un elemento al azar del siguiente set, utilizando métodos de sets.

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}'''

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
ganador = sorteo.pop()

'''Práctica Sets 3
Agrega el nombre Damián al siguiente set, utilizando métodos de sets:

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}'''

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
sorteo.add("Damián")