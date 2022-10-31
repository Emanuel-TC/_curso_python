mi_bool = 10 == 25 #compara un numero con otro
print(type(mi_bool))
print(mi_bool)
mi_bool = 10+25 == 15+20 #compara el resultado de la operación
print(type(mi_bool))
print(mi_bool)

mi_bool = 'rojo' == 'Rojo' #Compara string, pero es sensible a mayúsculos y minúsculas
print(type(mi_bool))
print(mi_bool)

mi_bool = 'rojo' == 'Rojo'.lower() #se puede ajustar
print(type(mi_bool))
print(mi_bool)

mi_bool = 5 != 'rojo' #No es igual
print(type(mi_bool))
print(mi_bool)