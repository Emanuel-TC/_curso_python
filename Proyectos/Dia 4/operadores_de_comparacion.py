'''En esta lección, veremos el uso de los booleanos'''
# compara un numero con otro
mi_bool = (10 == 25) # para una mejor comprensión, lo encerramos entre paréntesis
# imprimimos el tipo de dato
print(type(mi_bool))
# e imprimimos el dato
print(mi_bool)
mi_bool = (10+25 == 15+20) #compara el resultado de la operación
print(type(mi_bool))
print(mi_bool)

mi_bool = ('rojo' == 'Rojo') #Compara string, pero es sensible a mayúsculos y minúsculas
print(type(mi_bool))
print(mi_bool)

mi_bool = ('rojo' == 'Rojo'.lower()) #se puede ajustar
print(type(mi_bool))
print(mi_bool)

mi_bool = (5 != 'rojo') #No es igual
print(type(mi_bool))
print(mi_bool)

# Ejercicios

'''Práctica Operadores de Comparación 1
Crea dos variables (num1 y  num2) con los valores 36 y 17 respectivamente. 
Verifica si num1 es mayor o igual que num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool'''
num1,num2 =36,17
mi_bool = (num1 >= num2)

'''Práctica Operadores de Comparación 2
Crea dos variables (num1 y  num2):

Dentro de num1, almacena el resultado de la operación raíz cuadrada de 25

Dentro de num2, almacena el número 5.

Verifica si num1 es igual a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.
'''
num1,num2 = 25**0.5, 5
mi_bool = (num1 ==num2)

'''Práctica Operadores de Comparación 3
Crea dos variables (num1 y  num2):

Dentro de num1, almacena el resultado de la operación 64 x 3

Dentro de num2, almacena el resultado de la operación 24 x 8

Verifica si num1 es diferente a num2 y almacena el resultado de dicha comparación en una variable llamada mi_bool.'''

num1, num2 = 64*3, 24*8
mi_bool = (num1!=num2)