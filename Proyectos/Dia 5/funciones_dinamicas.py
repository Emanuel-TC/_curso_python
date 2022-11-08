def revisar_tres_cifras(numero):
    #corroboramos que un numero se encuentre en el rango de 100 hasta 999, el 1000 no lo incluye
    return numero in range(100,1000)

resultado = revisar_tres_cifras(358)
print(resultado)
suma = 65 + 23
resultado = revisar_tres_cifras(suma)
print(resultado)

def revisar_tres_numeros(lista):
    #mediante este ciclo va a corroborar dentro de una listaque esté un numero en el rango de 100 a 999
    for numero in lista:
        if numero in range(100,1000):
            return True
        else:
            #si no lo está en la primera o n -1 revisión, pasa hasta terminar con la revisión n
            pass
    #fuera del ciclo devuelve False si nunca lo encontró en el ciclo
    return False
resultado = revisar_tres_numeros([10,20,5000])
print(resultado)
def revisa_3_numeros(lista):
    #creamos una lista vacía
    lista_tres_cifras = []
    for numero in lista:
        #si numero esta en el rango de 100 a 999
        if numero in range(100,1000):
            #agrega a la lista vacía el numero que sí está en el rango
            lista_tres_cifras.append(numero)
        else:
            #si no,  pasa al siguiente numero y despues termina el ciclo
            pass
        #devuelve la lista que estaba vacía con los numero que sí estan el rango
        #si no hay ningún numero en el rango devuelve una lista vacía
    return lista_tres_cifras

resultado = revisa_3_numeros([10,200,500])
print(resultado)

''' Ejercicio 1:
    Crea una función (todos_positivos) que reciba una lista de números como parámetro, y devuelva True si todos los 
    valores de una lista son positivos, y False si al menos uno de los valores es negativo. Crea una lista llamada 
    lista_numeros con valores positivos y negativos.

No invoques la función, solo es necesario definirla.
'''
def todos_positivos(lista_numeros):
    for numero in lista_numeros:
        if numero < 0:
            return False
        else:
            pass
    return True
lista_numeros = [1,2,3,4,5,6,7,8,9,-1]

resultado = todos_positivos(lista_numeros)
print(resultado)

''' Ejercicio 2:
Crea una función (suma_menores) que sume los números de una lista (almacenada en la variable lista_numeros) 
siempre y cuando sean mayores a 0 y menores a 1000, y devuelva el resultado de dicha suma.
    '''
def suma_menores(lista_numeros):
    suma = 0
    for numero in lista_numeros:
        if numero in range(1,1000):
            suma += numero
        else:
            pass
    return suma
lista_numeros = [1,2,3,10000,-3]

resultado = suma_menores(lista_numeros)
print(resultado)

''' Ejercicio 3:
    Crea una función (cantidad_pares) que cuente la cantidad de números pares que existen 
    en una lista (lista_numeros), y devuelva el resultado de dicha cuenta.
    '''
def cantidad_pares(lista_numeros):
    cuenta = 0
    for numero in lista_numeros:
        if numero % 2 == 0:
            cuenta += 1
        else:
            pass
    return cuenta
lista_numeros = [1,2,3,4,5,6,7]
resultado = cantidad_pares(lista_numeros)
print(resultado)
