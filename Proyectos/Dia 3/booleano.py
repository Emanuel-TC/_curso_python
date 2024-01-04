var1 = True #se declara de manera directa
var2 = False
print(type(var1))
print(var1)
numero = 5 > 2+3 #se puede declarar de manera indirecta también
print(type(numero))
print(numero)

numero = 5 == 2+3 #se puede declarar de manera indirecta también
print(type(numero))
print(numero)

numero = bool(5>6) #se puede declarar de manera indirecta también
print(type(numero))
print(numero)
# También podemos generar valores booleanos al preguntar si existes elelmentos en las listas, tuples
lista = [1,2,3,4]
control = 5 in lista
print(type(control))
print(control)

control = 5 not in lista
print(type(control))
print(control)

# Ejercicios
'''Práctica Booleanos 1
Realiza una comparación que arroje como resultado un booleano y almacena el resultado (True/False) en una variable llamada prueba'''
prueba = bool(1<0)

'''Práctica Booleanos 2
Verifica si 17834/34 es mayor que 87*56 y muestra el resultado (booleano) en pantalla utilizando print()'''
prueba = bool(17834/34 > 87*56)
print(prueba)

'''Práctica Booleanos 3
Verifica si la raíz cuadrada de 25 es igual a 5 y muestra el resultado (booleano) en pantalla utilizando print()'''
prueba = bool(25**0.5==5)
print(prueba)