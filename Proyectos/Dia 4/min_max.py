numero_menor = min(15,30,4,56)
numero_mayor = max(15,30,4,56)
print(f"El numero menor es: {numero_menor}")
print(f"El numero mayor es: {numero_mayor}")
#se puede realizar en una lista:
lista_numeros = [15,30,4,56]
print(f"El numero mayor de la lista {lista_numeros} es: {max(lista_numeros)} y el menor es: {min(lista_numeros)}")

#en una lista de string se maxima o minimza alfabéticamente:
nombres = ['Juan','Pedro','Jesus','Zoe','María']
# Podemos hacer una correción para ordenar alfabéticamente
#print(f"En la lista {nombres}, alfabéticamente va primero: {min(nombres)}, y al final {max(nombres)}")
nombres_ordenados = []
i=0
while len(nombres) > 0:
    for nombre in nombres:
        nombres_ordenados.append(min(nombres))
        i +=1
        print(f"El nombre número {i} es {nombres_ordenados[-1]}")
        #print(nombres_ordenados)
        indice = nombres.index(min(nombres))
        nombres.pop(indice)

diccionario_edades = {"Carlos":55, "María":42, "Mabel":78, "José":44, "Lucas":24, "Rocío":35, "Sebastián":19, "Catalina":2,"Darío":49}
edad_minima = min(diccionario_edades.values())
ultimo_nombre = max(diccionario_edades.keys())
print(edad_minima)