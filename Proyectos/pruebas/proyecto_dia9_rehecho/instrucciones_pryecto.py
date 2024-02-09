import shutil

# Variables para descomprimir archivo
ruta_archivo_zip, nombre_archivo = "Proyecto+Dia+9.zip", "Instrucciones"

# código para descomprimir archivos
shutil.unpack_archive(ruta_archivo_zip,nombre_archivo,'zip')