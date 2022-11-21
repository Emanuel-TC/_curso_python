import numpy as np
from numpy import *
from numpy.random import choice


# definimos la función objetivo.
def funcion_objetivo(funcion):
    x1, x2, x3, x4 = funcion[0], funcion[1], funcion[2], funcion[3]
    resultado = (3 * x1 + (0.000001 * x1) ** 3.0) + (2 * x2 + ((0.000002 / 3) * x2) ** 3.0)
    return resultado, x1, x2, x3, x4


def restriccion_g_uno(vector_solucion):
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_g_uno = (-x4 + x3 - 0.55)
    return resultado_g_uno


def restriccion_g_dos(vector_solucion):
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_g2 = (-x3 + x4 - 0.55)
    return resultado_g2


def restriccion_h_tres(vector_solucion):
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_h3 = (1000 * math.sin(-x3 - 0.25) + 1000 * math.sin(-x4 - 0.25) + 894.8 - x1)
    return resultado_h3


def restriccion_h_cuatro(vector_solucion):
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_h4 = (1000 * math.sin(x3 - 0.25) + 1000 * math.sin(x3 - x4 - 0.25) + 894.8 - x2)
    return resultado_h4


def restriccion_h_cinco(vector_solucion):
    x1, x2, x3, x4 = vector_solucion[0], vector_solucion[1], vector_solucion[2], vector_solucion[3]
    resultado_h5 = (1000 * math.sin(x4 - 0.25) + 1000 * math.sin(x4 - x3 - 0.25) + 1294.8)
    return resultado_h5


def suma_restricciones(*args):
    total = 0
    for arg in args:
        total = sum(arg)
    return total

'''def mutacion(vector_uno, vector_dos, vector_tres, F):
    return vector_uno + F * (vector_dos - vector_tres)'''

def revisarLimites(vector_mutado, limites):
    nuevo_vector = []
    # realizar por cada elemento del vector
    for i in range(len(vector_mutado)):

        # si la variable excede los límites inferiores
        if vector_mutado[i] < limites[i][0]:
            nuevo_vector.append(limites[i][0])

        # si la variable excede los limites superiores
        if vector_mutado[i] > limites[i][1]:
            nuevo_vector.append(limites[i][1])

        # si la varibale está dentro de los limites
        if limites[i][0] <= vector_mutado[i] <= limites[i][1]:
            nuevo_vector.append(vector_mutado[i])
    return nuevo_vector

def evolucion_diferencial(tamanio_de_poblacion, limites, iter, F, cr):
    # lo primero que se debe hacer es crear una población con valores aleatorios:
    # lo podemos hacer con el siguiente código:
    poblacion = []  # creamos un arreglo vació llamado poblacion
    for i in range(0,
                   tamanio_de_poblacion):  # definimos el número de vectores a crear, en este caso, siempre lo define el tamanio de la poblacion
        vector = []
        for j in range(len(limites)):  # definimos el número de columnas o bien, dimension del vector
            vector.append(random.uniform(limites[j][0], limites[j][1]))  # lo llenamos con un valor flotante entre el limite inferior y el limite superior, iterando en cada índice de los limites designados
        poblacion.append(vector)  # y lo añadimos al arreglo

    '''for vector in poblacion: #si quieres ver el arreglo sólo ejecuta este código
        print(vector)'''

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

    # ejecutar iteraciones del algoritmo
    for i in range(numero_de_iteraciones):
        # iterar sobre todas las soluciones candidatas
        for j in range(tamanio_de_poblacion):
            #elegir tres candidatos, a, b y c, que no sean el actual
            vectores_candidatos = list(range(0, tamanio_de_poblacion))
            # vectores_candidatos.remove(j)
            vector_actual = vectores_candidatos.pop(j)
            random_index = random.sample(vectores_candidatos, 3)

            x_1 = poblacion[random_index[0]]
            x_2 = poblacion[random_index[1]]
            x_3 = poblacion[random_index[2]]
            x_t = poblacion[j]  # target individual

            # realizar mutación
            # El proceso de mutación lo realizamos por partes:
            # primeor la resta de x2-x3
            resta_x = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]

            # luego lo multiplicamos por el factor de mutacion F, y le sumamos el vector x1
            vector_mutado = [x_1_i + F * resta_x_i for x_1_i, resta_x_i in zip(x_1, resta_x)]
            print(f"El vector mutado: {vector_mutado}")

            ''''# comprobamos que los límites inferior y superior se conservan después de la mutación
            vectores_mutados = revisarLimites(vectores_mutados, limites)'''





numero_de_iteraciones = 100
F = 0.9
limites = np.array([[0.0, 1200.0], [0.0, 1200.0], [-0.55, 0.55], [-0.55, 0.55]])
