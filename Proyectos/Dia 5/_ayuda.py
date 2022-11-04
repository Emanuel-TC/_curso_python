diccionario = {'clave_1': 500, 'clave_2': 200, 'clave_3': 300, 'clave_4': 400}
resultado = diccionario.popitem()
print(resultado)
print(diccionario)

#Remueve los caracteres a la izquierda de nuestro texto principal:
# ,
# :
# %
# _ #

#Utiliza el método lstrip(). Imprime el resultado en pantalla:
#lstrip retorna una copia de la cadena pero sin los caracteres que se pueden combinar en la
#especificacion que se hizo dentro de comillas y parentesis
cadena = ",:_#,,,,,,:::____##Pyt%on_ _Total,,,,,,::#"
print(cadena)
print(cadena.lstrip(',:%_#'))

#Añade el elemento "naranja" como el cuarto elemento de la siguiente lista "frutas", utilizando
#el método insert():
#frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
#Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa
# y cómo es su funcionamiento.

frutas = ["mango", "banana", "cereza", "ciruela", "pomelo"]
print(frutas)
frutas.insert(3,"naranja") # inserta un objeto en el índice donde se indica, por ejemplo, pusimos el índice 3
                           # se recorren los que van después
print(frutas)

#Verifica si los sets a continuación forman conjuntos aislados (es decir, que no tienen elementos en común),
#utilizando el método isdisjoint(). Almacena dicho resultado en la variable conjuntos_aislados:
#marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
#marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
#Busca en la documentación acerca del funcionamiento del método solicitado para saber cómo actúa y cómo es su funcionamiento.
marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips", "Samsung", "LG"}
respuesta = marcas_tv.isdisjoint(marcas_smartphones) #devuelve un booleano, false si existe al menos, un elemento que coincide
                                                     #verdadero si no hay ningún elemento que coincida
print(respuesta)

marcas_smartphones = {"Samsung", "Xiaomi", "Apple", "Huawei", "LG"}
marcas_tv = {"Sony", "Philips"} #al borrar los ementos que coinciden, cambia a true
respuesta = marcas_tv.isdisjoint(marcas_smartphones)
print(respuesta)

