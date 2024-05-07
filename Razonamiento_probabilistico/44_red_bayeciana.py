

class bayesiana:
    def __int__(self):
        self.nodos={}

    def varios_n(self,nombre, pa, proba,):
        self.nodos[nombre] = {'papa':pa,'probabilidad':proba }

    def calculo (self, nombre_n,valor):

        probabilidad= self.nodos[nombre_n]['probabilidad']
        probas = probabilidad[tuple(valor[padre] for padre in self.nodos[nombre_n]['padre'])]
        return  probas
    
red = bayesiana()

red.varios_n('a',[],{():0.3})
red.varios_n('b',[a],{(True):0.8 , (False):0.2})

proba_de_red = red.calculo('b',{'a':True})

print(f'la probabilidad seria que : {proba_de_red}')


