# Ocupan menos espacio de memoria
# No se pueden modificar
# Son más rápidas
# Son más seguras

mi_tupple = (1,2,3,4,5)
# se puede indexar
print(mi_tupple[0])
# se puede anidar
mi_tupple = (1,2,3,4,5, (6,7,8))
print(mi_tupple[5][1])

'''
Práctica Tuples 1
Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla, y muestra el resultado (integer) en pantalla:
'''
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

'''
Práctica Tuples 2
Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
'''
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

'''
Práctica Tuples 3
Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d
'''
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla