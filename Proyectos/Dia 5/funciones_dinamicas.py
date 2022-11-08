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
