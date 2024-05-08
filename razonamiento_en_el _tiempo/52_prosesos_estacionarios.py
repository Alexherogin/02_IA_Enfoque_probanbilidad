

import numpy as np
import matplotlib.pyplot as plt

n= int(input('ingrese los numeros de pasos que quiera aplicar: '))
pasos= 0.0 
descios= 1.0

recorrido = np.random.normal(pasos,descios, n)
caminar = np.cumsum(recorrido)

plt.plot(caminar)
plt.title('ruta alatoria hecha')
plt.xlabel('pasos')
plt.ylabel('distancia')

plt.show()
