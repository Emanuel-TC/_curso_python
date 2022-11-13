from pathlib import Path, PureWindowsPath


ruta = Path("/Users/Emanuel/Desktop/_curso_python/Proyectos/Dia 6/prueba.txt") #ruta para cualquoer sistema
ruta_windows = PureWindowsPath(ruta) #convierte la ruta al estilo windows
if not ruta.exists():
    print("File not found")
else:
    print(f"File found in {ruta_windows}")
    print(ruta.read_text())