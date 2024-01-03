x = 6
y = 2
z = 7
print(f"{x} + {y} = {x+y}") #suma
print(f"{x} - {y} = {x-y}") #resta
print(f"{x} * {y} = {x*y}") #multiplicación
print(f"{x} / {y} = {x/y}") # división
# Las siguientes operaciones son útiles para resolver operaciones más complejas
# La división al piso elimina los deecimales del resultado de la divisón
print(f"{z} // {y} = {z//y}") #division al piso
# El módulo es el residuo de una división
print(f"{z} modulo de {y} es : {z%y}") #modulo
print(f"{x} elevado a la {y} es: {x**y}")
print(f"{x} elevado a la {3} es: {x**3}")
print(f"La raiz cuadrada de {x} es:  {x**0.5}") #se eleva a la 1/2

'''Práctica Operadores Matemáticos 1
Muestra en pantalla el cociente (división al piso) de los siguientes dos números: 874 dividido entre 27.'''
x = 874
y = 27
print(f"{x//y}")

'''Práctica Operadores Matemáticos 2
Muestra en pantalla el módulo (es decir, el resto) de la división entre 456 y 33.'''
x = 456
y = 33
print(f"{x%y}")

'''Práctica Operadores Matemáticos 3
Calcula y muestra en pantalla la raíz cuadrada de 783.'''
x= 783
print(f"{x**(1/2)}")