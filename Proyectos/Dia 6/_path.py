from pathlib import Path

base = Path.home() #ruta absoluta al directorio principal del usuario
guia = Path("Barcelona","Ruta_Sagrada")
print(base)
print(guia)
ruta_unida = Path(base,"Europa","España","Barcelona","Ruta_Sagrada.txt")
print(f"La ruta junta es: {ruta_unida}")
#si queremos tener la misma ruta pero con un archivo distinto, porque Path distingue archivo y directorio
#entonces hacemos lo siguiente:
ruta_dos = ruta_unida.with_name("Este_Es_Otro_Archivo_en_La_Ruta.txt") #toma la ruta anterior pero dirige a un archivo distinto
print(f"La ruta es: {ruta_dos}")
#para tener la dirección hasta el directorio padre más cercano, se hace lo siguiente:

print(f"La ruta con el directorio padre más cercano es: {ruta_dos.parent}")
#si queremos el siguiente directorio padre, sólo se concatena la extensión .parent otra vez
print(f"El siguiente directorio padre más cercano es: {ruta_dos.parent.parent}")
#A continuacion vamos a enumerar los archivos de un directorio

base = Path(Path.home(),"Europa")
print(f"Vamos a imprimir los archivos que están en la ruta {base}")
for txt in Path(base).glob("*.txt"):
    print(f"El archivo: {txt}")
print("Pero si quieres imprimir todos los que hay en las subcarpetas (si las hay, claro,) haces los siguiente: ")
for txt in Path(base).glob("**/*.txt"):
    print(f"El archivo: {txt}")
print("Si quieres imprimir una direccion a partir de un punto en especial, haces:")
guia = Path("Europa","España","Barcelona","Ruta_Sagrada.txt")
desde_europa = guia.relative_to("Europa")
desde_espania = guia.relative_to("Europa","España")
print(desde_europa)
print(desde_espania)
