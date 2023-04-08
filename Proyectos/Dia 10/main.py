import pygame
import random

# incializar pygame
pygame.init()

# colores
color_pantalla = (16, 33, 66)

# imágenes
icono_juego = pygame.image.load("imagenes/cohete.png")
imagen_nave = pygame.image.load("imagenes/transbordador-espacial.png")
imagen_enemigo = pygame.image.load("imagenes/ovni.png")
imagen_fondo = pygame.image.load("imagenes/fondo.png")

# crear pantalla
pantalla = pygame.display.set_mode((800,600))

# título e ícono
pygame.display.set_caption("Invasión extraterrestre")
pygame.display.set_icon(icono_juego)

# posicion jugador
jugador_x = 368
jugador_y = 500
posicion_jugador_x_cambio = 0
posicion_jugador_y_cambio = 0


# posicion enemigo
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
posicion_enemigo_x_cambio = 1
posicion_enemigo_y_cambio = 50

# teclas
tecla_derecha = pygame.K_RIGHT
tecla_izquierda = pygame.K_LEFT


# funcion jugador
def posicion_jugador(x, y):
    pantalla.blit(imagen_nave, (x, y))


# funcion jugador
def posicion_enemigo(x, y):
    pantalla.blit(imagen_enemigo, (x, y))


se_ejecuta = True


# loop del juego
while se_ejecuta:
    # RGB
    pantalla.blit(imagen_fondo, (0,0))

    for evento in pygame.event.get():
        # cerrar programa
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        # movimiento teclas
        if evento.type == pygame.KEYDOWN:  # tecla presionada
            if evento.key == tecla_izquierda:
                posicion_jugador_x_cambio = -1
            if evento.key == tecla_derecha:
                posicion_jugador_x_cambio = 1
        # soltar teclas
        if evento.type == pygame.KEYUP:  # tecla soltada
            if evento.key == pygame.key == tecla_izquierda or evento.key == tecla_derecha:
                posicion_jugador_x_cambio = 0

    # modificar posicion jugador
    jugador_x += posicion_jugador_x_cambio
    # mantener dentro de bordes jugador
    if jugador_x <= 0:
        jugador_x = 0
    elif jugador_x >= 736:
        jugador_x = 736

    # modificar posicion enemigo
    enemigo_x += posicion_enemigo_x_cambio
    # mantener dentro de bordes jugador
    if enemigo_x <= 0:  # si toca el borde izquierdo cambia su dirección a la derecha
        posicion_enemigo_x_cambio = 1
        enemigo_y += posicion_enemigo_y_cambio
    elif enemigo_x >= 736:  # si toca el borde derecho cambia su dirección a la izquierda
        posicion_enemigo_x_cambio = -1
        enemigo_y += posicion_enemigo_y_cambio

    posicion_jugador(jugador_x,jugador_y)
    posicion_enemigo(enemigo_x, enemigo_y)
    pygame.display.update()
