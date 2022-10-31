#x = True
#mascota = "perro"
#if not x: #si no es verdadero no se imprime
#    print("Es correcto")
#elif 2 > 2: #revisa la siguiente, pero también es falsa
#    print("Hola")
#elif 2 > 2: #Esta sí la imprime
#    print("Hola, 2 >= 2 sí es verdadera")
#elif mascota == "gato":
#    print("Esto es falso")
#else:
#    print(f"{mascota} no es igual a agto")
#mascota = "Perro"
#if mascota == "Gato":
#    print("Tienes un gato")
#elif mascota == "Perro":
#    print(f"Tienes un {mascota}")
#else:
#    print("No sé qué mascota tienes")
edad = 16
calificacion = 9
if edad >= 18:
    print("Eres mayo de edad")
    if calificacion >= 7:
        print(f"Aprobaste con {calificacion}")
    else:
        print(f"Reprobado con {calificacion}")
else:
    print("Eres menor de edad")
    if calificacion >= 7:
        print(f"Aprobaste con {calificacion}")
        num1 = input("Ingresa un número:")
        num2 = input("Ingresa otro número:")
        if num1 > num2:
            print(f"{num1} es mayor que {num2}")
        elif num2 > num1:
            print(f"{num2} es mayor que {num1}")
        else:
            print(f"{num1} y {num2} son iguales")
    else:
        print(f"Reprobado con {calificacion}")