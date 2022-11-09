'''def suma(**kwargs):
    #print(type(kwargs))
    total = 0
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")
        total += valor
    return total
print(suma(a=1, b=2, c=3, d=4)) '''

def prueba(num_uno,num_dos,*args,**kwargs):
    print(f"El primer valor es {num_uno}")
    print(f"El segundo valor es {num_dos}")
    for arg in args:
        print(f"arg = {arg}")
    for clave, valor in kwargs.items():
        print(f"{clave} = {valor}")

args =[1,2,3,4,5,6,7,8,9,10]
kwargs ={"a":1,"b":2,}

prueba(1,2,*args,**kwargs)

''' Ejercicio 1:
Crea una función llamada cantidad_atributos que cuente la cantidad de parémetros 
que se entregan, y devuelva esa cantidad como resultado.
'''
def cantidad_atributos(**kwargs):
    contador = 0
    for kwarg in kwargs:
        contador += 1
    return contador
print(cantidad_atributos(a=1, b=2, c=0))

''' Ejercicio 2:
Crea una función llamada lista_atributos que devuelva en forma de lista los valores de los atributos entregados 
en forma de palabras clave (keywords). La función debe preveer recibir cualquier cantidad de argumentos de este tipo.
'''
def lista_atributos(**kwargs):
    lista = []
    for clave, valor in kwargs.items():
        lista.append(valor)
    return lista
kwargs = {"a":1,"b":2,"c":3,"d":4}
print(lista_atributos(**kwargs))

''' Ejercicio 3:
    Crea una función llamada describir_persona, que tome como parámetros su nombre y luego una cantidad 
    indetermida de argumentos. Esta función deberá mostrar en pantalla:

Características de {nombre}:
{nombre_argumento}: {valor_argumento}
{nombre_argumento}: {valor_argumento}
etc...
Por ejemplo:

describir_persona("María", color_ojos="azules", color_pelo="rubio")

Mostrará en pantalla:

Características de María:
color_ojos: azules
color_pelo: rubio
    '''

def describir_persona(nombre, **kwargs):
    print(f"Características de {nombre}:")
    for clave, valor in kwargs.items():
        print(f"{clave} : {valor}")

describir_persona("María", color_ojos="azules", color_pelo="rubio")
