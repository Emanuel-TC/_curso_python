mi_bool = (4<5) and (5>5)
print(mi_bool)

texto = "Hola, este es un texto breve"
mi_bool = ('frase' in texto) or ("breve" in texto)
print(mi_bool)
mi_bool = ('Hola' in texto) and ('brebe' in texto)
print(mi_bool)

'''
Práctica Operadores Lógicos 1
Crea tres variables (num1 ,  num2 y num3):

Dentro de num1, almacena el valor 36

Dentro de num2, almacena el resultado de la operación 72/2

Dentro de num3, almacena el valor 48

Verifica si num1 es mayor que num2, y menor que num3. Almacena el resultado de dicha comparación en una variable llamada mi_bool.
'''
num1, num2, num3 = 36, 72/2, 48
mi_dic = {True:"sí",
          False: "no"}
print(f"El {num1} {mi_dic[num1>num2]} es mayor que {int(num2)} y {mi_dic[num1<num3]} es menor que {int(num3)}")
mi_bool = (num1 > num2) and (num1 < num3)
print("Un no y un sí en un and es igual a :",mi_bool)
print(f"El {num1} {mi_dic[num1>num2]} es mayor que {int(num2)} y {mi_dic[num1<num3]} es menor que {int(num3)}")
mi_bool = (num1 > num2) or (num1 < num3)
print("UN no y un sí en un or es igual a: ",mi_bool)