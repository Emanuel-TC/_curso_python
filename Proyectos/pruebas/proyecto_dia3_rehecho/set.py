# se crea por lo reguar con mi_set = {}, o mi_set = set()
# tiene elementos únicos, no se pueden repetir
# se pueden agregar elementos
# se pueden eliminar elementos
# se pueden buscar elementos
# se pueden recorrer
# se pueden hacer operaciones de conjuntos
mi_set = {1,2,3,4,5} 
print(type(mi_set))
# no tiene un orden específico
mi_set = {1,1,1,1,3,3,3,2,1,4,5}
print(mi_set)
# no se pueden meter listas, diccionarios, pero tuplas sí
for i in mi_set:
    print(i)

mi_set_strings = {'hola', 'mundo', 'hola', 'mundo', 'hola', 'mundo'}
print(mi_set_strings)
print('hola' in mi_set_strings)
print('adios' in mi_set_strings)