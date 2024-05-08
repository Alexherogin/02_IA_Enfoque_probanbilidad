import numpy as np

# Datos de entrada y salida (ejemplo simple de compuerta XOR)
entradas = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
salidas = np.array([[0], [1], [1], [0]])

# Inicialización de pesos y sesgos
num_entradas = 2
num_ocultas = 4
num_salidas = 1

pesos_ocultos = np.random.randn(num_entradas, num_ocultas)
sesgo_oculto = np.zeros((1, num_ocultas))
pesos_salida = np.random.randn(num_ocultas, num_salidas)
sesgo_salida = np.zeros((1, num_salidas))

# Función de activación (sigmoide)
def sigmoide(x):
    return 1 / (1 + np.exp(-x))

# Derivada de la función de activación (para retropropagación)
def derivada_sigmoide(x):
    return x * (1 - x)

# Hiperparámetros
tasa_aprendizaje = 0.1
epocas = 10000

# Entrenamiento de la red neuronal
for epoca in range(epocas):
    # Propagación hacia adelante (forward pass)
    entrada_oculta = np.dot(entradas, pesos_ocultos) + sesgo_oculto
    salida_oculta = sigmoide(entrada_oculta)
    entrada_salida = np.dot(salida_oculta, pesos_salida) + sesgo_salida
    salida_salida = sigmoide(entrada_salida)

    # Cálculo del error
    error = salidas - salida_salida

    # Retropropagación
    d_salida = error * derivada_sigmoide(salida_salida)
    error_oculta = d_salida.dot(pesos_salida.T)
    d_oculta = error_oculta * derivada_sigmoide(salida_oculta)

    # Actualización de pesos y sesgos
    pesos_salida += salida_oculta.T.dot(d_salida) * tasa_aprendizaje
    sesgo_salida += np.sum(d_salida, axis=0, keepdims=True) * tasa_aprendizaje
    pesos_ocultos += entradas.T.dot(d_oculta) * tasa_aprendizaje
    sesgo_oculto += np.sum(d_oculta, axis=0, keepdims=True) * tasa_aprendizaje

# Predicciones
predicciones = np.round(salida_salida)
print("Predicciones:")
print(predicciones)
