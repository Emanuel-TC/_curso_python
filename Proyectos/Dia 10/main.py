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
imagen_bala = pygame.image.load("imagenes/bala.png")

# crear pantalla
pantalla = pygame.display.set_mode((800,600))

# título e ícono
pygame.display.set_caption("Invasión extraterrestre")
pygame.display.set_icon(icono_juego)

# posicion jugador
jugador_x = 368 # Ancho de pantalla 800 a la mitad = 400, menos mitad de tamaño jugaodr, 64/2 = 32; 400-32 = 368
jugador_y = 500
posicion_jugador_x_cambio = 0
posicion_jugador_y_cambio = 0
se_mueve_a_la_derecha = 1
se_mueve_a_la_izquierda = -1
borde_izquierdo = 0
borde_derecho = 736


# posicion enemigo
enemigo_x = random.randint(0, 736)
enemigo_y = random.randint(50, 200)
posicion_enemigo_x_cambio = 1
posicion_enemigo_y_cambio = 50


# posición bala
bala_x = 0
bala_y = 500
posicion_bala_x_cambio = 0
posicion_bala_y_cambio = 1
bala_visible = False


# teclas
tecla_derecha = pygame.K_RIGHT
tecla_izquierda = pygame.K_LEFT


# funcion jugador
def posicion_jugador(x, y):
    pantalla.blit(imagen_nave, (x, y))


# funcion jugador
def posicion_enemigo(x, y):
    pantalla.blit(imagen_enemigo, (x, y))


def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(imagen_bala,(x + 16, y + 10)) # se les suman valores a la posición recibida para que no aparezan en la misma posición de la nave, sino un poco más arriba/centrado



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
                posicion_jugador_x_cambio = se_mueve_a_la_izquierda
            if evento.key == tecla_derecha:
                posicion_jugador_x_cambio = se_mueve_a_la_derecha
            if evento.key == pygame.K_SPACE:
                disparar_bala(jugador_x,bala_y)
        # soltar teclas
        if evento.type == pygame.KEYUP:  # tecla soltada
            if (evento.key == tecla_izquierda) or (evento.key == tecla_derecha):
                posicion_jugador_x_cambio = 0

    # modificar posicion jugador
    jugador_x += posicion_jugador_x_cambio
    # mantener dentro de bordes jugador
    if jugador_x <= borde_izquierdo:
        jugador_x = 0
    elif jugador_x >= borde_derecho:
        jugador_x = 736

    # modificar posicion enemigo
    enemigo_x += posicion_enemigo_x_cambio
    # mantener dentro de bordes jugador
    if enemigo_x <= borde_izquierdo:  # si toca el borde izquierdo cambia su dirección a la derecha
        posicion_enemigo_x_cambio = se_mueve_a_la_derecha
        enemigo_y += posicion_enemigo_y_cambio
    elif enemigo_x >= borde_derecho:  # si toca el borde derecho cambia su dirección a la izquierda
        posicion_enemigo_x_cambio = se_mueve_a_la_izquierda
        enemigo_y += posicion_enemigo_y_cambio

    # movimiento bala
    if bala_visible:
        disparar_bala(jugador_x,bala_y)
        bala_y -= posicion_bala_y_cambio

    posicion_jugador(jugador_x,jugador_y)
    posicion_enemigo(enemigo_x, enemigo_y)
    # Actualizar pantalla
    pygame.display.update()
