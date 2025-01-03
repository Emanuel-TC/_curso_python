import os
import shutil
from os import system
from pathlib import Path
ruta_recetas = Path(Path.home(),"Recetas")

def contar_recetas(ruta):
    contador = 0
    for _ in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def imprimir_menu(opciones):
    print("El menú es el siguiente:")
    for _ in opciones:
        print(_)
def encontrar_opcion(opcion,opciones):
    opcion = str(opcion)
    for op in opciones:
        if opcion in op:
            return op

def seleccionar_categoria():
    categorias = listar_categorias()
    imprimir_categorias()
    categoria = input("Ingresa la categoría que quieres seleccionar: \n")
    while categoria not in categorias:
        system("cls")
        print(f"La categoria {categoria} no existe, asegúrate de haberla ingresado correctamente")
        imprimir_categorias()
        categoria = input("Ingresa la categoría que quieres seleccionar: \n")
    else:
        return categoria
def listar_categorias():
    categorias = []
    for categoria in os.listdir(ruta_recetas):
        categorias.append(categoria)
    return categorias
def imprimir_categorias():
    print("Las categorías son las siguientes:\n")
    for _ in os.listdir(ruta_recetas):
        print(_)
def imprimir_recetas(ruta_categoria):
    for receta in Path(ruta_categoria).glob("**/*.txt"):
        nombre_receta = Path(receta.name)
        print(nombre_receta)

def leer_receta():
    categoria = seleccionar_categoria()
    ruta_categoria = Path(ruta_recetas, categoria)
    system("cls")
    total_recetas = contar_recetas(ruta_categoria)
    if total_recetas > 0:
        print(f"Las recetas en la categoria {categoria} son: \n")
        imprimir_recetas(ruta_categoria)
        receta_a_leer = input("Ingresa el nombre de la receta que deseas leer sin la extensión .txt\n") + ".txt"
        receta_a_leer = Path(ruta_categoria,receta_a_leer)
        while not receta_a_leer.exists():
            print(f"El archivo {receta_a_leer} no existe")
            receta_a_leer = input("Ingresa el nombre de la receta que deseas leer sin la extensión .txt\n") + ".txt"
            receta_a_leer = Path(ruta_categoria, receta_a_leer)
        else:
            print("La receta dice lo siguiente:\n")
            print(receta_a_leer.read_text()+"\n")
            salir = (input("\nDeseas regresar al menú principal (s/n)?\n")).lower()
            if salir == "n":
                leer_receta()
            else:
                pass
    else:
        system("cls")
        print("Lo siento, en esta categoría no existen recetas actualmente, volveremos al menú principal y crea una nueva receta\n")

    #return True
def crear_receta():
    categoria = seleccionar_categoria()
    system("cls")
    ruta_categoria = Path(ruta_recetas,categoria)
    total_recetas = contar_recetas(ruta_categoria)
    if total_recetas > 0:
        imprimir_recetas(ruta_categoria)
        print(f"Las recetas en la categoria {categoria} son: \n")
    nombre_receta = input("Ingresa el nombre de la receta que deseas crear:\n") +".txt"
    ruta_receta = Path(ruta_recetas, categoria, nombre_receta)
    archivo = open(ruta_receta, "w")
    salir = []
    lista_palabras = []
    while salir != "s":
        texto_receta = input("Ingresa el contenido de tu receta:\n")
        lista_palabras.append(texto_receta)
        salir = input("Deseas terminar la receta (s/n)").lower()
    for _ in lista_palabras:
        archivo.write(_+"\n")
    archivo.close()
def crear_categoria():
    imprimir_categorias()
    nombre_categoria = input("Ingresa el nombre de la categoría que deseas crear: \n")
    system("cls")
    ruta_categoria = Path(ruta_recetas, nombre_categoria)
    categorias = listar_categorias()
    if nombre_categoria not in categorias:
        os.mkdir(ruta_categoria)
        if ruta_categoria.exists():
            print("La categoría fue creada con éxito")
            imprimir_categorias()
            salir = (input("\nDeseas regresar al menú principal (s/n)?\n")).lower()
            if salir == "n":
                print("Crear Categoria:\n")
                crear_categoria()
            else:
                while salir != 's':
                    salir = (input("\nDeseas regresar al menú principal (s/n)?\n")).lower()
        else:
            print("Ocurrió un error xc")
def eliminar_receta():
    categoria = seleccionar_categoria()
    system("cls")
    ruta_categoria = Path(ruta_recetas,categoria)
    total_recetas = contar_recetas(ruta_categoria)
    if total_recetas > 0:
        print(f"Las recetas en la categoria {categoria} son: \n")
        imprimir_recetas(ruta_categoria)
        receta_a_eliminar = input("Ingresa el nombre de la receta que deseas eliminar sin la extensión .txt\n") + ".txt"
        receta_a_eliminar = Path(ruta_categoria, receta_a_eliminar)
        while not receta_a_eliminar.exists():
            print(f"El archivo {receta_a_eliminar} no existe")
            receta_a_eliminar = input("Ingresa el nombre de la receta que deseas eliminar sin la extensión .txt\n") + ".txt"
            receta_a_eliminar = Path(ruta_categoria, receta_a_eliminar)
        else:
            os.remove(receta_a_eliminar)
            if receta_a_eliminar.exists():
                print("Ocurrió un error al eliminar el archivo")
            else:
                print("La receta fue eliminada")
            salir = (input("\nDeseas regresar al menú principal (s/n)?\n")).lower()
            if salir == "n":
                eliminar_receta()
            else:
                pass
    else:
        system("cls")
        print("Lo siento, en esta categoría no existen recetas actualmente, volveremos al menú principal:\n")
def eliminar_categoria():
    categoria = seleccionar_categoria()
    system("cls")
    ruta_categoria = Path(ruta_recetas, categoria)
    if ruta_categoria.exists():
        shutil.rmtree(ruta_categoria)
        if not ruta_categoria.exists():
            print("La categoria fue eliminada\nLas categorías han quedado de la siguiente forma:\n")
            listar_categorias()
        else:
            print("Ocurrió un error al eliminar la categoria")
    else:
        print("La categoria no existe, ingresa una correctamente:\n")
        eliminar_categoria()
def seleccionar_opcion(eleccion,opciones):
    for _ in opciones:
        if eleccion == "1. Leer receta":
            return leer_receta()
        elif eleccion == "2. Crear receta":
            return crear_receta()
        elif eleccion == "3. Crear categoría":
            return crear_categoria()
        elif eleccion == "4. Eliminar receta":
            return eliminar_receta()
        elif eleccion == "5. Eliminar categoría":
            return eliminar_categoria()
        else:
            return True


opciones = ["1. Leer receta","2. Crear receta","3. Crear categoría","4. Eliminar receta", "5. Eliminar categoría", "6. Finalizar programa"]

total_recetas = contar_recetas(ruta_recetas)

opcion = 0

while opcion != 6:
    # Bienvenida al usuario
    print(f"Hola, bienvenido, las recetas están ubicadas en {ruta_recetas}\nY existen {total_recetas} recetas en total")
    imprimir_menu(opciones)
    opcion = int(input("Ingresa el número de la opción que quieres ejecutar: \n"))
    system('cls')
    print(f"Has elegido la opción {encontrar_opcion(opcion,opciones)}")
    seleccionar_opcion(encontrar_opcion(opcion,opciones),opciones)
