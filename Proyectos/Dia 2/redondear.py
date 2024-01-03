resultado = 90/7
redondeo = round(resultado) # round permite redondear el valor al entero más cercano
print(redondeo)
# también podemos usarlo para obtener sólo cierta cantidad de decimales, por ejemplo, para dos dígitos:
n = round(13.98888888888,2)
print(n)
'''Práctica Redondeo 1
Redondea el resultado de la división 10/3 a un número con 2 decimales, y muestra en pantalla el valor redondeado.'''
print(round(10/3,2))

'''Práctica Redondeo 2
Redondea el número 10.676767 al entero más próximo, y muestra en pantalla el resultado.'''
valor = 10.676767
print(round(valor))

'''Práctica Redondeo 3
Calcula la raíz cuadrada de 5, y muestra en pantalla el resultado redondeado con 4 posiciones decimales.'''
print(round(5**0.5,4))

print(type(round(13/2,0)))