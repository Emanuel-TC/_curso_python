from pathlib import Path
#from os import System

directorio_base = Path.home() / "Recetas"

for txt in Path(directorio_base).glob("**/*.txt"):
    print(txt)
