import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


class Perceptron:
    def __init__(self, input_no, learning_rate):
        # weights, learning rate
        self.learning_rate = learning_rate
        self.weights = np.zeros(input_no + 1)

    def get_sum(self, input_vector):
        # calculate input value of perceptron
        z = np.dot(input_vector, self.weights[1:]) + self.weights[0]
        return z

    def predict(self, input_vector):
        # returns activation 1 for class 1, -1 for class 2
        out = np.where(self.get_sum(input_vector) >= 0.0, 1, 0)
        return out

    def fit(self, X, y, epochs=10):
        # trains perceptron
        # w(t+1) = w(t) + x * learning rate * (y - predict)
        for _ in range(epochs):
            error = 0
            for x_i, target in zip(X, y):
                update = self.learning_rate * (target - self.predict(x_i))
                self.weights[1:] += x_i * update
                self.weights[0] += update  # x0 = 1
                error += int(update != 0)
            print("ERRORS:", error)


def plot_decision_regions(X, y, classifier, resolution=0.02):
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('blue', 'red', 'lightgreen', 'gray', 'cyan')
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
    plt.scatter(X[:2, 0], X[:2, 1], color='red', marker='o', label='0')
    plt.scatter(X[2:, 0], X[2:, 1], color='blue', marker='x', label='1')
    plt.xlabel('Input A')
    plt.ylabel('Input B')
    # plt.legend(loc='upper left')
    plt.show()


if __name__ == '__main__':
    # dFrame = pd.read_csv("iris.data", header=None)
    # y = dFrame.iloc[0:100, 4].values
    # y = np.where(y == 'Iris-setosa', -1, 1)
    # X = dFrame.iloc[0:100, [0, 2]].values
    # # plot_dataset(X)

    # my_perceptron = Perceptron(2, 0.1)
    # plot_decision_regions(X, y, my_perceptron)

    # my_perceptron.fit(X, y)
    # plot_decision_regions(X, y, my_perceptron)

    # print(my_perceptron.weights)

    X = np.array([[0, 0], [1, 1], [0, 1], [1, 0]])
    y = np.array([0, 0, 1, 1])
    # plot_dataset(X)

    my_perceptron = Perceptron(2, 0.1)
    # plot_decision_regions(X, y, my_perceptron)

    my_perceptron.fit(X, y)
    # plot_decision_regions(X, y, my_perceptron)

    # print(my_perceptron.weights)
