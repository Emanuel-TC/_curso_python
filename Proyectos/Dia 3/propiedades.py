poema = """Mil pequeños peces blancos
como si hiviera
el color del agua"""
print(poema)
print("agua" in poema) #si existe esa palabra en la variable que contiene esa string
poema = len(poema) #su longitud en caracteres
print(f"La longitud de este poema es de {poema} caracteres")

#Concatena 15 veces el texto "Repetición" y muestra el resultado en pantalla.
#Por suerte, conoces que los strings son multiplicables y puedes realizar esta actividad
# de forma simple y elegante.
texto = "Repetición"
print(texto*15)

#Verifica si la palabra "agua" no se encuentra en el siguiente haiku. Debes imprimir el booleano.
#Tierra mojada,
#mis recuerdos de viaje
#entre las lluvias

poema ="""Tierra mojada
mis recuerdos de viaje,
entre las lluvias"""
print("agua" not in poema)
palabras = list(poema.split())
print(len(palabras))


#Muestra en pantalla el largo (en números de caracteres) de la palabra electroencefalografista.
palabra = "electroencefalografista"
print(len(palabra))