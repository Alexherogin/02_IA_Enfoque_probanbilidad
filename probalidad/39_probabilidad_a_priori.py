

def priori(dados):
    numeros = int(input('escoja el numero de veses que desea tirar el dado: '))

    proba_i=1/numeros
    return proba_i

numero_buscado =int(input('escoja un numero del 1 al 6 : '))

proba = priori(numero_buscado)
print(f'la probabilidad de que salga el numero {numero_buscado} es de {proba}')