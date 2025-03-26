texto = input("Introduce un texto: \n")
letras = []
while len(letras)<3:
    letra = input(f"Introduce una letra: \n")
    if len(letra) > 1:
        print("Solo puedes introducir una letra, inténtalo de nuevo")
    else:
        letras.append(letra)
minusculas = [letra.lower() for letra in letras]
letras = minusculas
print(f"Las letras introducidas son: {letras}")
letra_1, letra_2, letra_3 = letras
texto = texto.lower()
print(f"La letra {letra_1} aparece {texto.count(letra_1)} veces")
print(f"La letra {letra_2} aparece {texto.count(letra_2)} veces")
print(f"La letra {letra_3} aparece {texto.count(letra_3)} veces")
texto_sin_comas_puntos = texto.replace(",", "").replace(".", "")
print(f"El texto tiene {len(texto_sin_comas_puntos.split())} palabras")
print(f"La primer letra del texto es {texto[0]}, y la última letra del texto es {texto_sin_comas_puntos[-1]}")
texto_inverso = texto.split()
texto_inverso.reverse()
texto_inverso = " ".join(texto_inverso)
print(f"El texto en orden inverso es: {texto_inverso}")
if "python" in texto:
    print(f"La palabra 'python' sí aparece en el texto")
else:
    print(f"La palabra 'python' no aparece en el texto")