

def inferacion (probabilidad_lluvia, probabilidad_T_lluvia,probabilidad_trafico):

    probabilidad_01= (probabilidad_T_lluvia*probabilidad_lluvia /
                      (probabilidad_T_lluvia*probabilidad_lluvia)+(probabilidad_trafico*(1-probabilidad_lluvia)))
    
    probabilidad_T_lluvia= 1 - probabilidad_01

    print(f'pobabilidad de trafico en la lluvia es: {probabilidad_01:.2f} ')
    print(f'posibilidad de no ver trafico en la lluvia es: { probabilidad_trafico:.2f}')

probabilidad_lluvia=0.3
probabilidad_T_lluvia=0.8
probabilidad_trafico=0.2

inferacion(probabilidad_lluvia,probabilidad_T_lluvia,probabilidad_trafico)