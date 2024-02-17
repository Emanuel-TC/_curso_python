import bs4
import requests


# obtener el título del sitio web
url = 'https://escueladirecta-blog.blogspot.com'
resultado = requests.get(url)

sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
titulo = sopa.select('title')[0].getText()

# Usamos el método select para buscar por las etiquetas de html, y recibimos una lista con los resultados, usamos [0] para obtener el primer resultado, y con getText() obtenemos el texto
print(f"El título del sitio web es: {titulo}")

# extraer elementos de una clase
columna_perfil = sopa.select('.profile-link')
for enlace in columna_perfil:
    print(enlace.getText())
#print(columna_perfil)