from random import shuffle

#lista inicial
palitos = ["-","--","---","----"]

#mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista

#print(mezclar(palitos))

#pediler intento
def probar_suerte():
    intento = ""
    while intento not in ["1","2","3","4"]:
        intento = input("Escoge un numero del 1 al 4:\n ")
    return int(intento)
#intentos = probar_suerte()
#print(intentos)

#comprobar intento
def revisar_intento(lista,intento):
    if lista[intento - 1] == "-":
        print("Lava los platos ja, ja")
    else:
        print("Esta vez te has salvado")
    print(f"Te tocó el palito {lista[intento - 1]}\n")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()
revisar_intento(palitos_mezclados,seleccion)