from numpy.random import choice
import numpy as np
from numpy import *
import random



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

# definimos la operación de mutación
'''def mutacion(vector_uno,vector_dos, vector_tres, F):

    #print(f"Los vectores introducidos son el vector 1: {vector_uno}\nLos vectores introducidos son el vector 2: {vector_dos}\nLos vectores introducidos son el vector 3: {vector_tres}")
    return vector_uno + F * (vector_dos - vector_tres)'''

def evolucion_diferencial(tamanio_de_poblacion, limites, iter, F, cr):
    # lo primero que se debe hacer es crear una población con valores aleatorios:
    # lo podemos hacer con el siguiente código:
    poblacion = []  # creamos un arreglo vació llamado poblacion
    for i in range(0,
                   tamanio_de_poblacion):  # definimos el número de vectores a crear, en este caso, siempre lo define el tamanio de la poblacion
        vector = []
        for j in range(len(limites)):  # definimos el número de columnas o bien, dimension del vector
            vector.append(random.uniform(limites[j][0], limites[j][
                1]))  # lo llenamos con un valor flotante entre el limite inferior y el limite superior, iterando en cada índice de los limites designados
        poblacion.append(vector)  # y lo añadimos al arreglo

    '''for vector in poblacion: #si quieres ver el arreglo sólo ejecuta este código
        print(vector)'''

    # Evaluamos cada individuo de la poblacion
    soluciones_candidatas = []
    valores_individuo_candidato = []
    for index, vector in enumerate(poblacion):
        valor_vector_candidato, x1, x2, x3, x4 = funcion_objetivo(vector)
        soluciones_candidatas.append([valor_vector_candidato])
        valores_individuo_candidato.append([x1, x2, x3, x4])

    # Encuentre el mejor vector de rendimiento de la población inicial.
    mejor_vector = poblacion[argmin(soluciones_candidatas)]
    mejor_resultado = min(soluciones_candidatas)
    resultado_anterior = mejor_resultado

    # ejecutar iteraciones del algoritmo
    for i in range(numero_de_iteraciones):
        # iterar sobre todas las soluciones candidatas
        for j in range(tamanio_de_poblacion):
            # elegir tres candidatos, a, b y c, que no sean el actual
            candidatos = [candidato for candidato in range(tamanio_de_poblacion) if candidato != j]
            a, b, c = poblacion[choice(candidatos, 3, replace=False)]



tamanio_de_poblacion = 4
numero_de_iteraciones = 10

limites = np.array([[0.0, 1200.0], [0.0, 1200.0], [-0.55, 0.55], [-0.55, 0.55]])

poblacion = []

for i in range(0,tamanio_de_poblacion):
    indv = []
    for j in range(len(limites)):
        indv.append(random.uniform(limites[j][0],limites[j][1]))
    poblacion.append(indv)

'''for vector in poblacion:
    print(vector)'''

print("\n")
'''for vector in poblacion:
    vector_resultado, x1,x2,x3,x4 = funcion_objetivo(vector)
    valores_vector = [x1, x2, x3, x4]

    restriccion_uno = restriccion_g_uno(valores_vector)
    restriccion_dos = restriccion_g_dos(valores_vector)
    restriccion_tres = restriccion_h_tres(valores_vector)
    restriccion_cuatro = restriccion_h_cuatro(valores_vector)
    restriccion_cinco = restriccion_h_cinco(valores_vector)

    suma = suma_restricciones(restriccion_uno, restriccion_dos, restriccion_tres, restriccion_cuatro, restriccion_cinco)

    print(f"El valor del vector es: {vector_resultado}, sus valores son: {valores_vector} ")
    print(f"La suma de sus restricciones es: {suma}")

    print("\n")'''


'''for vector in poblacion:
    print(f"Los valores optimos del vector {vector} son: {funcion_objetivo(vector)} ")'''


soluciones_candidatas = []
valores_individuo_candidato = []
for index,vector in enumerate(poblacion):
    valor_vector_candidato,x1, x2, x3, x4 = funcion_objetivo(vector)
    soluciones_candidatas.append([valor_vector_candidato])
    valores_individuo_candidato.append([x1, x2, x3, x4])

mejor_vector = poblacion[argmin(soluciones_candidatas)]
mejor_resultado = min(soluciones_candidatas)
resultado_anterior = mejor_resultado
print(f"El mejor vector es {mejor_vector}, y el mejor resultado es : {resultado_anterior}")
F = 0.9
# ejecutar iteraciones del algoritmo
vectores_candidatos = []
for i in range(numero_de_iteraciones):
# iterar sobre todas las soluciones candidatas
    for j in range(tamanio_de_poblacion):
        # elegir tres candidatos, a, b y c, que no sean el actual
        vectores_candidatos = list(range(0, tamanio_de_poblacion))
        #vectores_candidatos.remove(j)
        vector_actual = vectores_candidatos.pop(j)
        random_index = random.sample(vectores_candidatos, 3)

        x_1 = poblacion[random_index[0]]
        x_2 = poblacion[random_index[1]]
        x_3 = poblacion[random_index[2]]
        x_t = poblacion[j]  # target individual

        # realizar mutación
        #El proceso de mutación lo realizamos por partes:
            #primeor la resta de x2-x3
        resta_x = [x_2_i - x_3_i for x_2_i, x_3_i in zip(x_2, x_3)]

        #luego lo multiplicamos por el factor de mutacion F, y le sumamos el vector x1
        vector_mutado = [x_1_i + F * resta_x_i for x_1_i, resta_x_i in zip(x_1, resta_x)]
        vector_mutado = revisarLimites(vector_mutado, limites)
        print(f"El vector mutado: {vector_mutado}")

        '''vectores_candidatos = [candidato for candidato in range(tamanio_de_poblacion) if candidato != j]
        vector_uno, vector_dos, vector_tres = poblacion[choice(vectores_candidatos, 3, replace=False)]'''
#print(f"El vector uno es {vector_uno}, y el vector dos es {vector_dos}, y el vector tres es : {vector_tres}")
print(f"El vector uno es: {x_1}, el vector dos es: {x_2}, el vector tres es: {x_3} y el vector target es: {x_t}")

print(f"El último vector mutado: {vector_mutado}")