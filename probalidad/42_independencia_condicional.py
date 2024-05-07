
# 
def dado(numeros_d):
    if numeros_d>6 or numeros_d < 1:
        raise ValueError('el dado solo es de 6')
    posible=6 
    prova_i=1/posible
    return prova_i

numeros_d_1= int(input('escoja la cara del dado 1: '))
if numeros_d_1 > 6 or numeros_d_1<1:
    print('el dado solo es de 6')
numeros_d_2=int(input('escoja la cara del dado 2: '))
if numeros_d_2 > 6 or numeros_d_2<1:
    print('el dado solo es de 6')

proba_A=dado(numeros_d_1)
proba_B=dado(numeros_d_2)

proba_A_B=proba_A*proba_B

print(f'la probabilidad de obtener  el numero:{numeros_d_1} es de {proba_A}')
print(f'la probabilidad de obtener  el numero:{numeros_d_2} es de {proba_B}')
print(f'la probabilidad de obtener ambos es de : {proba_A_B}')