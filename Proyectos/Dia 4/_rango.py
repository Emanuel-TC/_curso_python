#los valores de range deben ser integers
for numero in range(5): #por defecto empieza en 0 y termina cuando se ha ejecutado las veces que se ha declarado
    print(numero)
for numero in range(1,5): #empieza en valor 1, se salta 0, pero lo cuenta como un valor ejecutado y termina un número antes del que se declaró al final
    print(numero)
for numero in range(1,5,2): #avanza en saltos de acuerdo al último valor aisgnado
    print(numero)
#range también sirve para incluir datos en una lista
lista = list(range(1,11)) #se hace un casting donde se almacenan en la lista los valores del range del 1 al 10 (al 11 no porque corta uno antes)
print(lista)
#Crea una lista formada por todos los números desde el 2500 al 2585 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(2500,2586))
#Utilizando la función range(), crea en una única linea de código una lista formada por todos los números
# múltiplos de 3 desde el 3 al 300 (inclusive). Almacena dicha lista en la variable mi_lista.
mi_lista = list(range(3,301,3))

#Utiliza la función range() y un loop para sumar los cuadrados de todos los números del 1 al 15 (inclusive).
# Almacena el resultado en una variable llamada suma_cuadrados.
#Para ello:
#Crea un rango de valores que puedas recorrer en un loop
#Para cada uno de estos valores, calcula su valor al cuadrado (potencia de 2). Puede que necesites crear variables intermedias (de manera opcional).
#Suma todos los valores al cuadrado obtenidos. Acumula la suma en la variable suma_cuadrados.

suma_cuadrados = 0
for numero in range(1,16):
    print(f"El cuadrado del numero {numero} es: {numero**2} ")
    suma_cuadrados += numero**2
    print(f"La suma hasta el momento es de: {suma_cuadrados}")