import os
from pathlib import Path
import shutil
import send2trash
'''archivo = open("archivo.txt", "w")
archivo.write("Hola mundo")
archivo.close()'''

#mueve archivos a un directorio
#shutil.move("archivo.txt", "/home/emanuel/Escritorio")
#no ejecutes el siguiente comando si no estás seguro de que no quieres volver a recuperar el archivo o
#directorios, mejor usa send2trash
#shutil.rmtree("/home/emanuel/Esscritorio")

#send2trash.send2trash("archivo.txt")
#para recorrer cada elementos de una ruta hacemos

# Ruta local usuario
ruta_local = Path(Path.home(),"Recetas")
ruta = os.walk(ruta_local)

for carpeta, subcarpetas, archivos in ruta:
    print(f"En la carpeta {carpeta}")
    if len(subcarpetas) > 0:
        print(f"Las subcarpetas son:")
        for subcarpeta in subcarpetas:
            print(f"\t{subcarpeta}")
    else:
        print(f"No hay subcarpetas en la carpeta {carpeta}")
    if len(archivos) > 0:
        print(f"Los archivos son:")
        for archivo in archivos:
            print(f"\t{archivo}")
        print("Los archivos que empiezan con 'E' son:")
        for archivo in archivos:
            if archivo.startswith("E"):
                print(f"\t{archivo}")
    else:
        print(f"No hay archivos en esta carpeta")
    print("\n")
