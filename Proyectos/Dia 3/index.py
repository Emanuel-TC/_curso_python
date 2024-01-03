# En este archivo vamos a aprender a usar el método index
mi_texto = "Esta es una prueba"
resultado = mi_texto[5]
print(f"La leta en la posición 5, del texto '{mi_texto}' es: {resultado}, y la palabra 'prueba', comienza en la posición {mi_texto.index('prueba')}")

'''Práctica Método Index() 1
Encuentra y muestra en pantalla qué caracter ocupa la quinta posición dentro de la siguiente palabra: "ordenador"'''
palabra = "ordenador"
resultado = palabra[4]
print(resultado)

'''Práctica Método Index() 2
Encuentra y muestra en pantalla el índice de la primera aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."'''

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.index("práctica")
print(resultado)

'''Práctica Método Index() 3
Encuentra y muestra en pantalla el índice de la última aparición de la palabra "práctica" en la siguiente frase:

"En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."'''

frase = "En teoría, la teoría y la práctica son los mismos. En la práctica, no lo son."
resultado = frase.rindex("práctica")
print(resultado)