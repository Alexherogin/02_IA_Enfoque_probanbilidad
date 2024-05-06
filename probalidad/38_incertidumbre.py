
import random

def lanzar_dado():
    dado = random.randint(1,6)
    return dado

def sumular(tiradas):
    res ={1:0,2:0,3:0,4:0,5:0,6:0} #
    for _ in range(tiradas):
        resu = lanzar_dado()
        res[resu]+=1
        return res
    
tiradas = 1500
res = sumular(tiradas)
proba_1 = res [1]/ tiradas
proba_2 = res [2]/ tiradas
proba_3 = res [3]/ tiradas
proba_4 = res [4]/ tiradas 
proba_5 = res [5]/ tiradas
    
proba_6 = res [6]/ tiradas
print(F'de las {tiradas}tiradaz')
print(f'la probabilidad de que salga el numero 1 es {proba_1}')
print(f'la probabilidad de que salga el numero 2 es {proba_2}')

print(f'la probabilidad de que salga el numero 3 es {proba_3}')
print(f'la probabilidad de que salga el numero 4 es {proba_4}')

print(f'la probabilidad de que salga el numero 5 es {proba_5}')
print(f'la probabilidad de que salga el numero 6 es {proba_6}')