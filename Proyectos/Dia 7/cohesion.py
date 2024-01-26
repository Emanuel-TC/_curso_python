'''
La cohesión se refiere al grado de relación entre los elementos de un módulo.
Cuando diseñamos una función, debemos identificar de un modo bien específico qué tarea va a realizar,
reduciendo su finalidad a un objetivo único y bien definido.

En resumen: para que una función sea cohesiva debe hacer solo una cosa, y si tiene que hacer más de una cosa,
estas deben tener una alta relación entre sí. Cuantas más cosas haga una función sin relación entre sí,
más complicado será entender el código.

Existen dos tipos de cohesión:

Cohesión débil:
    indica que la relación entre los elementos es baja, y por lo tanto no tienen una única funcionalidad.
Cohesión fuerte:
    indica que existe una alta relación entre los elementos existentes dentro del módulo.
    Este debe ser nuestro objetivo al diseñar programas.
'''

# Una versión con cohesión fuerte
def suma(num1, num2):
    resultado = num1 + num2
    return resultado

# cohesión débil
def suma():
    num1 = float(input("Elige un número"))
    num2 = float(input("Elige otro número"))
    resultado = num1 + num2
    return resultado
