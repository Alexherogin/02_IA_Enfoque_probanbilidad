import numpy as np


def sigmoid(x):
    return 1/(1+np.exp(-x)) 

class red:
    def __init__(self):
        np.random.seed(1)
        self.peso =2*np.random.random((3,1))-1

    def entr(self, entradas, salida,interaciones):
        for _ in range(interaciones):
            in_lay= entradas
            salida_n= self.pre(in_lay)
            error= salida-salida_n
            delta = np.dot(in_lay.T, error * salida_n* (1 - salida_n))
            self.peso += delta
    def pre(self,entradas):
        return sigmoid(np.dot(entradas,self.peso))

entrada_entr=np.array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
salida_entr=np.array([[0, 1, 1, 0]]).T

red=red()
red.entr(entrada_entr,salida_entr,15000)

print(f'predicciones del entrenamien { red.pre(np.array([1,0,0]))}')