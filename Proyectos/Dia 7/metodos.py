class Pajaro:
    alas = True
    def __init__(self,color,especie):
        self.color = color
        self.especie = especie

    def piar(self):
        print(f"Pio, mi color es {self.color} y mi especie es {self.especie}")

    def volar(self,metros):
        print(f"EL pajaro ha volado {metros} metros")

piolin = Pajaro("amarillo", "canario")
piolin.piar()
piolin.volar(50)

# Ejercicios prácticos

'''
Crea una clase Perro. Dicho perro debe poder ladrar.
Crea el método ladrar() y ejecútalo en una instancia de Perro. 
Cada vez que ladre, debe mostrarse en pantalla "Guau!".
'''
class Perro:

    def __init__(self):
        pass

    def ladrar(self):
        print("Guau!")

mi_perro = Perro()
mi_perro.ladrar()

'''
Crea una clase llamada Mago, y crea un método llamado 
lanzar_hechizo() (deberá imprimir "¡Abracadabra!").
Crea una instancia de Mago en el objeto merlin, y haz que lance un hechizo.
'''

class Mago:
    def __init__(self):
        pass
    def lanzar_hechizo(self):
        print("¡Abracadabra!")

merlin = Mago()
merlin.lanzar_hechizo()

'''
Crea una instancia de la clase Alarma, que tenga un método llamado postergar(cantidad_minutos). 
El método debe imprimir en pantalla el mensaje
"La alarma ha sido pospuesta {cantidad_minutos} minutos"
'''
class Alarma:
    def __init__(self):
        pass

    def postergar(self,cantidad_minutos):
        print(f"La alarma ha sido pospuesta {cantidad_minutos} minutos")

mi_alarma = Alarma()
mi_alarma.postergar(10)