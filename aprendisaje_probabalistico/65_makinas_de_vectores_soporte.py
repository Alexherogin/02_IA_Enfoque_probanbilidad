
import numpy as np
import matplotlib.pyplot as plt
from sklearn.mixture import GaussianMixture

def generar_datos(n_samples, seed=0):
    np.random.seed(seed)
    X = np.concatenate((np.random.normal(0, 1, int(0.7 * n_samples)),
                        np.random.normal(5, 1, int(0.3 * n_samples))))[:, np.newaxis]
    return X

def ajustar_modelo_gmm(X, n_components=2):
    gmm = GaussianMixture(n_components=n_components)
    gmm.fit(X)
    return gmm

def visualizar_resultados(X, gmm):
    labels = gmm.predict(X)
    plt.scatter(X, np.zeros_like(X), c=labels, s=40, cmap='viridis')
    plt.show()

def main():
    n_samples = 300
    X = generar_datos(n_samples)
    gmm = ajustar_modelo_gmm(X)
    visualizar_resultados(X, gmm)
    print("Medias estimadas:", gmm.means_)
    print("Covarianzas estimadas:", gmm.covariances_)

if __name__ == "__main__":
    main()
