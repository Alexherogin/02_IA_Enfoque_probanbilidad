
import random

def lanzar_dado(): # Función para simular el lanzamiento de un dado
    dado = random.randint(1,6) # Genera un número aleatorio entre 1 y 6 (inclusivos)

    return dado

def sumular(tiradas): #Función para simular múltiples tiradas de un dado y calcular la frecuencia de cada resultado
    res ={1:0,2:0,3:0,4:0,5:0,6:0} #
    for _ in range(tiradas):
        resu = lanzar_dado()
        res[resu]+=1# Incrementa la frecuencia del resultado obtenido
        return res # Devuelve el diccionario con las frecuencia
    
tiradas = 1500 # Número de tiradas a simular
res = sumular(tiradas)# Realiza la simulación
proba_1 = res [1]/ tiradas
proba_2 = res [2]/ tiradas
proba_3 = res [3]/ tiradas
proba_4 = res [4]/ tiradas 
proba_5 = res [5]/ tiradas
    
proba_6 = res [6]/ tiradas # Calcula las probabilidades de cada número
print(F'de las {tiradas}tiradaz')
print(f'la probabilidad de que salga el numero 1 es {proba_1}')
print(f'la probabilidad de que salga el numero 2 es {proba_2}')

print(f'la probabilidad de que salga el numero 3 es {proba_3}')
print(f'la probabilidad de que salga el numero 4 es {proba_4}')

print(f'la probabilidad de que salga el numero 5 es {proba_5}')
print(f'la probabilidad de que salga el numero 6 es {proba_6}')