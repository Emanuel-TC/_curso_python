import os
import re
from pathlib import Path
from datetime import date
import time
import math

ruta = os.walk('/home/emanuel/PycharmProjects/_curso_python_git/Proyectos/Dia 9/proyecto_dia_nueve/Mi_Gran_Directorio')
diccionario_coincidencias = {}

def lee_archivo(archivo):
    cadena = ''
    mi_archivo = open(archivo, 'r')
    for linea in mi_archivo:
        cadena += linea
    return cadena,archivo
def busca_coincidencia(cadena):
    patron = r'N[A-Za-z]{3}-\d{5}'
    if re.search(patron, cadena):
        return re.search(patron, cadena).group()
    else:
        return False

def comienza_busqueda():
    for carpeta, subcarpetas, archivos in ruta:
        if len(subcarpetas) > 0:
            for subcarpeta in subcarpetas:
                pass
        else:
            pass
        if len(archivos) > 0:
            for archivo in archivos:
                ruta_archivo = Path(carpeta,archivo)
                cadena_leida, nombre_archivo = lee_archivo(ruta_archivo)
                resultado_busqueda = busca_coincidencia(cadena_leida)
                if resultado_busqueda != False:
                    diccionario_coincidencias[archivo] = resultado_busqueda
                else:
                    pass
        else:
            pass
    return diccionario_coincidencias
inicio = time.time()
comienza_busqueda()
fin = time.time()
tiempo_de_ejecucion = fin - inicio

def inicio():
    fecha_hoy = date.today()
    contador = 0
    print("------------------------------")
    print(f"Fecha de busqueda: [{fecha_hoy.day}/{fecha_hoy.month}/{fecha_hoy.year}]\n")
    print("ARCHIVO\t\t\tNRO. SERIE\n-------\t\t\t----------")
    for clave, item in diccionario_coincidencias.items():
        print(f"{clave}\t{item}")
        contador += 1
    print(f"\nNúmeros encontrados: {contador}")
    print(f"Duración de la busqueda: {math.ceil(tiempo_de_ejecucion)} segundo(s)")
    print("-------------------------------------")


inicio()