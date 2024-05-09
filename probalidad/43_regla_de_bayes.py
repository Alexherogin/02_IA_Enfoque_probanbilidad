##

probavilidad_E = 0.01## Asigna la probabilidad de tener COVID (1%)
## Probavilidad de tener COVID con los resultados de la prueba

probavilidad_Positivo = 0.95 # Asigna la probabilidad de que la prueba dé un resultado positivo (95%)
probavilidad_Negativo = 0.05

def bayes (probavilidad_E,probavilidad_Positivo,probavilidad_Negativo):
    Negativo = 1- probavilidad_E # Calcula la probabilidad de no tener COVID (99%)
    Positivo = (probavilidad_E * probavilidad_Positivo)+(Negativo*probavilidad_Negativo)# Calcula la probabilidad de no tener COVID (99%)
    enfermo = (probavilidad_E * probavilidad_Positivo) / Positivo # Calcula la probabilidad de tener COVID dado un resultado positivo
    return enfermo
res = bayes(probavilidad_E,probavilidad_Positivo,probavilidad_Negativo) # Llama a la función bayes con los valores de las probabilidades
print(f'la probavilidad de tener COVID con los resultados de la prueva es de {res:.2%}')