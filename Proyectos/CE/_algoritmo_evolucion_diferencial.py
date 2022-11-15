from numpy.random import rand
from numpy.random import choice
from numpy import asarray
from numpy import clip
from numpy import argmin
from numpy import min
from numpy import around
import math

def restricciones(solucion):
    g1 = -solucion[3] + solucion[2] -0.55
    g2 = solucion[3] - solucion[2] - 0.55
    return g1,g2
    #-x4 +x3 -0.55
    #[0,1,2,3]

# definimos la función objetivo
def funcionObjetivo(funcion):
    # return 0
    x1, x2, x3, x4 = funcion[0], funcion[1], funcion[2], funcion[3]
    resultado = (3 * x1 + 0.000001 * x1 ** 3.0) + (2 * x2 + (0.000002/3) * x2 ** 3.0)
    resultado_g1 = resultado + (-x4 + x3 - 0.55)
    resultado_g2 = resultado_g1 + (-x3 + x4 - 0.55)

    resultado_h3 = resultado_g2 + (1000*math.sin(-x3-0.25) + 1000*math.sin(-x4-0.25) + 894.8 - x1)
    resultado_h4 = resultado_h3 + (1000*math.sin(x3-0.25) + 1000*math.sin(x3 - x4 - 0.25) + 894.8 - x2)
    resultado_h5 = resultado_h4 + (1000*math.sin(x4-0.25) + 10000*math.sin(x4 - x3 - 0.25) + 1294.8)
    resultado_final = resultado_h5
    return resultado_final


# definimos la operación de mutación
def mutacion(x, F):
    return x[0] + F * (x[1] - x[2])


# el operador de mutacion consiste en una diferencia
# aritmetica entre pares de vectores seleccionados aleatoriamente
# normalnte F es 0<F>2


#################CON LIMITES#########################################################################
def revisarLimites(vectores_mutados, limites):
    limiteMutado = [clip(vectores_mutados[i], limites[i, 0], limites[i, 1]) for i in range(len(limites))]
    return limiteMutado


##################CON LIMITES########################################################################

# definimos la operación de cruza
def cruza(vectoresMutados, target, nVariablesDeEntrada, cr):  # cr es 0<= cr <= 1
    # generamos un valor aleatorio uniforme para variable de entrada
    p = rand(nVariablesDeEntrada)
    # generamos vector de target por cruza binomial
    trial = [vectoresMutados[i] if p[i] < cr else target[i] for i in range(nVariablesDeEntrada)]
    return trial


def evolucion_diferencial(tamanio_de_poblacion, limites, iter, F, cr):
    # inicializar la población aleatoria de soluciones candidatas dentro de los límites especificados
    poblacion = limites[:, 0] + (rand(tamanio_de_poblacion, len(limites)) * (limites[:, 1] - limites[:, 0]))

    # evaluar nuestra población inicial de soluciones candidatas
    solucionesCandidatas = [funcionObjetivo(poblacionInicial) for poblacionInicial in poblacion]

    # Encuentre el mejor vector de rendimiento de la población inicial.
    mejor_vector = poblacion[argmin(solucionesCandidatas)]
    mejor_obj = min(solucionesCandidatas)
    anterior_obj = mejor_obj

    #  ejecutar iteraciones del algoritmo
    for i in range(iter):
        # iterar sobre todas las soluciones candidatas
        for j in range(tamanio_de_poblacion):
            # elegir tres candidatos, a, b y c, que no sean el actual
            candidatos = [candidato for candidato in range(tamanio_de_poblacion) if candidato != j]
            a, b, c = poblacion[choice(candidatos, 3, replace=False)]

            # realizar mutación
            vectores_mutados = mutacion([a, b, c], F)

            # comprobamos que los límites inferior y superior se conservan después de la mutación
            vectores_mutados = revisarLimites(vectores_mutados, limites)

            # Realizar cruza
            trial = cruza(vectores_mutados, poblacion[j], len(limites), cr)

            # calcular el valor de la función objetivo para el vector objetivo
            vectorObjetivo = funcionObjetivo(poblacion[j])
            # calcular el valor de la función objetivo para el vector de prueba
            vectorPrueba = funcionObjetivo(trial)
            # realizar selección
            if vectorPrueba < vectorObjetivo:
                # reemplace el vector objetivo con el vector de prueba
                poblacion[j] = trial
                # almacenar el nuevo valor de la función objetivo
                solucionesCandidatas[j] = vectorPrueba

        # encontrar el vector de mejor rendimiento en cada iteración
        mejor_obj = min(solucionesCandidatas)
        # almacena el valor más chico de la función objetivo
        if mejor_obj < anterior_obj:
            mejor_vector = poblacion[argmin(solucionesCandidatas)]
            anterior_obj = mejor_obj
            # reporta el progreso en cada iteración
            print('Iteracion: %d f([%s]) = %.5f' % (i, around(mejor_vector, decimals=18), mejor_obj))

    return [mejor_vector, mejor_obj]


###########################################Evolucion Diferencial##############################################

# Definimos tamaño de la poblacion
tamanio_de_poblacion = 100
# Definimos límites inferior y superior para cada dimensión
limites = asarray([(0.0, 1200.0), (0.0, 1200.0), (-0.55, 0.55), (-0.55, 0.55)]) #el arreglo de limites son las restricciones de cada x abajo
# definimos el número de iteraciones
iter = 1000
# definimos el factor de escala de mutación
# normalnte F es 0<F>2
F = 0.5

# definimos la tasa de cruce para la recombinación
cr = 0.7

solucion_con_restricciones = []

# Buscamos una solucion de la funcion objetivo con evolucion diferencial
solucion = evolucion_diferencial(tamanio_de_poblacion, limites, iter, F, cr)



print('\nLa solucion de optimizar funcion es: f([%s]) = %.5f' % (around(solucion[0], decimals=18), solucion[1]))