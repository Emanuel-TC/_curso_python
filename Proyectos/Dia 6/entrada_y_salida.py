mi_archivo = open("prueba.txt")
print(f"Mira, este es mi archivo: \n{mi_archivo.read()}")
print(f"\nSi lo quiero abrir por linas sólo debes hacer lo siguiente: ")
mi_archivo.close()

mi_archivo = open("prueba.txt")
una_linea = mi_archivo.readline()
print(una_linea)
#si copias la variable anterior y la imprimes, te muestra la siguiente línea
#porque python lo lee desde donde lo dejó la última vez
print(f"Puedes eliminar el salto de linea que hace si haces lo siguiente:")
una_linea = mi_archivo.readline()
print(una_linea.rstrip())
print(una_linea) #devuelve una copia de la cadena anterior eliminando los espacios en blanco de más
una_linea = mi_archivo.readline()

mi_archivo.close() #se recomienda cerrar el archivo una vez que sehaya terminado de usar.

mi_archivo = open("prueba.txt")
contador = 1
for linea in mi_archivo:
    print(f"{contador}. Aquí dice: {linea}")
    contador += 1
mi_archivo.close()