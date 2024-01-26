# polimorfismo aplicado a un objeto que tiene métodos con el mismo nombre pero se pueden usar en objetos distintos
0class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"La vaca {self.nombre} dice muuu")

class Oveja:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"La vaca {self.nombre} dice beee")


vaca_uno = Vaca("Lola")
oveja_uno = Oveja("Shawn")
vaca_uno.hablar()
oveja_uno.hablar()
print("\n")

for animal in [vaca_uno, oveja_uno]:
    animal.hablar()
    print("\n")

def animal_hablar(animal):
    animal.hablar()

animal_hablar(vaca_uno)
animal_hablar(oveja_uno)

'''
Práctica Polimorfismo 1
La función incorporada en Python len() tiene un comportamiento polimórfico, ya que,
calcula el largo de un objeto en función de su tipo (strings, listas, tuples, entre otros), 
devolviendo la cantidad de items o caracteres que lo componen.
Crea un iterador que recorra los siguientes objetos: 
palabra, lista, tupla y muestre en pantalla (print()) para cada uno de ellos su longitud 
con la función len().
'''
palabra = "polimorfismo"
lista = ["Clases", "POO", "Polimorfismo"]
tupla = (1, 2, 3, 80)
def iterador_polimorfico(objeto):
    print(len(objeto))

iterador_polimorfico(palabra)
iterador_polimorfico(lista)
iterador_polimorfico(tupla)

'''
Práctica Polimorfismo 2
Cuentas con tres clases de personajes en un juego, los cuales cuentan con 
sus métodos de ataque específicos.
Crea un iterador que logre un ataque conjugado en el siguiente orden: 
Arquero, Mago, Samurai, llamando al método atacar() de cada uno de los personajes. 
Deberás crear instancias de cada una de las clases anteriores para construir un 
iterable (una lista llamada personajes) que pueda recorrese en dicho orden.
'''
class Mago():
    def atacar(self):
        print("Ataque mágico")

    def defender(self):
        print("Escudo mágico")

class Arquero():
    def atacar(self):
        print("Lanzamiento de flecha")

    def defender(self):
        print("Esconderse")

class Samurai():
    def atacar(self):
        print("Ataque con katana")

    def defender(self):
        print("Bloqueo")

mi_arquero = Arquero()
mi_mago = Mago()
mi_samurai = Samurai()

for personaje in [mi_arquero, mi_mago, mi_samurai]:
    personaje.atacar()

'''
Práctica Polimorfismo 3
Tienes tres clases de personajes en un juego, los cuales cuentan con sus métodos de 
defensa específicos.
Crea una función llamada personaje_defender(), que pueda recibir un objeto 
(una instancia de las clases de tus personajes), y ejecutar su método defender() 
independientemente de qué tipo de personaje se trate.
'''

def personaje_defender(personaje):
    personaje.defender()

personaje_defender(mi_arquero)
personaje_defender(mi_mago)
personaje_defender(mi_samurai)
