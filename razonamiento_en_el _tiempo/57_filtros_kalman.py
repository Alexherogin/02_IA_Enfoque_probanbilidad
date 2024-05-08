

import numpy as np
from scipy.linalg import inv

A=np.array([[1,1],[0,1]])# matriz de estado
H=np.array([[0,1]])#matriz observacion
Q=np.array([[0.0001,0],[0,0.0001]])#ruido del sistema
R=np.array([[1]])#ruido de la ob¿bservacion

X = np.array([[0,0]])# estado inicial
Y =np.array([[1,0],[0,1]])
obser= np.array([1.1,2.0,2.9,4.0])
for i in obser:#prediccion
    x = np.dot( A,x) + np.dot(H,i)
    p = np.dot(A,np.dot(p,A.T)) + Q

    y = z - np.dot(H, x)#actiaizaciones
    S = np.dot(np.dot(H, P), H.T) + R
    K = np.dot(np.dot(P, H.T), inv(S))
    x = x + np.dot(K, y)
    P = np.dot((np.eye(2) - np.dot(K, H)), P)
    print(f'posicion estimada :{x[0][0]:2f},velocidad estimada {x[1][0]:2f}')
    print(f'matriz  final es {p}')