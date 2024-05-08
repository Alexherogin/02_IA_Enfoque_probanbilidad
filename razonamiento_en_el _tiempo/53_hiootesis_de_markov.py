

import numpy as np

matriz = np.array([[0.7,0.2,0.1],#se crea la matriz 
                   [0.3,0.4,0.3],
                   [0.1,0.4,0.5]])

star= 0 #inicionde los estados

pasos= int(input('cuantas simulaciones quiere hacer: '))

actual = star

for _ in range(pasos):
    print(actual, end='')
    actual = np.random.choice(3,p=matriz[actual])