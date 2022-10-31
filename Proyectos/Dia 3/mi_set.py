mi_set = set([1,2,3,4,5]) #primer forma de declarar el set
print(type(mi_set))
print(mi_set)

otro_set = {1,2,3}
print(type(otro_set))
print(otro_set)
otro_set = {1,2,3,4,1,1,1,1,2,2,2,2}
print(f"En los sets no hay repetcion de elementos, como en este {otro_set}")
otro_set = {1,2,3,4,1,1,1,1,2,2,2,2,(1,2,3)}
print(f"Pero si puede tener tuples dentro, como este {otro_set}")
print(f"El largo del set {otro_set} es {len(otro_set)}")
print(f"¿Es verdad que 2 está en {otro_set}? {2 in otro_set}")
#usamos métodos de set
un_set_mas = mi_set.union(otro_set)
print(f"Los valores del nuevo set son : {un_set_mas}")
#metdo agregar
un_set_mas.add(6)
print(f"Los valores del nuevo set son : {un_set_mas}")
#metodo eliminiar
un_set_mas.remove(1)
print(f"Los valores del nuevo set son : {un_set_mas}")
#remover un elemento de manera aleatoria
sorteo= un_set_mas.pop() #siempre y cuando se deje vacío el argumento
print(f"El ganador es: {sorteo}")

sorteo = {"Camila", "Margarita", "Axel", "Jorge", "Miguel", "Mónica"}
ganador = sorteo.pop()
print(f"El ganador 'a' es {ganador} ")
