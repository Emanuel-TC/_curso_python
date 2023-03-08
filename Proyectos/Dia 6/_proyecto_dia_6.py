import os
import shutil
from pathlib import Path
from os import system
ruta_base = Path(Path.home(), "Recetas")

def listar_categorias():
    print("Las categorias son las siguientes: \n")
    for categoria in total_categorias:
        print(categoria)

def seleccionar_y_listar_categoria():
    categoria = input("\nIngrese el nombre de la categoria: \n")
    if categoria in total_categorias:
        lista_recetas = [receta.name for receta in Path(ruta_base, categoria).glob("**/*.txt")]
        #revisamos si categoria está vacía
        #caso leer
        if len(lista_recetas) == 0:
            limpiar_pantalla()
            print(f"En la categoria {categoria} no hay recetas")
            return categoria
        else:
            limpiar_pantalla()
            print("En la categoria seleccionada, las recetas son las siguientes: \n")
            for receta in lista_recetas:
                print(receta)
            return categoria
    else:
        limpiar_pantalla()
        print(f"La categoria {categoria} no existe")
        return False

def limpiar_pantalla():
    system("clear")

def mostrar_menu():
    lista_opciones = ['1 - Leer receta', '2 - Crear receta', '3 - Crear categoria', '4 - Eliminar receta', '5 - Eliminar categoria', '6 - Finalizar programa']
    for opciones in lista_opciones:
        print(opciones)

def leer_receta():
    listar_categorias()
    categoria_seleccionada = seleccionar_y_listar_categoria()
    if categoria_seleccionada == False:
        print("Menú principal:\n")
    else:
        lista_recetas = [receta.name for receta in Path(ruta_base, categoria_seleccionada).glob("**/*.txt")]
        if len(lista_recetas) == 0:
            print("\n")
        else:
            receta_a_leer = input("\nIngrese el nombre de la receta a leer: \n")
            if Path(ruta_base, categoria_seleccionada, receta_a_leer + ".txt").exists():
                limpiar_pantalla()
                print(f"""La receta dice lo siguiente:
                      {Path(ruta_base, categoria_seleccionada, receta_a_leer + ".txt").read_text()}""")
            else:
                limpiar_pantalla()
                print("La receta no existe")

def crear_receta():
    listar_categorias()
    categoria_seleccionada = seleccionar_y_listar_categoria()
    if categoria_seleccionada == False:
        print("Menú principal:\n")
    else:
        receta_a_crear = input("\nIngrese el nombre de la receta a crear \n")
        ruta_seleccionada = Path(ruta_base, categoria_seleccionada)
        receta_creada = ruta_seleccionada.joinpath(receta_a_crear + ".txt")
        texto_receta = input("\nIngrese el contenido de la receta:\n")
        mi_archivo = open(receta_creada, "w")
        mi_archivo.write(texto_receta)
        mi_archivo.close()

def crear_categoria():
    listar_categorias()
    categoria_a_crear = input("\nIngrese el nombre de la categoria a crear: \n")
    ruta_creada = Path(ruta_base, categoria_a_crear)
    if categoria_a_crear not in total_categorias:
        categoria_creada = os.mkdir(ruta_creada)
        limpiar_pantalla()
        print(f"La categoria {ruta_creada.name} ha sido creada en {ruta_base}")
    else:
        limpiar_pantalla()
        print("La categoria ya existe")

def eliminar_receta():
    listar_categorias()
    categoria_seleccionada = seleccionar_y_listar_categoria()
    if categoria_seleccionada == False:
        print("Menú principal:\n")
    else:
        receta_a_eliminar = input("\nIngrese el nombre de la receta a eliminar: \n")
        if Path(ruta_base, categoria_seleccionada, receta_a_eliminar + ".txt").exists():
            limpiar_pantalla()
            os.remove(Path(ruta_base, categoria_seleccionada, receta_a_eliminar + ".txt"))
            print(f"La receta {receta_a_eliminar} ha sido eliminada")
        else:
            limpiar_pantalla()
            print("La receta no existe")

def eliminar_categoria():
    listar_categorias()
    categoria_seleccionada = input("\nIngrese el nombre de la categoria a eliminar: \n")
    if categoria_seleccionada in total_categorias:
        shutil.rmtree(Path(ruta_base, categoria_seleccionada))
        limpiar_pantalla()
        print(f"La categoria {categoria_seleccionada} ha sido eliminada")
    else:
        limpiar_pantalla()
        print(f"La categoria {categoria_seleccionada} no existe")


respuesta = ''

# 1. Saludo al usuario
print("Holaa, nuevo usuario, te doy la más cordial bienvenida.")
# 2. informar dónde están las recetas
print(f"Las recetas se encuentran en: {ruta_base}")
# 3. informar cuántas recetas hay en esa carpeta

while respuesta!= '6':
    total_recetas = [receta for receta in Path(ruta_base).glob("**/*.txt")]
    total_categorias = [categoria.name for categoria in Path(ruta_base).iterdir() if categoria.is_dir()]
    print(f"Actualmente tenemos {len(total_recetas)} recetas.")
    # 4. Mostrar menú de opciones
    print("A continuación te mostraré un menú con las opciones disponibles:")
    mostrar_menu()
    respuesta = input("Ingrese una opción: ")
    limpiar_pantalla()
    if respuesta == '1':
        leer_receta()
    elif respuesta == '2':
        crear_receta()
    elif respuesta == '3':
        crear_categoria()
    elif respuesta == '4':
        eliminar_receta()
    elif respuesta == '5':
        eliminar_categoria()
