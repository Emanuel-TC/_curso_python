numero_menor = min(15,30,4,56)
numero_mayor = max(15,30,4,56)
print(f"El numero menor es: {numero_menor}")
print(f"El numero mayor es: {numero_mayor}")
#se puede realizar en una lista:
lista_numeros = [15,30,4,56]
print(f"El numero mayor de la lista {lista_numeros} es: {max(lista_numeros)} y el menor es: {min(lista_numeros)}")

#en una lista de string se maxima o minimza alfabéticamente:
nombres = ['Juan','Pedro','Jesus']
print(f"En la lista {nombres}, alfabéticamente va primero: {min(nombres)}, y al final {max(nombres)}")