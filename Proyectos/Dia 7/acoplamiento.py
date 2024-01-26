'''El acoplamiento es un concepto que mide la dependencia entre dos módulos distintos (como por ejemplo, clases).

Podemos hablar de dos tipos:

Acoplamiento débil,
    que implica que no hay dependencia entre un módulo y otros. Esta es la situación ideal.
Acoplamiento fuerte,
    que es la situación contraria, e indica que el módulo tiene dependencias internas con otros.

Se trata de un pilar vinculado con la cohesión, ya que por lo general un acoplamiento débil se asocia a una
cohesión fuerte.'''

# Una situación de acoplamiento fuerte puede originar errores que son difíciles de depurar.

class Mascota:
    tiene_patas = True
    pass


class Perro:
    def correr(self, velocidad):
        if Mascota.tiene_patas:
            self.velocidad = velocidad


mi_mascota = Perro()
mi_mascota.correr("rápido")
print(mi_mascota.velocidad)