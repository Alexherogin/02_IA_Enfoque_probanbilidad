

import numpy as np

matriz = np.array([[0.7,0.2,0.1],   
                   [0.3,0.4,0.3],
                   [0.1,0.6,0.3]])

star = 0

pasos = 10 

actual = star

print('secuencia  markov: ')

for _ in range(pasos):
    print(actual , end = '')
    actual = np.random.choice([1,2,3], p=matriz[actual])