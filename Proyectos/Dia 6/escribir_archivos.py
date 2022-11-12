archivo = open("prueba_1.txt","w")
archivo.write("Soy el nuevo archivo\n")
lista_palabras = ["Hola","mundo","aquí","estoy"]
for palabra in lista_palabras:
    archivo.write(palabra)
    archivo.write("\n")
archivo.close()

archivo = open("prueba_1.txt","a")
archivo.write("Soy la linea final\n")
archivo.close()

