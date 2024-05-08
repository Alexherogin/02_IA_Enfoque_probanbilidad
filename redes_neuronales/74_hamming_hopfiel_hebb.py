import numpy as np

# Red de Hamming
def hamming_correction(pattern):
    weights = np.outer(pattern, pattern)
    noisy_pattern = pattern.copy()
    noisy_pattern[2] = 0
    return np.sign(np.dot(weights, noisy_pattern))

# Ejemplo de uso
pattern_hamming = np.array([1, 0, 1, 0, 1])
print("Red de Hamming - Patron corregido:", hamming_correction(pattern_hamming))

# Red de Hopfield
def hopfield_update(weights, noisy_pattern, iterations=10):
    for _ in range(iterations):
        noisy_pattern = np.sign(np.dot(weights, noisy_pattern))
    return noisy_pattern

# Ejemplo de uso
pattern_hopfield1 = np.array([1, 0, 1, 0, 1])
pattern_hopfield2 = np.array([1, 1, 0, 1, 0])
weights_hopfield = np.outer(pattern_hopfield1, pattern_hopfield1) + np.outer(pattern_hopfield2, pattern_hopfield2)
noisy_hopfield = np.array([1, 0, 0, 1, 1])
print("Red de Hopfield - Patron corregido:", hopfield_update(weights_hopfield, noisy_hopfield))

# Regla de Hebb
def hebb_weights(pattern1, pattern2):
    return np.outer(pattern1, pattern1) + np.outer(pattern2, pattern2)

# Ejemplo de uso
pattern_hebb1 = np.array([1, 0, 1])
pattern_hebb2 = np.array([1, 1, 0])
print("Regla de Hebb - Matriz de pesos:", hebb_weights(pattern_hebb1, pattern_hebb2))

# Maquina de Boltzmann (capa oculta)
def boltzmann_hidden_layer(input_pattern, weights):
    return np.sign(np.dot(input_pattern, weights))

# Ejemplo de uso
pattern_boltzmann = np.array([1, 0, 1])
weights_boltzmann = np.random.randn(3, 4)
print("Maquina de Boltzmann - Salida de la capa oculta:", boltzmann_hidden_layer(pattern_boltzmann, weights_boltzmann))
