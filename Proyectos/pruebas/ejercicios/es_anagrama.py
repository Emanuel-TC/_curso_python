'''
Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 *  Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
'''
def es_anagrama(palabra_1, palabra_2):
    palabra_1_ordenada = [letra for letra in palabra_1].sort()
    palabra_2_ordenada = [letra for letra in palabra_2].sort()
    if palabra_1_ordenada == palabra_2_ordenada:
        print(f"Las palabras {palabra_1} y {palabra_2} son anagramas")
        return True
    else:
        return False
palabra_1 = input("Introduce la primer palabra: \n")
while True:
    palabra_2 = input("Introduce la segunda palabra: \n")
    if palabra_1.lower() == palabra_2.lower():
        print("Las palabras son iguales, no son anagramas, introduce una palabra diferente")
    else:
        break
print(es_anagrama(palabra_1, palabra_2))
