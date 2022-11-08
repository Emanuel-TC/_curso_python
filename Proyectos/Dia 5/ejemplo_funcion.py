precios_cafe = [("Capuchino",1.5),("Expresso",2),("Moka",1.9)]

'''for elemento in precios_cafe:
    print(elemento)
'''
def cafe_mas_caro(lista_precios):
    precio_mayor = 0
    nombre_cafe = ""

    for cafe, precio in lista_precios:
        if precio > precio_mayor:
            precio_mayor = precio
            nombre_cafe = cafe
        else:
            pass

    return (nombre_cafe,precio_mayor)

print(cafe_mas_caro(precios_cafe))

cafe, precio = cafe_mas_caro(precios_cafe)

print(f"El cafe más caro es el {cafe} con un precio de {precio}")
