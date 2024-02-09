from pathlib import Path
import os, re, time, math
from datetime import datetime


def leer_archivo(archivo):
    mi_archivo = open(archivo,"r")
    texto = mi_archivo.read()
    mi_archivo.close()
    return texto


def buscar_coincidencias(texto):
    patron = r'N{1}\D{3}-\d{5}'
    if re.findall(patron, texto):
        coindicencias = re.findall(patron,texto)
        return coindicencias
    else:
        return False


def imprimir_resultados(coincidencias,nombre_archivo):
    for coincidencia in coincidencias:
        print(f"{nombre_archivo}\t{coincidencia}")


tiempo_inicio = time.time()
ruta_local = Path("Mi_Gran_Directorio")
ruta = os.walk(ruta_local)
fecha_hoy = datetime.now()
total_recultados = 0

print("-" * 50)
print(f"Fecha de búsqueda: [{fecha_hoy}]")
print('''\nARCHIVO\t\t\tNRO. SERIE
--------\t\t----------''')
for carpeta, subcarpetas, archivos in ruta:
    if len(archivos) > 0:
        for archivo in archivos:
            contenido = leer_archivo(Path(carpeta, archivo))
            coincidencias = buscar_coincidencias(contenido)
            if coincidencias != False:
                total_recultados += len(coincidencias)
                imprimir_resultados(coincidencias,archivo)
            else:
                pass
                #print(f"En el archivo {archivo} no hay coincidencias")
print(f"\nNúmeros encontrados {total_recultados}")
tiempo_final = time.time()
tiempo = math.ceil(tiempo_final-tiempo_inicio)
if tiempo != 1:
    print(f"El tiempo de ejecución fue de {tiempo} segundos")
else:
    print(f"El tiempo de ejecución fue de {tiempo} segundo")