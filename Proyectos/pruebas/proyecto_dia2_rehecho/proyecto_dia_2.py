nombre = input("Introduce tu nombre: \n")
ventas = int(input("Introduce tu ventas: \n"))
print(f"Hola {nombre}, tu ventas es: {ventas}, por lo que tu comisón es de ${round(ventas*0.13,2)}")