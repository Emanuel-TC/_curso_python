import timeit


declaracion_prueba_for = "prueba_uno(10)"
setup_prueba_for = '''
def prueba_uno(numero):
    lista = []
    for i in range(1,numero+1):
        lista.append(i)
    return lista
                    '''

declaracion_prueba_while = "prueba_dos(10)"
setup_prueba_while = ''' 
def prueba_dos(numero):
    lista = []
    i = 1
    while i <= numero:
        lista.append(i)
        i += 1
    return lista
'''

declaracion_prueba_lista_com = "prueba_tres(10)"
setup_prueba_lista_com = '''
def prueba_tres(numero):
    lista = [i for i in range(1,numero+1)]
    return lista
'''

prueba_uno = timeit.timeit(declaracion_prueba_for, setup_prueba_for, number=1000000)
prueba_dos = timeit.timeit(declaracion_prueba_while, setup_prueba_while, number=1000000)
prueba_tres = timeit.timeit(declaracion_prueba_lista_com,setup_prueba_lista_com, number=1000000)
print(f"La Prueba uno tardó: {prueba_uno} segundos")
print(f"La Prueba dos tardó: {prueba_dos} segundos")
print(f"La Prueba tres tardó: {prueba_tres} segundos")
