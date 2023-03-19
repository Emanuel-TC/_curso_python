import math

redondeo_abajo = math.floor(67.87)
print(redondeo_abajo)
redondeo_arriba = math.ceil(67.87)
print(redondeo_arriba)
numero_pi = math.pi
print(numero_pi)
logaritmo = math.log(64, 2)
print(f"Si quieres saber a qué exponente debes elevar el 2 para que te dé 64, el resultado es: {logaritmo}")

'''
Obtén el logaritmo base 10 del número 25, y almacena el resultado en la variable resultado.
Puedes utilizar el método math.log10()
Puedes consultar el enlace anterior si quieres conocer más acerca del logaritmo decimal.
'''
resultado = math.log10(25)
print(f"El logartmo base 10 del número 25 es: {resultado}")

'''
Práctica Módulo Math 2
Obten la raíz cuadrada de pi con la constante math.pi y el método math.sqrt() . 
Almacena el resultado obtenido en la variable resultado.
'''
resultado = math.sqrt(math.pi)
print(f"La raíz cuadrada de pi es: {resultado}")

'''
Encuentra el factorial de 7 y almacena el resultado en la variable resultado.
El método a utilizar es factorial() 
'''
resultado = math.factorial(7)
print(f"El factorial de 7 es: {resultado}")