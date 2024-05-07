
pelotas={'rojas':35,'verdes':5,'blancas':50}

def condicion(color,cond):
    if color in pelotas and cond in pelotas:
        probs =pelotas[color]/pelotas[cond]
    else:
        probs = 0
    return probs
color_deciado = 'verde'
cond ='blancas'
pcond = condicion(color_deciado,cond)

suma = sum(condicion(color,cond)for color in pelotas)
normal = {color:condicion(color,cond) / suma for color in pelotas}

print(f'la condicion de una pelota {color_deciado} ya que {cond}: {pcond}')
print('normal')
for color,prob in normal.items():
    print(f'{color}: {prob}')