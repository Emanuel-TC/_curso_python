#la comprension de listas facilita mucho su uso

palabra = "Python"

lista = []

for letra in palabra:
    lista.append(letra)

print("Sin compresión de listas")
print(lista)

#es más simple con compresión de listas

lista = [letra for letra in palabra] #una letra por cada letra que haya en palabra
print("Con compresión de listas")
print(lista)

lista_numeros = [numero/2 for numero in range(0,21,2)]
print(lista_numeros)
#se puedeintegra un if en esta compresión de listas
lista_numeros = [numero/2 for numero in range(0,21,2) if numero*2 >= 10 ]
print(lista_numeros)

lista_numeros = [numero for numero in range(0,21,2)]
print(lista_numeros)
#se puedeintegra un if en esta compresión de listas
lista_numeros = [numero if numero*2 >= 10 else f"el numero {numero} multiplicado por 2 no es mayor que 10" for numero in range(0,21,2)] #si se agrega un else, entonces
#va al inicio antes del for y antes de la varibale que va a ser el índice
print(lista_numeros)

pies = list(range(10,51,10))
metros =[pie/3.281 for pie in pies]
print(metros)


#Práctica Comprensión de Listas 1
#Para realizar el ejercicio a continuación, puedes optar por diferentes caminos. Si bien en programación el camino
# correcto es el que devuelve el resultado correcto, te animo a que intentes aplicar los conceptos de comprensión de listas para comenzar a afianzarlos para el futuro. ¡Pueden resultarte muy útiles en tu práctica profesional!
#Crea una lista valores_cuadrado formada por los números de la lista valores, elevados al cuadrado.
#valores = [1, 2, 3, 4, 5, 6, 9.5]
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_cuadrado = [cuadrado ** 2 for cuadrado in valores]
print(valores_cuadrado)

#Crea una lista valores_pares formada por los números de la lista valores que (¡adivinaste!) sean pares.
#valores = [1, 2, 3, 4, 5, 6, 9.5]
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [par for par in valores if par % 2 ==0]
print(valores_pares)

#Para la siguiente lista de temperaturas en grados Fahrenheit, expresa estos mismos valores en una nueva lista
# de valores de temperatura en grados Celsius. La conversión entre tipo de unidades es la siguiente:
#°C = (°F - 32) * (5/9)
#o expresado de otro modo:
# (grados_fahrenheit-32)*(5/9)

temperatura_fahrenheit = [32, 212, 275]
grados_celsius = [(grado -32)*(5/9) for grado in temperatura_fahrenheit]
print(grados_celsius)



