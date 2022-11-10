''' Ejercicio 3:
Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
'''

def dos_ceros_repetidos(*args):
    contador = 0
    for numero in args:
        if numero == 0:
            contador += 1
            if contador == 2:
                return True
        else:
            contador = 0
    return False


print(dos_ceros_repetidos(0,5,6,1,0,8,9,10,11,12,15,16,18,1,2,2,2,0,0,9,3,5,0))
print(dos_ceros_repetidos(6,0,5,1,0,3,0,1))


