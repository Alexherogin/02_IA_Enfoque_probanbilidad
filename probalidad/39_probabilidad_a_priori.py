

def priori(dados):
    # Solicitar al usuario el número de veces que desea tirar el dado
    numeros = int(input('escoja el numero de veses que desea tirar el dado: '))
# Calcular la probabilidad a priori como 1 dividido entre el número de veces que se tira el dado
    proba_i=1/numeros
    return proba_i
# Solicitar al usuario que elija un número del 1 al 6

numero_buscado =int(input('escoja un numero del 1 al 6 : '))

proba = priori(numero_buscado)
print(f'la probabilidad de que salga el numero {numero_buscado} es de {proba}')