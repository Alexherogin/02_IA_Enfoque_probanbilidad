
import numpy as np
from hmmlearn import hmm
observa = np.array([[0,1,0,1,0],
                    [1,0,1,0,1]
                    ])

estados_ocultos = 2
modelo=hmm.GaussianHMM(n_components= estados_ocultos,n_iter=10)

modelo.fit(observa)

tranciciones=modelo.transmat_
emicion= modelo.means_

print(f'probabilidad de trancicion : {tranciciones}')
print(f'probabilidad de emicion : {emicion}')
