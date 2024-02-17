import bs4
import requests


'''
Este código busca extraer mediante web scraping, los libros que tengan 5 estrellas de calificación 
en la página web https://books.toscrape.com/
'''
url = 'https://books.toscrape.com/catalogue/page-{}.html'
enlaces = [url.format(numero) for numero in range(1, 51)]

