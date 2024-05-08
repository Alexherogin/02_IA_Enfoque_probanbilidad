

import numpy as np

matriz = np.array([[0.7,0.3],
                   [0.6,0.4]])


star = np.array([0.5,0.5])

pasos= 1000 
actual = star.copy()

for _ in range(pasos):
    actual = np.dot(matriz,actual)

print (f'probabilidad de A es {actual[0]}')
print (f'probabilidad de B es {actual[1]}')