'''
Crea una función llamada abrir_leer() que abra (open) un archivo
indicado como parámetro, y devuelva su contenido (read).
'''

def abrir_leer(archivo):
    mi_archivo = open(archivo, 'r')
    datos = mi_archivo.read()
    mi_archivo.close()
    return datos

print(abrir_leer('prueba.txt'))

''' 
Crea una función llamada sobrescribir() que abra (open) un archivo indicado como parámetro, 
y sobrescriba cualquier contenido anterior por el texto "contenido eliminado"
'''

def sobrescribir(archivo,texto):
    mi_archivo = open(archivo, 'w')
    mi_archivo.write(texto)
    mi_archivo.close()

print(abrir_leer("prueba_1.txt"))

sobrescribir('prueba_1.txt',"contenido eliminado")

print(abrir_leer('prueba_1.txt'))

'''
Crea una función llamada registro_error() que abra (open) un archivo indicado como parámetro, 
y lo actualice añadiendo una línea al final que indique "se ha registrado un error de ejecución". 
Finalmente, debe cerrar el archivo abierto.
'''

def registro_error(archivo,texto):
    mi_archivo = open(archivo, 'a')
    mi_archivo.write(texto)
    mi_archivo.close()

registro_error('prueba_1.txt','\nse ha registrado un error')

print(abrir_leer('prueba_1.txt'))

