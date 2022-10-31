# differential evolution global optimization for the ackley multimodal objective function
from scipy.optimize import differential_evolution
from numpy.random import rand
from numpy import sin

# objective function
def objective(f):
    x1, x2 = f
    return 3 * x1 + 0.000001 * x1 ** 3.0 + 2 * x2 + (0.000002 / 3) * x2
#def restricciones(x):
    #x1,x2,x3,x4 =x
   # return x1 >= 0, x1 <= 1200, x2 >= 0, x2 <= 1200
    # x3 >= -0.55, x3 <= 0.55, x4 >= -0.55, x4 <= 0.55

# define range for input
r_min, r_max = -5.0, 5.0
# define the bounds on the search
bounds = [[r_min, r_max], [r_min, r_max]]
# perform the differential evolution search
result = differential_evolution(objective, bounds)
# summarize the result
print('Status : %s' % result['message'])
print('Total Evaluations: %d' % result['nfev'])
# evaluate solution
solution = result['x']
evaluation = objective(solution)
print('Solution: f(%s) = %.5f' % (solution, evaluation))