lista = ['pablo','luis,','laura','fede','julia'] #se declara la lista
for nombre in lista: #se puede leer como: por_cada nombre en lista
    if nombre.startswith('l'): #si nombre empieza con L
        print(f"El nombre de {nombre} empieza con L") #imprime el nombre con l
    else:
        print(f"El nombre de {nombre} no empieza con L") #imprimer el nombre sin L
numeros= [1,2,3,4,5]
valor = 0
for numero in numeros:
    valor = valor + numero #en cada iteración se suma el valor anterior
    print(valor)

palabra = 'python'
for letra in palabra:
    print(letra)

for objeto in [[1,2],[3,4],[5,6]]: #se puede imprimir un arreglo de listas en conjunto
    print(objeto)

for objeto_a,objeto_b in [[1,2],[3,4],[5,6]]: #se puede imprimir por separado cada elemento asignándolo a otra variable
    print(objeto_a)
    print(objeto_b)

#for en diccionarios
dic ={'clave1':'a', 'clave2':'b', 'clave3':'c'}
for item_por_defecto in dic:
    print(f"por defecto se imprimen la {item_por_defecto} del diccionario")

for valor in dic.values():
    print(f"Se imprime el valor {valor} del diccionario")
for clave in dic.keys():
    print(f"Se imprime la clave {clave} del diccionario")
for items in dic.items():
    print(f"Se imprime el item {items} del diccionario")

#Dada la siguiente lista de números, realiza la suma de todos los números utilizando loops For y almacena el resultado
# de la suma en una variable llamada suma_numeros: lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_numeros = 0
for numero in lista_numeros:
    suma_numeros = suma_numeros + numero
    print(suma_numeros)

#Dada la siguiente lista de números, realiza la suma de todos los números pares e impares* por separado en las variables
# suma_pares y suma_impares respectivamente: lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
#*Recordando de los días anteriores: el módulo (o resto) de un número dividido 2 es cero cuando dicho valor es par, y 1 cuando es impar

num % 2 == 0 (valores pares)

num % 2 == 1 (valores impares)

lista_numeros = [1,5,8,7,6,8,2,5,2,6,4,8,5,9,8,3,5,4,2,5,6,4]
suma_pares = 0
suma_impares = 0
for numero in lista_numeros:
    if numero % 2 == 0:
        suma_pares = suma_pares + numero
        print(f"La suma de los numeros pares es: {suma_pares}")
    else:
        suma_impares = suma_impares + numero
        print(f"La suma de los numeros impares es: {suma_impares}")