# match es la incorporación de case a python, sin embargo, aunque se podía hacer algo parecido con if y else
# en match se puede dar el siguiente uso:
cliente = {"nombre": "Emanuel",
           "edad": 22,
           "ocupacion": "Estudiante"}
pelicula = {"titulo": "Matrix",
            "ficha_tecnica": {"protagonista": "Keanu Reeves",
                              "director": "Lana y Lilly Wachownsky"}
            }
lista_compras = ["Pollo", "Huevos","Leche"]
elementos = [cliente,pelicula,lista_compras,"libro"]

for elemento in elementos:
    match elemento:
        # En el caso que la estructura de mi diccionario sea esta
        case {"nombre": nombre, "edad": edad, "ocupacion": ocupacion}:
            # hace match y podemos usar ese elemento de la lista
            print("Es un cliente")
            print(f"El cliente {nombre} tiene {edad} años de edad y es {ocupacion}")
            # en el caso que la estructura de mi elemento, sea este diccionario, lo imprime
        case {"titulo": titulo, "ficha_tecnica": {"protagonista": protagonista, "director": director}}:
            print("Es una pelicula")
            print(f"La pelicula {titulo} tiene como protagonista a {protagonista}, y su director es {director}")
        case [elemento1,elemento2,elemento3]:
            print("Es una lista")
            print(elemento)
        case _: #case _: es el índicado cuando no encuentra una coicidencia con el valor
            print("No se qué es")