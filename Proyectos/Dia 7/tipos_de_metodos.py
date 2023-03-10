class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print("Pio")

    #metodos de instancia
    def volar(self,metros):
        print(f"EL pajaro ha volado {metros} metros")
        #acceden a otros métodos
        self.piar()

    #metodo de instancia
        #acceden y modifican atributos del objeto de la clase

    def pintar_negro(self):
        self.color = "negro"
        print(f"El pajaro tiene el color {self.color}")

    #metodos de Clase
    #no necesitan instancia para ejecutarse (self)
    @classmethod
    def poner_huevos(cls,cantidad):
        print(f"Puso {cantidad} huevos")
        #pueden modificar atributos de clase pero no de instancia
        cls.alas = False
        print(Pajaro.alas)
        #LO siguiente es un error, no puedes usar self en métodos de clase
        #print(f"Es de color {self.color}")

    #métodos estáticos
    @staticmethod
    #no pueden acceder a atributos de clase ni de instancia
    def mirar():
        #self.color = "rojo"
        #cls.alas = True
        print("El pajaro mira")
        #se puede llamar sin crear un objeto de su clase

piolin = Pajaro("amarillo", "canario")
piolin.pintar_negro()
piolin.volar(10)
#metodos de instancia
#pueden moficicar estado de la clase
piolin.alas = False
print(piolin.alas)
Pajaro.poner_huevos(2)
Pajaro.mirar()

'''
Crea un método estático respirar() para la clase Mascota. 
Cuando se llame, debe imprimir en pantalla "Inhalar... Exhalar"
'''
class Mascota:
    @staticmethod
    def respirar():
        print("Inhalar... Exhalar")
Mascota.respirar()

'''
Crea un método de clase revivir() que actúa sobre el atributo de clase vivo de la clase 
Jugador, estableciéndolo en True cada vez que es invocado. 
El valor predeterminado del atributo vivo, debe ser False.
'''


class Jugador:
    vivo = False
    @classmethod
    def revivir(cls):
        cls.vivo = True
        print(cls.vivo)
Jugador.revivir()

'''
Crea un método de instancia lanzar_flecha() que reste en -1 la cantidad de flechas que 
tiene una instancia de Personaje, que cuenta con un atributo de instancia de tipo número, 
llamado cantidad_flechas.
'''
class Personaje:

    def __init__(self,cantidad_flechas):
        self.cantidad_flechas = cantidad_flechas

    def lanzar_flecha(self):
        self.cantidad_flechas = self.cantidad_flechas - 1


MiPersonaje = Personaje(10)
MiPersonaje.lanzar_flecha()
