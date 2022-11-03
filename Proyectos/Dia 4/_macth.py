#match es la incorporación de case a python, sin embargo, aunque se podía hacer algo parecido con if y else
#en match se puede dar el siguiente uso:
cliente = {"nombre":"Emanuel", "edad":22,"ocupacion":"Estudiante"}
pelicula = {"titulo":"Matrix", "ficha_tecnica":{"protagonista":"Keanu Reeves","director": "Lana y Lilly Wachownsky"}}
elementos = [cliente,pelicula,"libro"]

for elemento in elementos:
    match elemento:
        case {"nombre":nombre, "edad":edad, "ocupacion":ocupacion}:
            print("Es un cliente")
            print(f"El cliente {nombre} tiene {edad} años de edad y es {ocupacion}")
        case {"titulo":titulo, "ficha_tecnica":{"protagonista":protagonista, "director":director}}:
            print("Es una pelicula")
            print(f"La pelicula {titulo} tiene como protagonista a {protagonista}, y su director es {director}")
        case _: #case _: es el índicado cuando no encuentra una coicidencia con el valor
            print("No se qué es")