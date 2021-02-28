import numpy as np


np.random.seed(42)


class Layer:
    """
    This is just a dummy class that is supposed to represent the general
    functionality of a neural network layer. Each layer can do two things:
     - forward pass - prediction
     - backward pass - training
    """

    def __init__(self):
        pass

    def forward(self, inp):
        # a dummy layer returns the input
        return inp

    def backward(self, inp, grad_outp):
        pass


class ReLU(Layer):
    def __init__(self):
        pass

    def forward(self, inp):
        return 0.0

    def backward(self, inp, grad_outp):
        pass


class Sigmoid(Layer):
    def __init__(self):
        pass

    def forward(self, inp):
        return 0.0

    def backward(self, inp, grad_outp):
        pass


class Dense(Layer):
    def __init__(self, inp_units, outp_units, learning_rate=0.1):
        pass

    def forward(self, inp):
        return 0.0

    def backward(self, inp, grad_outp):
        pass


class MLP():
    def __init__(self):
        pass

    def add_layer(self, neuron_count, inp_shape=None, activation='ReLU'):
        pass

    def forward(self, X):
        activations = []

        return activations

    def predict(self, X):
        return 0.0

    def fit(self, X, y):
        pass


if __name__ == '__main__':
    test = [[300, 400, 500], [2, 0, 1]]
    test = np.array(test)

    network = MLP()

    # TODO: add layers to the network

    print(network.predict(test))
