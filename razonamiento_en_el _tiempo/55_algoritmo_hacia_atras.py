

def delante_atras(inicio_p,paso_adelante,pasos_atras,paso):

    probabilidad= inicio_p
    for _ in range(paso):
        nuevo = [0]*len(probabilidad)
        for i in range(len(probabilidad)):
            for j in range(len(paso_adelante[i])):
                nuevo[j] += probabilidad[1]*paso_adelante[i][j]
            for k in range(len(paso_adelante[i])):
                nuevo[k] += probabilidad[i]*pasos_atras[i][k]
        probabilidad=nuevo
    return probabilidad
inicio_p=[0.5,0.5]
paso_adelante=[[0.8,0.2],[0.4,0.6]]

pasos_atras=[[0.3,0.7],[0.1,0.9]]
paso=int(input('Agrege el numero de pasos para interactuar : '))

res = delante_atras(inicio_p,paso_adelante,pasos_atras,paso)

print(f'las probabilidads de {paso}pasos son:')
for i , prob in enumerate(res):
    print(f'Pinteraciones{i}) = {prob}')