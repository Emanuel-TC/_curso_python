texto = "ABCDEFGHIJKLM"
fragmento = texto[2:10]
print(fragmento)
fragmento = texto[2:10:2]
print(fragmento)
fragmento = texto[::2]
print(fragmento)
fragmento = texto[::-2]
print(fragmento)

#Extrae la primera palabra de la siguiente frase utilizando slicing, y muéstrala en pantalla:
#"Controlar la complejidad es la esencia de la programación"
#Pista: "Controlar" tiene un largo de 9 caracteres.

frase = "Controlar la complejidad es la esencia de la programación"
fragmento = frase[:9]
print(fragmento)

#Toma cada tercer caracter empezando desde el noveno hasta el final de la frase, e imprime el resultado.
#"Nunca confíes en un ordenador que no puedas lanzar por una ventana"

frase = "Nunca confíes en un ordenador que no puedas lanzar por una ventana"
frase = frase[8::3]
print(frase)

#Invierte la posición de todos los caracteres de la siguiente frase y muestra el resultado en pantalla.
#"Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = "Es genial trabajar con ordenadores. No discuten, lo recuerdan todo y no se beben tu cerveza"
frase = frase[::-1]
print(frase)