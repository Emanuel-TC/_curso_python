#import zipfile
'''mi_zip = zipfile.ZipFile("mi_archivo_comprimido.zip", "w")
mi_zip.write('mi_texto_A.txt')
mi_zip.write('mi_texto_B.txt')
mi_zip.close()'''
'''mi_zip = zipfile.ZipFile("mi_archivo_comprimido.zip", "r")
mi_zip.extractall()'''

#con shutil
import shutil

'''direccion_carpeta = '/home/emanuel/Recetas'
nombre_archivo_comprimido = 'recetas_comprimidas'
shutil.make_archive(nombre_archivo_comprimido,'zip',direccion_carpeta)'''

shutil.unpack_archive('recetas_comprimidas.zip','Recetas','zip')