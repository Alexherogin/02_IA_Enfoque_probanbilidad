import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))
x= 2.0
res=sigmoid(x)
print(f'sigmoif fr {x} es : {res}')

def tangente(x):
    return np.tan(x)

x= 2.0
res=tangente(x)
print(f'tangente fr {x} es : {res}')

def max(x):
    plus_x=np.exp(x-np.max(x))
    return plus_x/np.sum(plus_x)
x= np.array([2.0,1.0,0.1])

res=max(x)
print(f'max fr {x} es : {res}')