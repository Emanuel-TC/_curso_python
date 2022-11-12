import os
"""
ruta = os.getcwd() #get current working directory
print(ruta)
print("Esa es la ruta actual")

ruta = os.chdir("C:\\Users\\Emanuel\\Desktop\\alternativa") #cambia de directorio
print("Acabo de cambiar de ruta")
archivo = open("texto.txt","r")
directorio = os.listdir()
print(f"Estos  son los archivos de mi directorio nuevo:\n {directorio}")

print(archivo.read())
archivo.close()
ruta = os.mkdir("C:\\Users\\Emanuel\\Desktop\\alternativa\\otra_carpeta") #cambia de directorio
ruta = os.chdir("C:\\Users\\Emanuel\\Desktop\\alternativa")
directorio = os.listdir()
print(f"Estos  son los archivos de mi directorio {directorio}") """
'''
ruta = "C:\\Users\\Emanuel\\Desktop\\_curso_python\\Proyectos\\Dia 6\\prueba.txt"
archivo = os.path.basename(ruta) #obtiene el nombre base de la ruta de arriba
print(archivo)
direccion = os.path.dirname(ruta) #obtiene el nombre de la dirección sin el último valor
print(direccion)
direccion_archvivo = os.path.split(ruta)
print(direccion_archvivo)

ruta = os.rmdir("C:\\Users\\Emanuel\\Desktop\\alternativa\\otra_carpeta") #borra la carpeta

'''
from pathlib import Path

carpeta = Path("C:/Users/Emanuel/Desktop/alternativa") / "texto.txt"
#archivo = carpeta

mi_archivo = open(carpeta, "r")
print(mi_archivo.read())