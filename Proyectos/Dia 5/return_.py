def multiplicar(numero1,numero2):
    return numero1 * numero2

#hay varias formas de usar la función, asignando el return a una variable
resultado = multiplicar(3,3)
# o bien, imprimiendo directamente:
print(multiplicar(3,3))
#imprimiendo después la variable para tener un mejor control de su valor
print(f"Aquí imprimo el return que se guarda en la variable resultado {resultado}")

#también podemos definir la función de una forma distinta:
def multiplicar_dos_numeros(numero1,numero2):
    total = numero1 * numero2
    return total

resultado = multiplicar_dos_numeros(40,2)
print(resultado)

''' Ejercicio 1:
    Crea una función llamada potencia que tome dos valores numéricos como argumentos. 
    Deberá devolver el número que resulte de resolver una potencia, utilizando el primer número como base, 
    y el segundo como exponente:
    '''
def potencia(base,exponente):
    return base ** exponente

resultado = potencia(10,2)
print(resultado)

''' Ejercicio 2:
    Crea una función llamada usd_a_eur que tome como único parámetro un valor numérico 
    (un monto en dólares estadounidenses), y devuelva como resultado el monto equivalente en euros. 
    A fines de este ejemplo, tomaremos la conversión 1 USD = 0.90 EUR.

    Crea una variable llamada dolares y almacena en ella un monto cualquiera para entregárselo a tu función 
    y evaluar su resultado.
    '''
def usd_a_eur(dolares):
    return dolares * 0.9
dolares = 10

''' Ejercicio 3:
    Crea una función llamada invertir_palabra que tome los caracteres de una palabra dada como argumento, 
    invierta el orden de sus caracteres y los devuelva de ese modo y en mayúsculas.

Por ejemplo, si le proporcionamos la palabra "Python", deberá devolver: "NOHTYP"
También, deberás crear una variable llamada palabra, que contenga el string que tú prefieras, 
para sumisitrarle como argumento a la función creada.
'''
def invertir_palabra(palabra):
    palabra = palabra[::-1]
    return palabra.upper()

resultado = invertir_palabra("Python")
print(resultado)

