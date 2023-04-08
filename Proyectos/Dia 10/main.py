import pygame

# incializar pygame
pygame.init()

# colores
color_pantalla = (16, 33, 66)

# imágenes
icono_juego = pygame.image.load("imagenes/cohete.png")
imagen_nave = pygame.image.load("imagenes/transbordador-espacial.png")

# crear pantalla
pantalla = pygame.display.set_mode((800,600))

# título e ícono
pygame.display.set_caption("Invasión extraterrestre")
pygame.display.set_icon(icono_juego)

# posicion jugador
jugador_x = 368
jugador_y = 536


def posicion_jugador():
    pantalla.blit(imagen_nave, (jugador_x, jugador_y))


se_ejecuta = True


# loop del juego
while se_ejecuta:
    # RGB
    pantalla.fill(color_pantalla)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

    posicion_jugador()
    pygame.display.update()
