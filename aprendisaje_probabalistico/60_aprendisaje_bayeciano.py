
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
datosV =np.random.normal(loc=5,scale=2,size=1000)

obcerva= datosV[:50]

prioridad= np.random.normal(loc=0,scale=15)#distribucion proritaria
poste=(np.sum(obcerva)+1)/(len(obcerva)+1)#calcula distribucion por teorias bayes

plt.hist(datosV, bins=30, alpha=0.5, label="Distribucion verdadera")
plt.axvline(x=prioridad, color='r', linestyle='--', label="Media a priori")

plt.axvline(x=poste, color='g', linestyle='--', label="Media a posteriori")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.title("Aprendizaje Bayesiano")
plt.legend()
plt.show()

print(f"Media a priori: {prioridad:.2f}")
print(f"Media a posteriori: {poste:.2f}")
