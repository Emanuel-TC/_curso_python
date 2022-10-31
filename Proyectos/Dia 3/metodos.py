texto = "Este es el texto de Emanuel"
resultado = texto.upper() #Mayusculas
print(resultado)
resultado = texto.lower() #minusculas
print(resultado)
resultado = texto.split() #Separado en una lista
print(resultado)
resultado = texto.split("t") #Separado en una lista entre cada "t" sin incluirla
print(resultado)
a = "Aprender"
b = "Pyton"
c = "es"
d = "genial"
resultado = " ".join([a,b,c,d]) #une los elementos de una lista en un string
print(resultado)

resultado = texto.find("Emanuel") #la diferencia con index es que si pones un elemento inexiste no devuelve error, sino un -1
print(resultado)

resultado = texto.replace("Emanuel","Heber") #reemplaza ja
print(resultado)

#Imprime el siguiente texto en mayúsculas, empleando el método específico de strings:
frase = "Especialmente en las comunicaciones electrónicas, la escritura enteramente en mayúsculas equivale a gritar."
print(frase.upper())

#Une la siguiente lista en un string, separando cada elemento con un espacio.
# Utiliza el método apropiado de listas/strings, y muestra en pantalla el resultado.
lista_palabras = ["La","legibilidad","cuenta."]
espacio = " ".join(lista_palabras)
print(espacio)

#Reemplaza en la siguiente frase:
#"Si la implementación es difícil de explicar, puede que sea una mala idea."
#los siguientes pares de palabras:
#"difícil" --> "fácil"
#"mala" --> "buena"
#y muestra en pantalla la frase con ambas palabras modificadas.

frase= "Si la implementación es difícil de explicar, puede que sea una mala idea."
frase= frase.replace("difícil","fácil")
frase= frase.replace("mala","buena")
print(frase)