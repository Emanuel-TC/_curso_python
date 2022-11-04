from random import randint
intentos = 0
numero = 0
numero_secreto = randint(1,100)
nombre = input("Dime tu nombre: \n")
print(f"Hola {nombre}, estoy pensando un numero entre el 1 y el 100")
print("Tienes 8 intentos para averiguarlo")

while intentos < 8:
    numero = int(input("Ingresa un numero entre el 1 y el 100: "))
    intentos += 1
    if numero not in range(1,100):
        print(f"El número {numero} no es válido, ingresa un número entre el 1 y el 100")
    elif numero < numero_secreto:
        print(f"El numero que estoy pensando es mayor a {numero}")
    elif numero > numero_secreto:
        print(f"El numero que estoy pensando es menor a {numero}")
    else:
        print(f"Qué crack, el numero que estoy pensando sí es {numero}, adivinaste en {intentos} intentos")
        break
if numero != numero_secreto:
    print(f"Error, fallaste, agotaste los intentos, el numero correcto es {numero_secreto}")