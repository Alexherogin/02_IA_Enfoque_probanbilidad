
import numpy as np
from hmmlearn import hmm
#conjuntos de datos
observa = np.array([[0,1,0,1,0],#lista de secuencia binaria
                    [1,0,1,0,1]
                    ])

estados_ocultos = 2#se crea emicion gaussianas
modelo=hmm.GaussianHMM(n_components= estados_ocultos,n_iter=100)

modelo.fit(observa)#se aplica el algoritmo adelante atras

tranciciones=modelo.transmat_
emicion= modelo.means_

print(f'probabilidad de trancicion : {tranciciones}')
print(f'probabilidad de emicion : {emicion}')
