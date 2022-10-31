#Realiza un programa que pregunte nombre, y ventas
#Debe de darle las comisones que equivalen a un 13 % de las ventas
nombre = input("Hola, ¿Cuál es tu nombre? ") #en la variable nombre almacenas la entrada
ventas = input("¿Cuántas ventas hiciste? ") # en la variable ventas almacenas las ventas
numero_de_ventas = int(ventas) # en esta nueva variable conviertes de string a int las ventas
comisiones = round((numero_de_ventas * 13)/100,2) # se sacan las comsiones
#comisiones = round(comisiones,2) # se redondean las comisiones a 2 decimales
print(f"Ok, {nombre} venditse {ventas} y por lo tanto, tus comsiones son de {comisiones}")

