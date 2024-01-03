# Para declarar un tuple, simplemente se escriben los valores frente a la variable, de preferencia entre parétesis
mi_tuple = (1,2,3,4)
print(type(mi_tuple))
t= (1,2.0,'Hola')
# también se puede ver el contenido de un índice
print(t[2])
t= (1,2.0,'Hola',(3,4.0,'mundo'))
print(t[3][2]) #se consulta el índice de un índice
# se pueden asignar los valores del tuple a otras variables, pero debe haber suficientes valores por cada variable
w,x,y,z = t
print(w,x,y,z)
t= (1,2.0,'Hola',(3,4.0,'mundo'),1)
print(len(t))
# se cuentan las apariciones del valor dentro de count
print(t.count(1))
print(f"el valor de {t[1]} está en el índice {t.index(2.0)}") #el índice d eun valor

# Ejercicios

'''Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla,
y muestra el resultado (integer) en pantalla: '''
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

# Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)

'''Práctica Tuples 3
Extrae los elementos de la siguiente tupla en cuatro variables: a, b, c, d

mi_tupla = (1, 2, 3, 4)'''
mi_tupla = (1, 2, 3, 4)
a,b,c,d = mi_tupla