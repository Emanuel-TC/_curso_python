class Animal:

    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
    def nacer(self):
        print(f"Nació un {self.__class__.__name__}")

    def hablar(self):
        print("Este animal emite un sonido")

class Pajaro(Animal):
    #para los atributos de la clase, si queremos agregar un nuevo atributo
    #es posile ahorrar los atributos de la clase padre y añadir los que necesitamos

    def __init__(self, edad, color, altura_vuelo):
        #usamos super
        super().__init__(edad, color)
        self.altura_vuelo = altura_vuelo

    def hablar(self):
        print("Pio")
    def volar(self,metros):
        print(f"{Pajaro.__name__} voló {metros} metros")

piolin = Pajaro(2,"amarillo",20)
#en herencia extendida los métodos que son iguales de los que heredan se ejcutan en lugar de
#los que heredaron
piolin.hablar()
piolin.volar(20)
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

class Padre:
    def hablar(self):
        print("Hola")

#también puede heredar de distintas clases
class Madre:
    def reir(self):
        print("Ja, ja")
    #si existen los mismos métodos en clases distintas heradadas, toma
    #el método de la primer clase que heredó
    def hablar(self):
        print("Qué tal")

class Hijo(Padre, Madre):
    pass

class Nieto(Hijo):
    pass

nieto = Nieto()

nieto.hablar()
nieto.reir()

'''
Práctica Herencia Extendida 1

Si la clase Hija ha heredado de su padre la forma de reir, y de su madre la vocación, 
y hoy tienen el mismo trabajo en la Fiscalía, crea la herencia múltiple que le permita 
a esta clase heredar correctamente de Padre y Madre.
Completa el código suministrado a continuación para lograrlo.
'''


class Padre():
    def trabajar(self):
        print("Trabajando en el Hospital")

    def reir(self):
        print("Ja ja ja!")

class Madre():
    def trabajar(self):
        print("Trabajando en la Fiscalía")

class Hija(Madre,Padre):
    pass
Elizabeth = Hija()
Elizabeth.trabajar()
Elizabeth.reir()

'''
Práctica Herencia Extendida 2
"El ornitorrinco es una de las criaturas más raras del mundo: aunque es un mamífero, 
pone huevos; y amamanta a sus crías pero no tienen mamas." (National Geographic)

Crea una clase Ornitorrinco que herede de otras clases: 
Vertebrado, Pez, Reptil, Ave y Mamifero, tal que "construyas" un animal que 
tiene los siguientes métodos y atributos:

- poner_huevos()
- tiene_pico = True
- vertebrado = True
- venenoso = True
- nadar()
- caminar()
- amamantar()
'''
class Vertebrado:
    vertebrado = True

class Ave(Vertebrado):
    tiene_pico = True
    def poner_huevos(self):
        print("Poniendo huevos")

class Reptil(Vertebrado):
    venenoso = True

class Pez(Vertebrado):
    def nadar(self):
        print("Nadando")
    def poner_huevos(self):
        print("Poniendo huevos")

class Mamifero(Vertebrado):
    def caminar(self):
        print("Caminando")
    def amamantar(self):
        print("Amamantando crías")

class Ornitorrinco(Ave,Pez,Mamifero,Reptil):
    pass

perry = Ornitorrinco()
if perry.vertebrado:
    print(f"{Ornitorrinco.__name__} es vertebrado")
    if perry.tiene_pico:
        print(f"{Ornitorrinco.__name__} tiene pico")
        if perry.venenoso:
            print(f"{Ornitorrinco.__name__} es venenoso")
            perry.poner_huevos()
            perry.nadar()
            perry.caminar()
            perry.amamantar()

'''
Práctica Herencia Extendida 3

Un hijo ha heredado de su padre todas sus características, sin embargo, 
tienen diferentes hobbies. Logra que la clase Hijo herede de Padre todos sus métodos 
y atributos, sobreescribiendo el método hobby() para que se devuelva[1]: 
"Juego videojuegos en mi tiempo libre"

[1]: asegúrate de utilizar return seguido de una cadena de texto
'''


class Padre():
    color_ojos = "marrón"
    tipo_pelo = "rulos"
    altura = "media"
    voz = "grave"
    deporte_preferido = "tenis"

    def reir(self):
        return "Jajaja"

    def hobby(self):
        return "Pinto madera en mi tiempo libre"

    def caminar(self):
        return "Caminando con pasos largos y rápidos"


class Hijo(Padre):
    def hobby(self):
        return "Juego videojuegos en mi tiempo libre"
Emanuel = Hijo()
print(f"Emanuel heredó de su padre ojos color {Emanuel.color_ojos}, pelo tipo {Emanuel.tipo_pelo}, altura de {Emanuel.altura}, una voz {Emanuel.voz}, y su deporte favorito es el {Emanuel.deporte_preferido}, pero su hobby es {Emanuel.hobby()}")