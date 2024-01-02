# En este archivo veremos la dos formas en las que se usan las cadenas formateadas
# La forma antigua, con la función 'format'
x = 10
y = 2
# Usamos llaves que serán sustituidas por el orden en el que aparecen las variables en la función format
print("La suma de {} y {} es {}".format(x,y,x+y))

color = "Rojo"
matricula = 123456
# Usando la forma nueva, y la más comprensible, sólo es necesario usar una letra f antes de las comillas de la función print, y ente llaves la variables
print(f"El auto es {color} y su matricula es {matricula}")
'''Práctica Formatear Cadenas 1
Necesitamos imprimir el nombre y número de asociado dentro de la siguiente frase:

Estimado/a (nombre_asociado), su número de asociado es: (numero_asociado)'''
nombre_asociado = "Jesse Pinkman"
numero_asociado = 399058
print(f"Estimado/a {nombre_asociado}, su número de asociado es: {numero_asociado}")

'''Práctica Formatear Cadenas 2
Muestra al usuario la cantidad de puntos acumulados dentro de la siguiente frase:

Has ganado (puntos_nuevos) puntos! En total, acumulas (puntos_totales) puntos'''
puntos_nuevos = 350
puntos_totales = 1225
print(f"Has ganado {puntos_nuevos} puntos! En total, acumulas {puntos_totales} puntos")
