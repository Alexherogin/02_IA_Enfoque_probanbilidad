#

import numpy as np
import matplotlib.pyplot as plt

#parametrso de distribucion 

media = 5 # media de distribucion

d_estandar = 2 

#generacion de datos
numeros= 1000
datos = np.random.normal(media,d_estandar,numeros)

#calculos de los datos

m_datos = np.mean(datos)
D_esta_date = np.std(datos)
diferencia_datos = np.var(datos)

#

plt.hist(datos, bins =30 , density=True , alpha=0.6, color='g')
plt.title('Histograma de datos')
plt.xlabel('Datos')
plt.ylabel('Frecuencia')# 
plt.grid(True)

print(f'la media de datos es: {m_datos}')
print(f'la desviacion estandar de datos es: {D_esta_date}')
print(f'la diferencia de datos es: {diferencia_datos}')

plt.show()