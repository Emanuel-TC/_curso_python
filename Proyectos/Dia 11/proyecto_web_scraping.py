import bs4
import requests


'''
Este código busca extraer mediante web scraping, los libros que tengan sólo 4 o 5 estrellas de calificación 
en la página web https://books.toscrape.com/
'''
url = 'https://books.toscrape.com/catalogue/page-{}.html'
titulos = []
# identificar condiciones de extracción
clase_libro = '.product_pod'
calificacion_4_estrellas = '.star-rating.Four' # nota: Cuando hay un espacio en el nombre de la clase, se debe reemplazar por un punto.
calificacion_5_estrellas = '.star-rating.Five'

def genera_pagina(url,numero):
    yield url.format(numero)

for n in range(1,51):
    pagina = next(genera_pagina(url,n))
    resultado = requests.get(pagina)
    sopa = bs4.BeautifulSoup(resultado.text, 'lxml')
    # Primera condición, buscamos los elementos que tengan la clase "product_pod"
    libros = sopa.select(clase_libro)
    for libro in libros:
        # Segunda condición, buscamos los elementos que tengan la clase "star-rating Four" o "star-rating Five"
        if libro.select(calificacion_4_estrellas):
            titulos.append(libro.h3.a['title']) # podemos acceder a los "hijos" de un tag con la notación "tag.hijo"
            print(f"El libro {libro.h3.a['title']} tiene 4 estrellas")
        elif libro.select(calificacion_5_estrellas):
            titulos.append(libro.h3.a['title'])
            print(f"El libro {libro.h3.a['title']} tiene 5 estrellas")
