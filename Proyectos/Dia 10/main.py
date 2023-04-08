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
posicion_jugador_x_cambio = 0
posicion_jugador_y_cambio = 0

# teclas
tecla_derecha = pygame.K_RIGHT
tecla_izquierda = pygame.K_LEFT


def posicion_jugador(x, y):
    pantalla.blit(imagen_nave, (x, y))


se_ejecuta = True


# loop del juego
while se_ejecuta:
    # RGB
    pantalla.fill(color_pantalla)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False

        if evento.type == pygame.KEYDOWN:  # tecla presionada
            if evento.key == tecla_izquierda:
                posicion_jugador_x_cambio = -0.3
            if evento.key == tecla_derecha:
                posicion_jugador_x_cambio = 0.3

        if evento.type == pygame.KEYUP:  # tecla soltada
            if evento.key == pygame.key == tecla_izquierda or evento.key == tecla_derecha:
                posicion_jugador_x_cambio = 0

    jugador_x += posicion_jugador_x_cambio
    posicion_jugador(jugador_x,jugador_y)
    pygame.display.update()
