mi_bool = 4 < 5 < 6
print(mi_bool)

mi_bool = (4 < 5) and (5 > 6)
print(mi_bool)

mi_bool = (4 < 5) or (5 > 6)
print(mi_bool)

mi_bool = (5 <= 5) or ("Perro" == "Perro")
print(mi_bool)

mi_bool = (5 <= 5) and ("Perro" == "Perro")
print(mi_bool)

frase = "Hola, ¿cómo estás?"
mi_bool = ("Hola" in frase) or ("Hello" in frase)
print(mi_bool)

mi_bool = ("Hola" in frase) and ("Hello" in frase)
print(mi_bool)

mi_bool = 'a' == 'a'
print(mi_bool)

mi_bool = not ('a' == 'a')
print(mi_bool)

mi_bool = not ('a' != 'a')
print(mi_bool)