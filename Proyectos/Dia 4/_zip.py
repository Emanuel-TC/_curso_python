nombres = ['Ana', 'Hugo', 'Valeria']
edades = [65,29,42,26] #en este caso, vemos que es más largo, pero zip toma el más corto y los une a esa medida
#zip integra en un tuple un valor de la lista con otro valor de la otra lista
ciudades = ['Lima', 'Madrid', 'Mexico'] #también es posible agregar más listas al tuple
combinados = zip(nombres,edades,ciudades)
print(combinados)

#no aparece nada, pero se debe hacer un casting de la siguiente forma:
combinados = list(zip(nombres,edades,ciudades))
print(combinados)

print("Prueba con loop for: ")
for nombre, edad, ciudad in combinados:
    print(f"{nombre} tiene {edad} años de edad, y vive en {ciudad} ")

#Muestra en pantalla frases como la del siguiente ejemplo:

#La capital de Alemania es Berlín
#Utiliza la función zip, loops, y las siguientes listas de países y capitales para resolverlo rápida y eficientemente.
#
#capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
#paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]

capitales = ["Berlín", "Tokio", "París", "Helsinki", "Ottawa", "Canberra"]
paises = ["Alemania", "Japón", "Francia", "Finlandia", "Canadá", "Australia"]
capital_pais = list(zip(capitales, paises))
for capital,pais in capital_pais:
    print(f"La capital de {pais} es {capital}")

#Crea un objeto zip formado a partir de listas, de un conjunto de marcas
# y productos que tú prefieras, dentro de la variable mi_zip.
marcas = ['Apple', 'Tesla']
productos = ['IPhone','Auto electrico']

mi_zip = list(zip(marcas,productos))
for marca, producto in mi_zip:
    print(f"Lo más distintivo de {marca} es el {producto}")

#Crea el zip con las traducciones los números del 1 al 5 en español,
# portugués e inglés (en el mismo orden), y convierte el objeto generado en
# una lista almacenada en la variable numeros:
#uno / um / one
#dos / dois / two
#tres / três / three
#cuatro / quatro / four
#cinco / cinco / five
#El resultado deberá seguir la estructura:
#[('uno', 'um', 'one'), ('dos', 'dois', 'two'), ... ]
espaniol = ['uno', 'dos','tres','cuatro','cinco']
portugues = ['um','dois','três','quatro','cinco']
ingles = ['one','two','three','four','five']
numeros = list(zip(espaniol,portugues,ingles))
print(numeros)
for es,po,en in numeros:
    print(f"El 1 en español es {es}, en portugués es {po}, y en inglés es: {en}")