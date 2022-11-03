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
metros =[pie*3.281 for pie in pies]
print(metros)




