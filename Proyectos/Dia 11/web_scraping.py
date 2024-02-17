import bs4
import requests


# obtener el título del sitio web
url = 'https://www.escueladirecta.com/'
resultado = requests.get(url)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
titulo = sopa.select('title')[0].getText()

# Usamos el método select para buscar por las etiquetas de html, y recibimos una lista con los resultados, usamos [0] para obtener el primer resultado, y con getText() obtenemos el texto
print(f"El título del sitio web es: {titulo}")

# extraer elementos de una clase
'''columna_perfil = sopa.select('.profile-link')
for enlace in columna_perfil:
    print(enlace.getText())'''
#print(columna_perfil)

# extraer imágenes

imagenes = sopa.select('.course-box-image')
enlaces_imagenes = []
datos_imagenes = []
for imagen in imagenes:
    enlaces_imagenes.append(imagen['src'])
for enlace in enlaces_imagenes:
    datos_imagenes.append(requests.get(enlace))
contador = 0
for imagen in datos_imagenes:
    archivo = open("mi_imagen_" + str(contador) + ".jpg", "wb")
    archivo.write(imagen.content)
    archivo.close()
    contador += 1
