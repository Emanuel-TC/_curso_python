def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("Hola")
        funcion(palabra)
        print("Adiós")
    return otra_funcion

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