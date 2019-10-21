import numpy as np
from math import e


np.random.seed(42)


class Layer:
    def __init__(self):
        pass

    def forward_pass(self, inp):
        pass

    def backward_pass(self, inp, grad_outp):
        pass


class Sigmoid(Layer):
    def __init__(self):
        pass

    def forward(self, inp):
        pass

    def backward(self, inp, grad_outp):
        pass


class Dense(Layer):
    def __init__(self, inp_units, outp_units, learning_rate=0.1):
        pass

    def forward(self, inp):
        pass

    def backward(self, inp, grad_outp):
        pass


class MLP():
    def __init__(self):
        pass

    def add_layer(self, neuron_count, inp_shape=None):
        pass

    def forward(self, X):
        pass

    def predict(self, X):
        pass


test = [[3, 4, 5], [2, 0, 1]]
test = np.array(test)

network = MLP()
# TODO: add layers

network.predict(test)
