# Definir un diccionario con el número de pelotas de cada color
pelotas={'rojas':35,'verdes':5,'blancas':50}

# Definir una función para calcular la probabilidad condicional
def condicion(color,cond):
    if color in pelotas and cond in pelotas:
        probs =pelotas[color]/pelotas[cond]
    else:
        probs = 0
    return probs
# Definir la pelota y la condición a evaluar
color_deciado = 'verde'
cond ='blancas'
pcond = condicion(color_deciado,cond)

suma = sum(condicion(color,cond)for color in pelotas) # Calcular la suma de las probabilidades condicionales
normal = {color:condicion(color,cond) / suma for color in pelotas}# Calcular la probabilidad condicional normalizada

print(f'la condicion de una pelota {color_deciado} ya que {cond}: {pcond}') 
print('normal')
for color,prob in normal.items():
    print(f'{color}: {prob}')