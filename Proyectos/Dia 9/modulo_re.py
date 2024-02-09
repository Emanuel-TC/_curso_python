import re
import time
from os import system

'''Significado de valores en expresiones regulares
    caracter    descripción             ejemplo         Coincidencias
    /d          dígito numérico         v\d.\d\d        v1.23   v3.21   v5.98
    /w          caracter alfanumérico   \w\w\w-\w\w     abc-de  zqk-gh  lkj-fd
    /s          espacio en blanco       número\s\d\d    número 25   número 64 número 98
    
    ************  En mayúscula el valor significa lo contrario que en minúcula  *************
    caracter    descripción             ejemplo         Coincidencias
    /D          NO numérico             \D\D\D\D        Ksd-    .,LM    ?-A-
    /W          NO alfanumérico         \W\W\W\W        .,-?    ----    ?¡.,
    /S          NO espacio en blanco    \S\S\S\S        1234    -.,M    mns?
    
    ************  SIGNOS CUANTIFICADORES  *************
    caracter    descripción             ejemplo         Coincidencias
    +           1 o más veces           código_\d-\d+   código_1-1  código_2-97 código_3-321
    {n}         se repite n veces       \d-\d{4}        1-9876  2-6543  3-3698
    {n,m}       se repite de n a m veces \w{3,5}        a123   b12  32165
    {n,}        desde n hacia arriba      -\d{4,}-       -1234-   -98765-  -369852147-
    *           0  o más veces             \w\s*\w      s     s   vv     m a   f       6
    ?           1 o 0                   casa?           casa    casas
    
'''

'''texto = "Si necesitas ayuda llama al (01) 800-456-9999 las 24 horas al servicio del sistema online"
numero = r'\d{3}-\d{3}-\d{4}'
print(re.search(numero, texto).group())
'''
def valida_contrasenia(password):
    patron = r'[A-Z]\d\w{5}\W'
    if re.search(patron, password):
        print("Contraseña validada")
        return True
    else:
        return False

def validador():
    chequeo = 0
    while chequeo == False:
        system("clear")
        contrasenia = input("Ingrese contraseña empezando con una mayúscula, luego un numero, 5 letras y un signo especial:\n")
        chequeo = valida_contrasenia(contrasenia)
        if chequeo == False:
            print("Contraseña no valida, intenta otra vez en tres segundos")
            time.sleep(3)
    print("\n================================")
#validador()
'''
Práctica Módulo RE 1
Crea una función llamada verificar_email para comprobar si una dirección de email es correcta, que verifique si el email 
dado como argumento contiene "@" (entre el nombre de usuario y el dominio) y finaliza en ".com" (aunque aceptando también 
casos que cuentan con un dominio adicional, tal como ".com.br" para el caso de un usuario de Brasil).
Si se encuentra el patrón, la función debe finalizar mostrando en pantalla el mensaje "Ok", pero si detecta que la frase 
no contiene los elementos indicados, debe informarle al usuario "La dirección de email es incorrecta" imprimiendo el 
mensaje.
'''


def verificar_email(email):
    p = r'\w+@\w+\.com'
    if re.search(p, email):
        print("Ok")
    else:
        print("La dirección de email es incorrecta")

texto = input('Ingrese su email:\n')
verificar_email(texto)


'''
Práctica Módulo RE 2
Crea una función llamada verificar_saludo para verificar si una frase entregada como argumento inicia con la palabra 
"Hola". Si se encuentra el patrón, la función debe finalizar mostrando el mensaje "Ok", pero si detecta que la frase no 
contiene "Hola", debe informarle al usuario "No has saludado" imprimiendo el mensaje en pantalla.
'''

def verificar_saludo(frase):
    #p = r'Hola\.*'
    #el patrón anterior funciona bien, pero se puede mejorar
    p = r'Hola|HOLA|hola|\.*'
    if re.search(p, frase):
        print("Ok")
    else:
        print("No has saludado")
frase = input("Ingresa una frase, no olvides inciar con un 'Hola':\n")
verificar_saludo(frase)

'''
El código postal de una región determinada se forma a partir de dos caracteres alfanuméricos y cuatro numéricos a 
continuación (ejemplo: XX1234). Crea una función, llamada verificar_cp para comprobar si el código postal pasado como 
argumento sigue este patrón. Si el patrón es correcto, mostrar al usuario el mensaje "Ok", de lo contrario: 
"El código postal ingresado no es correcto".
'''
def verificar_cp(cp):
    p = r'\w{2}\d{4}'
    if re.search(p, cp):
        print("Ok")
    else:
        print("El código postal ingresado no es correcto")

cp = input("Ingrese su código postal:\n")
verificar_cp(cp)