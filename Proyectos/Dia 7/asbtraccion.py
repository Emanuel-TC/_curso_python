'''La abstracción es el pilar de la programación orientada a objetos que se relaciona con ocultar toda la
complejidad que algo puede tener por dentro, ofreciendo una interfaz con funciones de alto nivel, por lo general
sencillas de usar, que pueden ser usadas para interactuar con la aplicación sin tener conocimiento de lo que
hay dentro.'''

class Animal:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Woof!"

class Gato(Animal):
    def hacer_sonido(self):
        return "Meow!"

# Uso de la abstracción
mascota1 = Perro("Buddy", 3)
mascota2 = Gato("Whiskers", 2)

print(f"{mascota1.nombre} dice: {mascota1.hacer_sonido()}")
print(f"{mascota2.nombre} dice: {mascota2.hacer_sonido()}")
