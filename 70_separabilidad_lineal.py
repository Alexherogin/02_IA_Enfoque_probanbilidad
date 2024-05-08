import numpy as np
from sklearn import svm

# Definir dos conjuntos de datos
X1 = np.array([[1, 2], [2, 3], [3, 1], [4, 3]])
y1 = np.array([0, 0, 1, 1])
X2 = np.array([[5, 2], [2, 1]])
y2 = np.array([1, 0])

# Concatenar los dos conjuntos de datos y sus etiquetas
X = np.concatenate((X1, X2), axis=0)
y = np.concatenate((y1, y2), axis=0)

# Crear un modelo SVM con un kernel lineal
model = svm.SVC(kernel='linear')

# Entrenar el modelo con los datos
model.fit(X, y)

# Verificar si los datos son linealmente separables
if len(model.support_vectors_) > 0:
    print("Los datos no son linealmente separables.")
else:
    print("Los datos son linealmente separables.")
