'''
Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']
'''
def palabra_sin_letras_repetidas_en_orden(palabra):
    palabra = palabra.lower()
    lista = list(palabra)
    mi_set = set(lista)
    lista = list(mi_set)
    lista = sorted(lista)
    return lista
print(palabra_sin_letras_repetidas_en_orden("Entretenido"))
