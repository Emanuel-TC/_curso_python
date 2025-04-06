def calcula_area(tipo_poligono):
    '''
    :param tipo_poligono: 'TRIANGULO', 'CUADRADO', 'RECTANGULO'
    :return: float(area_poligono)
    '''
    if tipo_poligono.upper() == 'TRIANGULO':
        base = int(input("Ingresa la medida de la base del triangulo: \n"))
        altura = int(input("Ingresa la altura del triangulo: \n"))
        return (base * altura)/2
    elif tipo_poligono.upper() == 'CUADRADO':
        base = int(input("Ingresa la medida de un lado del cuadrado: \n"))
        return base**2
    elif tipo_poligono.upper() == 'RECTANGULO':
        base = int(input("Ingresa la base del rectangulo: \n"))
        altura = int(input("Ingresa la altura del rectangulo: \n"))
        return base * altura
    else:
        print("No has ingresado un polígono correcto")
print(f"La base de un cuadrado es igual a: {calcula_area('CUADRADO')}")
print(f"La base de un triangulo es igual a: {calcula_area('triangulo')}")
print(f"La base de un rectangulo es igual a: {calcula_area('Rectangulo')}")