from numpy.random import choice
import numpy as np
from numpy import *
import random
# definimos la función objetivo.
def funcion_objetivo(vector):
    x1, x2, x3, x4 = vector[0], vector[1], vector[2], vector[3]
    resultado = (3 * x1 + (0.000001 * x1) ** 3.0) + (2 * x2 + ((0.000002 / 3) * x2) ** 3.0)
    return resultado, x1, x2, x3, x4
def restriccion_g_uno(vector_solucion):
    epsilon = 0.0001
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_g_uno = max(0, -x4 + x3 - 0.55 - epsilon)
    return resultado_g_uno
def restriccion_g_dos(vector_solucion):
    epsilon = 0.0001
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_g2 = max(0, -x3 + x4 - 0.55 - epsilon)
    return resultado_g2
def restriccion_h_tres(vector_solucion):
    epsilon = 0.0001
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_h3 = max(0, 1000 * math.sin(-x3 - 0.25) + 1000 * math.sin(-x4 - 0.25) + 894.8 - x1 - epsilon)
    return resultado_h3
def restriccion_h_cuatro(vector_solucion):
    epsilon = 0.0001
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_h4 = max(0, 1000 * math.sin(x3 - 0.25) + 1000 * math.sin(x3 - x4 - 0.25) + 894.8 - x2-epsilon)
    return resultado_h4
def restriccion_h_cinco(vector_solucion):
    epsilon = 0.0001
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_h5 = max(0, 1000 * math.sin(x4 - 0.25) + 1000 * math.sin(x4 - x3 - 0.25) + 1294.8-epsilon)
    return resultado_h5
def suma_restricciones(*args):
    total = 0
    for arg in args:
        total = sum(arg)
    return total
def genera_poblacion(tamanio_de_poblacion, limites):
    poblacion = []  # creamos un arreglo vació llamado poblacion
    for i in range(0,tamanio_de_poblacion):  # definimos el número de vectores a crear, en este caso, siempre lo define el tamanio de la poblacion
        vector = []
        for j in range(len(limites)):  # definimos el número de columnas o bien, dimension del vector
            vector.append(random.uniform(limites[j][0], limites[j][1]))  # lo llenamos con un valor flotante entre el limite inferior y el limite superior, iterando en cada índice de los limites designados
        poblacion.append(vector)  # y lo añadimos al arreglo
    return poblacion

def ajusta_limites(vector_mutado,limites):
    for i in range(len(vector_mutado)):
        while vector_mutado[i] < limites[i][0] or vector_mutado[i] > limites[i][1]:
            # si la variable excede los límites inferiores
            if vector_mutado[i] < limites[i][0]:
                vector_mutado[i] = limites[i][0] * 2 - vector_mutado[i]

            # si la variable excede los limites superiores
            if vector_mutado[i] > limites[i][1]:
                vector_mutado[i] = limites[i][1] * 2 - vector_mutado[i]
    return vector_mutado
def mutacion(vector_uno, vector_dos, vector_tres,F):
    # El proceso de mutación lo realizamos por partes:
    # primero la resta de x2-x3
    resta_x = [vector_dos_i - vector_tres_i for vector_dos_i, vector_tres_i in zip(vector_dos, vector_tres)]
    # luego lo multiplicamos por el factor de mutacion F, y le sumamos el vector x1
    vector_mutado = [vector_uno_i + F * resta_x_i for vector_uno_i, resta_x_i in zip(vector_uno, resta_x)]
    return vector_mutado
def cruza(vector_target, vector_mutado,cr):
    vector_trial = []
    # se realizará por cada elemento del vector tarjet
    for k in range(len(vector_target)):
        cruza = random.random()
        # el proceso de cruza ocurre cuando el valor generado aleatoriamente es menor
        # o igual al valor de la tasa de cruza
        if cruza <= cr:
            vector_trial.append(vector_mutado[k])

        # si no es así, entonces no se hace la cruza
        else:
            vector_trial.append(vector_target[k])
    return vector_trial

def evolucion_diferencial(tamanio_de_poblacion, limites, iteraciones, F, cr):
    # lo primero que se debe hacer es crear una población con valores aleatorios:
    # lo podemos hacer con el siguiente código:
    poblacion = genera_poblacion(tamanio_de_poblacion, limites)

    #Evaluamos cada individuo de la poblacion
    soluciones_candidatas = []
    valores_individuo_candidato = []
    for index, vector in enumerate(poblacion):
        valor_vector_candidato, x1, x2, x3, x4 = funcion_objetivo(vector)
        soluciones_candidatas.append([valor_vector_candidato])
        valores_individuo_candidato.append([x1, x2, x3, x4])

    #Encuentre el mejor vector de rendimiento de la población inicial.
    mejor_vector = poblacion[argmin(soluciones_candidatas)]
    mejor_resultado = min(soluciones_candidatas)
    resultado_anterior = mejor_resultado
    print(f"El mejor vector es: {mejor_vector} y el mejor resultado es: {resultado_anterior}")

    # ejecutar iteraciones del algoritmo
    i = 0
    vectores_candidatos = []
    while i in range(iteraciones):
        i += 1
        total_generacion = []
        # iterar sobre todas las soluciones candidatas
        for j in range(tamanio_de_poblacion):
            #elegir tres candidatos, a, b y c, que no sean el actual
            vectores_candidatos = list(range(0, tamanio_de_poblacion))
            vector_actual = vectores_candidatos.pop(j)
            random_index = random.sample(vectores_candidatos, 4)

            x_1 = valores_individuo_candidato[random_index[0]]
            x_2 = valores_individuo_candidato[random_index[1]]
            x_3 = valores_individuo_candidato[random_index[2]]
            x_t = valores_individuo_candidato[random_index[3]]  # target individual

            # realizar mutación
            vector_mutado = mutacion(x_1,x_2,x_3,F)
            #print(f"El vector mutado {vector_mutado}")
            '''Corroboramos que los limites estén dentro de los rangos establecidos
            de los contrario se le aplica
            una modificación para controlar los limites'''
            vector_mutado = ajusta_limites(vector_mutado, limites)
            #print(f"El vector mutado revisado {vector_mutado}")

            # Procedemos a realizar la cruza
            vector_trial = cruza(x_t,vector_mutado,cr)

            total_trial = funcion_objetivo(vector_trial)[0]
            total_target = funcion_objetivo(x_t)[0]

            if total_trial < total_target:
                poblacion[j] = vector_trial
                total_generacion.append(total_trial)
                #print(f"El total de trial es: {total_trial}, y el total de target es: {total_target}")

            else:
                #print(f"El total de target es: {total_target}")
                total_generacion.append(total_target)

        print(f"El total de trial {i} es: {total_trial}, y el total de target es: {total_target}")
        #print(f"El total de target {i} es: {total_target}")

        aptitud_mejor_valor = min(total_generacion)  # aptitud del mejor valor
        sol = poblacion[argmin(total_generacion)] # solucion mejor individuo
    print(f"El valor del vector solucion es: {aptitud_mejor_valor}")
    print(f"El vector óptimo es:{sol}")


tamanio_de_poblacion = 100
numero_de_iteraciones = 100
F = 0.9
cr = 0.5
limites = np.array([[0.0, 1200.0], [0.0, 1200.0], [-0.55, 0.55], [-0.55, 0.55]])
evolucion_diferencial(tamanio_de_poblacion,limites,numero_de_iteraciones,F, cr)