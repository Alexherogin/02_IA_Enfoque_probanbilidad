
# 
def dado(numeros_d):
    if numeros_d>6 or numeros_d < 1: # Verifica si el número ingresado está fuera del rango válido (1-6)
        raise ValueError('el dado solo es de 6')
    posible=6   # Asigna el número de caras del dado (6)
    prova_i=1/posible# Calcula la probabilidad de obtener un número en particular (1/6)
    return prova_i

numeros_d_1= int(input('escoja la cara del dado 1: '))# se agrega el numero que se quiere saber la probabilidad
if numeros_d_1 > 6 or numeros_d_1<1:
    print('el dado solo es de 6')
numeros_d_2=int(input('escoja la cara del dado 2: '))#se agrega el numero que se quiere saber la probabilidad
if numeros_d_2 > 6 or numeros_d_2<1:
    print('el dado solo es de 6')

proba_A=dado(numeros_d_1)#se llama la funcion del dado con el valor que se escoji de la caras dado 1 
proba_B=dado(numeros_d_2)#se llama la funcion del dado con el valor que se escoji de la caras dado 2

proba_A_B=proba_A*proba_B #se multiplica los valores  de a y b  y el resultado se guarda en una variable 

# imprime resultados
print(f'la probabilidad de obtener  el numero:{numeros_d_1} es de {proba_A}')
print(f'la probabilidad de obtener  el numero:{numeros_d_2} es de {proba_B}')
print(f'la probabilidad de obtener ambos es de : {proba_A_B}')