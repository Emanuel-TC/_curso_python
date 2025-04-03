from random import randint

num_secreto = randint(1,100)
num_intentos = 0
print("Bievenido:")
##intento = input(f"Introduce un número para adivinar el número secreto entre 1 y 100: \n")
while num_intentos < 8:
    intento = input(f"Introduce un número para adivinar el número secreto entre 1 y 100: \n")
    if int(intento) == num_secreto:
        print(f"Felicidades, el número sí es: {intento}")
        break
    elif int(intento) < num_secreto:
        num_intentos += 1
        print(f"Lo siento, el número {intento} es menor que el número secreto")
        print(f"Te quedan {8 - num_intentos} intentos.\n")
    elif int(intento) > num_secreto:
        num_intentos += 1
        print(f"Lo siento, el número {intento} es mayor que el número secreto, inténtalo de nuevo")
        print(f"Te quedan {8 - num_intentos} intentos.\n")
if num_intentos == 8:
    print(f"Fallaste, el número era: {num_secreto}")
else:
    print("VICTORY!")