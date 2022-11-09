''' Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valorintermedio.

'''
def devolver_distintos(numero_uno, numero_dos, numero_tres):
    lista = [numero_uno, numero_dos, numero_tres]
    suma_numeros = numero_uno + numero_dos + numero_tres
    lista = sorted(lista)
    if suma_numeros > 15:
        return lista[2]
    elif (suma_numeros >= 10) and (suma_numeros <=15):
        return lista[1]
    else:
        return lista[0]
print(devolver_distintos(4, 3, 1))


