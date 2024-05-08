

import numpy as np
import matplotlib.pyplot as plt

n= int(input('ingrese los numeros de pasos que quiera aplicar: '))
pasos= 0.0 #medida de pasos empesando desde 0 
descios= 1.0#deesciacion de los pasos empesando en 1

recorrido = np.random.normal(pasos,descios, n) #genera  la secuencia para los pasos 
caminar = np.cumsum(recorrido)#calcula la trayectoria 
#modulo y funciones del plt que nos crea una grafica
plt.plot(caminar)
plt.title('ruta alatoria hecha')
plt.xlabel('pasos')
plt.ylabel('distancia')

plt.show()# se muestra la gradica creada10
