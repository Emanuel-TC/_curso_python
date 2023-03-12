class CD:
    def __init__(self, nombre,autor,canciones):
        self.nombre = nombre
        self.autor = autor
        self.canciones = canciones

    #modificamos métodos especiales como:
    def __str__(self):
        return f"Nombre: {self.nombre} \nAutor: {self.autor}"
    #y podemos hacerlo con cualquier otro, por ejemplo:
    def __len__(self):
        return self.canciones
    def __del__(self):
        print(f"Se ha sido eliminado el objeto")


mi_cd = CD('Mario', 'Mario R',23)
print(mi_cd)
print(len(mi_cd))

del mi_cd


#esto sólo aplica para la clase que se está modificando el método, por ejemplo, en otro caso externo
mi_lista = [numero for numero in range(10)]
print(len(mi_lista))

'''
Práctica Métodos Especiales 1
Dada la clase Libro, implementa el método especial __str__ para que 
cada vez que se imprima el objeto, devuelva '"{titulo}", de {autor}' (atención: 
el título debe estar encerrado entre comillas dobles).
'''

class Libro:
    def __init__(self, titulo, autor,cantidad_paginas):
        self.titulo = titulo
        self.autor = autor
        self.cantidad_paginas = cantidad_paginas

    def __str__(self):
        return f'"{self.titulo}", de {self.autor}'

    def __len__(self):
        return self.cantidad_paginas

    def __del__(self):
        print("Libro eliminado")

mi_libro = Libro('Moby-Dick','Herman Melville',2000)
print(mi_libro)


'''
Práctica Métodos Especiales 2
Dada la clase Libro, implementa el método especial __len__ para que cada vez 
que se ejecute la función len() sobre el mismo, devuelva el número de páginas como número entero.
'''
print(len(mi_libro))
'''
Práctica Métodos Especiales 3
Dada la clase Libro, implementa el método especial __del__ para que el usuario 
sea informado con el mensaje "Libro eliminado", mostrándolo en pantalla cada vez que 
el libro se elimine.
'''
del mi_libro
