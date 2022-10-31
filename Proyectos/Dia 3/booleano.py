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

lista = [1,2,3,4]
control = 5 in lista
print(type(control))
print(control)

control = 5 not in lista
print(type(control))
print(control)