"""
Entendiendo el concepto de las funciones como objeto
"""

def cambiar_letras(tipo):

    """En esta función recibimos un tipo de opción, may para mayúsculas
    o min para minúsculas. A partir de eso, devolvemos la función seleccionada y se almcenará en una variable
    para ser usada
    """
    def minusculas(texto):
        print(texto.lower())

    def mayusculas(texto):
        print(texto.upper())

    if tipo == "may":
        return mayusculas  # se regresa como variable sin los () pafra usarse después

    elif tipo == "min":
        return minusculas  # se regresa como variable sin los () pafra usarse después


operacion = cambiar_letras("may")
operacion("Texto en mayusculas")

def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")
    return otra_funcion

# Podemos usar la función decoradora simplemente poniendo el @ y el nombre de la funicón sobre la función a decorar
#@decorar_saludo
def mayusculas(texto):
    print(texto.upper())


#@decorar_saludo
def minusculas(texto):
    print(texto.lower())
#para poder usar los decoradores cuando querramos se asigna la función como argumento
mayusculas_decoradas = decorar_saludo(mayusculas)
minusculas_decoradas = decorar_saludo(minusculas)

minusculas("PALabra\n")
mayusculas_decoradas("PALabra")