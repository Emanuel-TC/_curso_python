import pygame
import random
import math
from pygame import mixer

# incializar pygame
pygame.init()

# colores
color_pantalla = (16, 33, 66)

# imágenes
icono_juego = pygame.image.load("imagenes/cohete.png")
imagen_nave = pygame.image.load("imagenes/transbordador-espacial.png")

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


# música
mixer.music.load("audio/MusicaFondo.mp3")
mixer.music.set_volume(0.3)
mixer.music.play(-1)


# variables enemigo
imagen_enemigo =  []
enemigo_x = []
enemigo_y = []
posicion_enemigo_x_cambio = []
posicion_enemigo_y_cambio = []
cantidad_enemigos = 8

for _ in range(cantidad_enemigos):
    imagen_enemigo.append(pygame.image.load("imagenes/ovni.png"))
    enemigo_x.append(random.randint(0, 736))
    enemigo_y.append(random.randint(50, 200))
    posicion_enemigo_x_cambio.append(0.5)
    posicion_enemigo_y_cambio.append(50)


# posición bala
bala_x = 0
bala_y = 500
posicion_bala_x_cambio = 0
posicion_bala_y_cambio = 3
bala_visible = False


# puntaje
puntaje = 0
fuente = pygame.font.Font("freesansbold.ttf", 32)
texto_x = 10
texto_y = 10

# teclas
tecla_derecha = pygame.K_RIGHT
tecla_izquierda = pygame.K_LEFT


# funcion jugador
def posicion_jugador(x, y):
    pantalla.blit(imagen_nave, (x, y))


# funcion jugador
def posicion_enemigo(x, y, ene):
    pantalla.blit(imagen_enemigo[ene], (x, y))


def disparar_bala(x, y):
    global bala_visible
    bala_visible = True
    pantalla.blit(imagen_bala,(x + 16, y + 10)) # se les suman valores a la posición recibida para que no aparezan en la misma posición de la nave, sino un poco más arriba/centrado


# función detectar colicisiones
def hay_colision(x_1,y_1,x_2,y_2):
    x2__menos_x_1_todo_al_cuadrado = math.pow(x_2 - x_1, 2)
    y_2_menos_y_1_todo_al_cuadrado = math.pow(y_2 - y_1, 2)
    distancia = math.sqrt(x2__menos_x_1_todo_al_cuadrado + y_2_menos_y_1_todo_al_cuadrado)
    if distancia < 27:
        return True
    else:
        return False

def mostrar_puntaje(x,y):
    texto = fuente.render(f"Puntaje: {puntaje}",True,(255,255,255))
    pantalla.blit(texto,(x,y))


# texto final de juego
fuente_final = pygame.font.Font("freesansbold.ttf", 64)
def texto_final():
    mi_fuente = fuente_final.render("JUEGO TERMINADO",True,(255,255,255))
    pantalla.blit(mi_fuente,(60,200))


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
                sonido_bala = mixer.Sound("audio/disparo.mp3")

                if not bala_visible:
                    bala_x = jugador_x
                    sonido_bala.play()
                    disparar_bala(bala_x,bala_y)
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
    for enemigo in range(cantidad_enemigos):
        # fin del juego
        if enemigo_y[enemigo] > 500:
            for k in range(cantidad_enemigos):
                enemigo_y[k] = 1000
            texto_final()
            break

        enemigo_x[enemigo] += posicion_enemigo_x_cambio[enemigo]
    # mantener dentro de bordes jugador
        if enemigo_x[enemigo] <= borde_izquierdo:  # si toca el borde izquierdo cambia su dirección a la derecha
            posicion_enemigo_x_cambio[enemigo] = se_mueve_a_la_derecha
            enemigo_y[enemigo] += posicion_enemigo_y_cambio[enemigo]
        elif enemigo_x[enemigo] >= borde_derecho:  # si toca el borde derecho cambia su dirección a la izquierda
            posicion_enemigo_x_cambio[enemigo] = se_mueve_a_la_izquierda
            enemigo_y[enemigo] += posicion_enemigo_y_cambio[enemigo]
        # colisión
        colision = hay_colision(enemigo_x[enemigo], enemigo_y[enemigo], bala_x, bala_y)
        if colision:
            sonido_colision = mixer.Sound("audio/Golpe.mp3")
            sonido_colision.play()
            # la bala se situa nuevamente a la posición y del jugador
            bala_y = 500
            bala_visible = False
            puntaje += 1
            #print(puntaje)
            enemigo_x[enemigo] = random.randint(0, 736)
            enemigo_y[enemigo] = random.randint(50, 200)
        # aparición de enemigo
        posicion_enemigo(enemigo_x[enemigo], enemigo_y[enemigo],enemigo)

    # movimiento bala
    if bala_y <= -24:
        bala_y = 500
        bala_visible = False
    if bala_visible:
        disparar_bala(bala_x,bala_y)
        bala_y -= posicion_bala_y_cambio



    posicion_jugador(jugador_x,jugador_y)
    mostrar_puntaje(texto_x,texto_y)

    # Actualizar pantalla
    pygame.display.update()
