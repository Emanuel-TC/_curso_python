# En este archivo vamos a usar las conversiones para cambiar el tipo de dato que tenemos
edad = input("Dime tu edad ")
print(type(edad))
# A continuación escribimos explícitamente que convetiremos el valor 'edad' en un entero
edad = int(edad)
print(type(edad))
nueva_edad = (1+edad)
print(nueva_edad)

'''Práctica con Conversiones 1
Convierte el valor de num1 en un int e imprime el tipo de dato que resulta:'''
num1 = 7.5
num1 = int(num1)
print(type(num1))

'''Práctica con Conversiones 2
Convierte el valor de num2 en un float e imprime el tipo de dato que resulta:'''
num2 = 10
num2 = float(num2)
print(type(num2))

'''Práctica con Conversiones 3
Suma los valores de num1 y num2.

No modifiques el valor de las variables ya declaradas, sino aplica las conversiones necesarias dentro de la función print().'''
num1 = "7.5"
num2 = "10"

print(num3 = int(num1) + float(num2))