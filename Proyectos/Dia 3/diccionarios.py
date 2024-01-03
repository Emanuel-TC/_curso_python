# En  este archivo veremos el uso de los diccionarios
diccionario = {'c1':'valor1','c2':'valor2'} #compuesto por indice1:valor, indice2:valor2, etc
                                            # los índices no se repiten, los valores ´si
print(diccionario)

resultado = diccionario['c1'] #se busca el valor que está en esa clave o índice
print(resultado)

cliente = {'nombre':'Juan', 'apellido':'Fuentes', 'peso':88,'talla':1.76}
consulta = cliente['apellido']
print(consulta)
consulta = cliente['talla']
print(consulta)

diccionario = {'c1':55,'c2':[10,20,30],'c3':{'s1':100,'s2':200}} #contiene elementos sencillos, hasta listas, diccionarios
print(diccionario['c3'])
print(diccionario['c2'][1]) #podemos consultar el valor del índice de la lista dentro
print(diccionario['c3']['s2']) #podemos consultar el valor del índice o clave del diccionario dentro
diccionario = {'c1':['a','b','c'],'c2':['d','e','f']}
# Con esta línea imprimimos la letra e pero en mayúsucula
print(diccionario['c2'][1].upper())
# para añadir elementos al dic, se crea un nuevo índice, y se le asigna el valor
diccionario['c3'] = ['g','h','i']
print(diccionario)
# para reemplazar elementos al dic, se escoge el índice, y se le asigna el nuevo valor
diccionario['c3'] = ['j','k','l']
print(diccionario)
# se obtiene todas las claves del dic
print(diccionario.keys())

print(f"Los valores del diccionario son: {diccionario.values()}") #los valores del dic
print(f"Los elementos del dic son: {diccionario.items()}") #todos los elementos del dic

'''Práctica Diccionarios 1
Crea un diccionario llamado mi_dic que almacene la siguiente información de una persona:

nombre: Karen

apellido: Jurgens

edad: 35

ocupacion: Periodista

Los nombres de las claves y valores deben ser iguales a la consigna.'''
mi_dic = {'nombre':'Karen','apellido':'Jurgens','edad':35,'ocupacion':'Periodista'}


'''Crea una función print que devuelva del segundo item de la lista llamada points2, dentro del siguiente diccionario.
Si el valor 300 cambiara en el futuro, el código debería funcionar igual para devolver el valor que se encuentre en
esa misma posición. Para ello, deberás hacer referencia a los nombres de las claves y/o índices según corresponda.'''
mi_dict = {"valores_1":{"v1":3,"v2":6},"puntos":{"points1":9,"points2":[10,300,15]}}
print(mi_dict['puntos']['points2'][1])

'''Práctica Diccionarios 3
Actualiza la información de nuestro diccionario llamado mi_dic  (reasignando nuevos valores a las claves según corresponda), y agrega una nueva clave llamada "pais" (sin tilde). Los nuevos datos son:

nombre: Karen

apellido: Jurgens

edad: 36

ocupacion: Editora

pais: Colombia

para ello, no debes cambiar la línea de código ya escrita, sino actualizar los valores mediante métodos de diccionarios.
'''

mi_dic = {"nombre":"Karen", "apellido":"Jurgens", "edad":35, "ocupacion":"Periodista"}
mi_dic['edad'] = 36
mi_dic['ocupacion'] = 'Editora'
mi_dic['pais'] = 'Colombia'