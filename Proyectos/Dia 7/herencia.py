class Animal:

    def __init__(self, edad,color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print(f"Nació un {self.__class__.__name__}")

class Pajaro(Animal):
    pass

piolin = Pajaro(2,"amarillo")
print(f"Hace {piolin.edad} años nació un {piolin.__class__.__name__} de color {piolin.color}")

'''
Práctica Herencia 1
Crea una clase llamada Persona, que tenga los siguientes atributos de instancia: nombre, edad. Crea otra clase, 
Alumno, que herede de la primera estos atributos.
'''
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
class Alumno(Persona):
    pass

'''
Practica 2 Herencia
Crea una clase llamada Mascota, que tenga los siguientes atributos de instancia: 
edad, nombre, cantidad_patas. Crea otra clase, Perro, que herede de la primera sus atributos.
'''
class Mascota:
    def __init__(self, edad, nombre, cantidad_patas):
        self.edad = edad
        self.nombre = nombre
        self.cantidad_patas = cantidad_patas
class Perro(Mascota):
    pass

'''
Práctica Herencia 3
Crea una clase llamada Vehiculo, que contenga los métodos acelerar() y frenar() 
(puedes dejar el código de los métodos en blanco con pass). 
Crea una clase llamada Automovil que herede estos métodos de Vehiculo.
'''
class Vehiculo:

    def acelerar(self, velocidad):
        print(f"{self.__class__.__name__} aceleró a {velocidad} km/h")
    def frenar(self, tiempo):
        print(f"{self.__class__.__name__} frenó en {tiempo} segundos")
class Automovil(Vehiculo):
    pass

vento = Automovil()
vento.acelerar(100)
vento.frenar(10)