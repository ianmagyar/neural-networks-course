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

W_sanger = np.random.normal(scale=0.1, size=(2, 2))
prev_W_sanger = np.ones((2, 2))

learning_rate = 0.1
nb_iterations = 2000
t = 0.0

for i in range(nb_iterations):
    prev_W_sanger = W_sanger.copy()
    dw = np.zeros((2, 2))
    t += 1.0

    for j in range(Xs.shape[0]):
        Ysj = np.dot(W_sanger, Xs[j]).reshape((2, 1))
        QYd = np.tril(np.dot(Ysj, Ysj.T))
        dw += np.dot(Ysj, Xs[j].reshape((1, 2))) - np.dot(QYd, W_sanger)

    W_sanger += (learning_rate / t) * dw
    W_sanger /= np.linalg.norm(W_sanger, axis=1).reshape((2, 1))

print(W_sanger)

vectors = W_sanger.T

plt.scatter(Xs[:, 0], Xs[:, 1])
plt.quiver(*[0, 0], *vectors[0], color=['r'], scale=21)
plt.quiver(*[0, 0], *vectors[1], color=['b'], scale=21)
plt.show()
