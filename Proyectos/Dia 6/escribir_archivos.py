# En este ejercicio vamos a ver los modos de apertura del método open
# r para sólo lectura
archivo = open("prueba.txt","r")
primer_linea = archivo.readline()
print(primer_linea)
archivo.close()
# w para re-escribir sobre el archivo
archivo = open("prueba_1.txt","w")
archivo.write("Soy el nuevo archivo\n")
lista_palabras = ["Hola","mundo","aquí","estoy"]
for palabra in lista_palabras:
    archivo.write(palabra+"\n")
archivo.close()
# a para añadir al final del texto un elemento
archivo = open("prueba_1.txt","a")
archivo.write("Soy la linea final\n")
archivo.close()

# Ejercicios
'''Práctica Crear y Escribir Archivos 1
Abre el archivo llamado "mi_archivo.txt", y cambia su contenido por el texto "Nuevo texto".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.'''

archivo = open("mi_archivo.txt","w")
archivo.write("Nuevo texto")
archivo.close()
archivo = open("mi_archivo.txt","r")
print(archivo.read())
archivo.close()

'''Práctica Crear y Escribir Archivos 2
Abre el archivo llamado "mi_archivo.txt", y añade una línea al final del mismo que diga: "Nuevo inicio de sesión".

Imprime el contenido completo de "mi_archivo.txt" al finalizar.

Pista: deberás cerrarlo en modo escritura y volverlo a abrir en modo lectura.'''

archivo = open("mi_archivo.txt","a")
archivo.write("Nuevo inicio de sesión")
archivo.close()
archivo = open("mi_archivo.txt","r")
print(archivo.read())
archivo.close()

'''
Práctica Crear y Escribir Archivos 3
Utiliza el método writelines para escribir los valores de la siguiente lista al final del archivo "registro.txt" . Inserta un tabulador entre cada elemento de la lista para separarlos.

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

Imprime el contenido completo de "registro.txt" al finalizar.

Pista: recuerda que el símbolo para concatenar un tabulador en un string es \t. También, deberás cerrar el archivo en modo escritura y volverlo a abrir en modo lectura para poder imprimir su contenido.'''

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]
archivo = open("registro.txt","a")
for palabra in registro_ultima_sesion:
    archivo.writelines(palabra+"\t")
archivo.close()
archivo = open("registro.txt","r")
print(archivo.read())
archivo.close()