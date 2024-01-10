from pathlib import Path, PureWindowsPath
import os

ruta_actual = os.getcwd()
#print(ruta_actual)


ruta = Path(ruta_actual+"/prueba.txt") #ruta para cualquoer sistema
ruta_windows = PureWindowsPath(ruta) #convierte la ruta al estilo windows
if not ruta.exists():
    print("File not found")
else:
    print(f"File found in {ruta_windows}\nEl archivo dice lo siguiente:\n")
    print(ruta.read_text())