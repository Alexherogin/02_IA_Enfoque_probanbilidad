
import numpy as np

# Definir la función de transición de estado (modelo dinámico)
def transicion_estado(x_t_1):
    # Ejemplo: Modelo de movimiento lineal
    return x_t_1 + np.random.normal(loc=0, scale=1)

# Definir la función de observación (modelo de medición)
def observacion(x_t):
    # Ejemplo: Observación con ruido gaussiano
    return x_t + np.random.normal(loc=0, scale=0.1)

# Inicializar el filtro de partículas
n_particulas = 100
particulas = np.random.normal(loc=0, scale=1, size=n_particulas)

# Simulación de filtrado de partículas
observaciones = [1.1, 2.0, 2.9, 4.0]
for z in observaciones:
    # Predicción: Mover las partículas según el modelo de transición
    particulas = transicion_estado(particulas)

    # Actualización: Ponderar las partículas según la observación
    pesos = np.exp(-0.5 * (z - particulas)**2 / 0.1**2)
    pesos /= np.sum(pesos)

    # Resampling: Muestrear nuevas partículas según los pesos
    particulas = np.random.choice(particulas, size=n_particulas, p=pesos)

    # Estimación: Calcular la media de las partículas como la estimación del estado
    estimacion_estado = np.mean(particulas)

    print(f"Estimación del estado: {estimacion_estado:.2f}")

print("Partículas finales:")
print(particulas)
