

import numpy as np
import matplotlib.pyplot as plt

np.random.seed(52)
n = int(input('ingrese la cantidad de tiempo que dese: '))
t = np.arange(n)
ruido =np.random.normal(loc=0, scale=1,size=n)
tiempo = 0.5*t+ruido

ventana = 5

serie_suavidad= np.convolve(tiempo,np.ones(ventana)/ventana,mode='valido')

ultimo_Valor= tiempo[-1]
ultimo= np.std(tiempo)
predicion= np.random.normal(loc=ultimo_Valor,scale= ultimo)

plt.figure(figsize=(10,7))
plt.plot(t,tiempo,label='Tiempo')
plt.plot(t[ventana -1:],serie_suavidad,label='Suavidad')
plt.axvline(x=n, color='green',linestyle='--',label='prediccion')
plt.scatter(n,predicion,color='green',marker='o')
plt.xlabel('tiempo')
plt.ylabel('valor')
plt.legend()
plt.title('filtrad,predicicon y suavidad')
plt.grid()
plt.show()


print(f'proxim valor : {predicion}')
