mi_tuple = (1,2,3,4)
print(type(mi_tuple))
t= (1,2.0,'Hola')
print(t[2]) #también se puede ver el contenido de un índice
t= (1,2.0,'Hola',(3,4.0,'mundo'))
print(t[3][2]) #se consulta el índice de un índice
w,x,y,z =t #se pueden asignar los valores del tuple a otras variables, pero debe haber suficientes valores por cada variable
print(w,x,y,z)
t= (1,2.0,'Hola',(3,4.0,'mundo'),1)
print(len(t))
print(t.count(1)) #se cuentan las apariciones del valor dentro de count
print(f"el valor de {t[1]} está en el índice {t.index(2.0)}") #el índice d eun valor

#Utiliza un método de tuplas para contar la cantidad de veces que aparece el valor 2 en la siguiente tupla,
# y muestra el resultado (integer) en pantalla:
mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2, 3, 3, 3, 1, 3, 2, 2, 1, 3, 2)
print(mi_tupla.count(2))

#Convierte a lista la siguiente tupla, y almacénala en una variable llamada mi_lista.

mi_tupla = (1, 2, 3, 2, 3, 1, 3, 2)
mi_lista = list(mi_tupla)