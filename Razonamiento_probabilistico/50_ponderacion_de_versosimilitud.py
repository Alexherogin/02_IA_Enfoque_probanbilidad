

import numpy as np
from scipy.optimize import minimize

datos_m = [10, 15, 8, 12, 20]

def verosimilitud(mu, datos):
    a = -mu * len(datos) + sum(y * np.log(mu) - np.log(np.math.factorial(y)) for y in datos)
    return a

def maximo_verosimilitud(datos):
    res = minimize(verosimilitud, 1, args=(datos,), method='Nelder-Mead')
    mejor_mu = res.x[0]
    return mejor_mu

mu_optimo = maximo_verosimilitud(datos_m)

print(f"Estimacion de mu (numero promedio de multimillonarios): {mu_optimo:.2f}")
