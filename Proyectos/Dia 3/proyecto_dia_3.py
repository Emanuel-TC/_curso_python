nombre = input("Hola, '¿cómo te llamas?") #declaro variable para almacenar el nombre
print(f"Hola, {nombre}, por favor ingresa un texto del tipo que gustes: ")
texto = input(" ") #declaro variable para contener el texto
print("A continuación necesito que ingreses tres letras")
letra_numero_1 = input("Ingresa la primer letra") # en cada una
letra_numero_2 = input("Ingresa la segunda letra") # de las siguientes variables
letra_numero_3 = input("Ingresa la tercera letra") # se almacena cada letra por contabilizar

letra_numero_1 = letra_numero_1.lower() # cada letra
letra_numero_2 = letra_numero_2.lower() # se transofrma
letra_numero_3 = letra_numero_3.lower() # en minúsculas

lista = [letra_numero_1, letra_numero_2, letra_numero_3] #se almacenan en una lista las letras anteriores
nuevo_texto = texto.lower()  #todo el texto se convierte en minúsculas

aparicion_letra_1 = nuevo_texto.count(letra_numero_1) #en cada una de estas variables
aparicion_letra_2 = nuevo_texto.count(letra_numero_2) # se almacena la cantidad de veces
aparicion_letra_3 = nuevo_texto.count(letra_numero_3) # que aparece cada letra en el texto

numero_de_palabras = list(texto.split()) #esta función separa el texto en elementos separados regularmente por un espacio " " y se almacena en unavaribale en forma de lista
primer_letra = texto[0] #Solicito valor del primer índice del texto original
ultima_letra = texto[-1] #ultimo valor del índice del texto original
texto_inverso = texto[::-1] # se invierte todo el texto desde : valor 0 : hasta últo valor :-1 en reversa
buscar_python = 'Python' in texto #almacenamos un True o un False con la comparación
dic = {True:"sí", False:"no"} #construyo un diccionario con dos valores, sí y no, con propiedad True o False
print(f"""En tu texto: '{texto}' \nse encuentran {aparicion_letra_1} veces la letra {letra_numero_1},
              {aparicion_letra_2} veces la letra {letra_numero_2}, 
              y {aparicion_letra_3} veces la letra {letra_numero_3}.             
              Además existen {len(numero_de_palabras)} palabras en total.
              La primer letras es {primer_letra} y la ultima letra es {ultima_letra}.
              El texto al revés dice: '{texto_inverso}'
              Finalmente la palabra 'Python' {dic[buscar_python]} está en el texto""")


