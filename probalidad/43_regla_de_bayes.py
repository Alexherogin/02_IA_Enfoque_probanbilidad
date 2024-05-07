##

probavilidad_E = 0.01

probavilidad_Positivo = 0.95
probavilidad_Negativo = 0.05

def bayes (probavilidad_E,probavilidad_Positivo,probavilidad_Negativo):
    Negativo = 1- probavilidad_E
    Positivo = (probavilidad_E * probavilidad_Positivo)+(Negativo*probavilidad_Negativo)
    enfermo = (probavilidad_E * probavilidad_Positivo) / Positivo
    return enfermo
res = bayes(probavilidad_E,probavilidad_Positivo,probavilidad_Negativo)
print(f'la probavilidad de tener COVID con los resultados de la prueva es de {res:.2%}')