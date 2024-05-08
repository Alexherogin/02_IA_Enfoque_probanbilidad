import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

np.random.seed(0)
n= 300
x =  np.concatenate((np.random.normal(0, 1, int(0.7 * n)),
                    np.random.normal(5, 1, int(0.3 * n))))[:, np.newaxis]
n_compo= 2
gmm=GaussianMixture(n_components=n_compo)
gmm.fit(x)

lables= gmm.predict(x)


print(f'estimacion: {gmm.means_}')
print(f'comparacion estimada {gmm.covariances_}')

plt.scatter(x,np.zeros_like(x),c=lables, s=40,cmap='viridis')
plt.show()