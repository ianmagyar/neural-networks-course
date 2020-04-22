import numpy as np

from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler

import matplotlib.pyplot as plt


np.random.seed(1000)

X, _ = make_blobs(n_samples=500, centers=2, cluster_std=5.0, random_state=1000)

scaler = StandardScaler(with_std=False)
Xs = scaler.fit_transform(X)

Q = np.cov(Xs.T)
eigu, eigv = np.linalg.eig(Q)
print(eigu)
print(eigv)

plt.scatter(Xs[:, 0], Xs[:, 1])
plt.quiver(*[0, 0], *eigv[:, 0], color=['r'], scale=21)
plt.quiver(*[0, 0], *eigv[:, 1], color=['b'], scale=21)
plt.show()

W_oja = np.random.normal(scale=0.25, size=(2, 1))
prev_W_oja = np.ones((2, 1))

learning_rate = 0.0001
tolerance = 1e-8

while np.linalg.norm(W_oja - prev_W_oja) > tolerance:
    prev_W_oja = W_oja.copy()
    for x in Xs:
        y = np.dot(x, W_oja)

        dW_oja = learning_rate * y * (x - W_oja.T * y).reshape((2, 1))
        W_oja += dW_oja


oja_vec = W_oja.T[0]

plt.scatter(Xs[:, 0], Xs[:, 1])
plt.quiver(*[0, 0], *oja_vec, color=['r'], scale=21)
plt.show()
