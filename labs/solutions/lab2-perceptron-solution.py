import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Perceptron:
    def __init__(self, input_no, learning_rate):
        self.learn_rate = learning_rate
        self.errors = []
        self.weights = np.zeros(input_no + 1)

    def get_sum(self, input_vector):
        return np.dot(input_vector, self.weights[1:]) + self.weights[0]

    def predict(self, input_vector):
        return np.where(self.get_sum(input_vector) >= 0.0, 1, -1)

    def fit(self, X, y, epochs=10):
        self.weights = np.zeros(1 + X.shape[1])
        for i in range(epochs):
            error = 0
            for xi, target in zip(X, y):
                update = self.learn_rate * (target - self.predict(xi))
                self.weights[1:] += update * xi
                self.weights[0] += update
                error += int(update != 0)
            self.errors.append(error)
        return self


def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])

    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution),
                           np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())

    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],
                    alpha=0.8, c=cmap(idx),
                    marker=markers[idx], label=cl)

    plt.xlabel('sepal length [cm]')
    plt.ylabel('petal length [cm]')
    plt.legend(loc='upper left')
    plt.show()


def plot_dataset(X):
    plt.scatter(X[:50, 0], X[:50, 1], color='red', marker='o', label='setosa')
    plt.scatter(X[50:100, 0], X[50:100, 1], color='blue', marker='x', label='versicolor')
    plt.xlabel('petal length')
    plt.ylabel('sepal length')
    plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    dFrame = pd.read_csv("iris.data", header=None)
    y = dFrame.iloc[0:100, 4].values
    y = np.where(y == 'Iris-setosa', -1, 1)
    X = dFrame.iloc[0:100, [0, 2]].values
    plot_dataset(X)

    my_perc = Perceptron(2, 0.1)
    plot_decision_regions(X, y, my_perc)

    my_perc.fit(X, y)
    plot_decision_regions(X, y, my_perc)
