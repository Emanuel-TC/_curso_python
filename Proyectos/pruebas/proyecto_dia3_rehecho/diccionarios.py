# Ahora vamos a usar un diccionario
diccionario = {'c1': 'valor1',
                'c2': 'valor1',
                'c3': 'valor3'}
# print(diccionario['c1'])
# Un diccionarioo puede tener cualquier tipo de dato, incluso otro diccionario

clientes = {    'cliente1': {
                            'nombre': 'Juan',
                            'apellido': 'Perez',
                            'dni': '12345678',
                            'edad': 30
                        },
                'cliente2':{
                            'nombre': 'Ana',
                            'apellido': 'Gomez',
                            'dni': '87654321',
                            'edad': 25
                            }
}
print(f"El cliente {clientes['cliente1']['nombre']} {clientes['cliente1']['apellido']} tiene {clientes['cliente1']['edad']} años")
print(f"El cliente {clientes['cliente2']['nombre']} {clientes['cliente2']['apellido']} tiene {clientes['cliente2']['edad']} años")

dic = { 'c1:': ['a', 'b', 'c'],
        'c2': ['d', 'e', 'f']
}
print(dic['c2'][1].upper())
