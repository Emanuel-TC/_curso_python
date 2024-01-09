'''
Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla cuántos números
primos hay en el rango que va desde cero hasta ese número
incluido, y va a devolverla cantidad de números primos que
encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos
'''
'''def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0

    while iteracion <= numero:
        print(f"El número actual es {iteracion}")
        for n in range(3,iteracion,2):
            print(f"Revisamos el número {n}")
            if iteracion % n == 0:
                print(f"{iteracion} modulo {n} es 0")
                iteracion += 2
                print(f"Ahora el número en el ciclo es {iteracion}")
                break
        else:
            primos.append(iteracion)
            print(f"A la lista se agrega el número {iteracion}")
            iteracion += 2
            print(f"Ahora el número es {iteracion}\n")

    print(primos)
    return len(primos)

print(contar_primos(7))'''


def contar_primos(numero):
    primos = [2]
    iteracion = 3
    if numero < 2:
        return 0

    while iteracion <= numero:
        print(f"La lista actual es {primos}")
        print(f"La iteración actual es {iteracion}")
        for n in range(3, iteracion, 2):
            print(f"Entramos al ciclo for\n\tRevisamos si {iteracion} módulo {n} es 0")
            if iteracion % n == 0:
                print(f"{iteracion} modulo {n} es 0")
                break
            print(f"\t\tEn efecto, {iteracion} modulo {n} es 0")
        else:
            primos.append(iteracion)
            print(f"A la lista se agrega el número {iteracion}")

        iteracion += 2
        print(f"Sumanos 2 a {iteracion-2}")
        print(f"Ahora el número es {iteracion}\n")

    print("Se termina de iterar")
    print(primos)
    return len(primos)

print(contar_primos(19))



