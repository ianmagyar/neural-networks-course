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
        return np.maximum(0, inp)

    def backward(self, inp, grad_outp):
        pass


class Sigmoid(Layer):
    def __init__(self):
        pass

    def forward(self, inp):
        return 1 / (1 + np.exp(-inp))

    def backward(self, inp, grad_outp):
        pass


class Dense(Layer):
    def __init__(self, inp_units, outp_units, learning_rate=0.1):
        self.learning_rate = learning_rate
        self.weights = np.random.normal(
            loc=0.0, scale=np.sqrt(2 / (inp_units + outp_units)),
            size=(inp_units, outp_units))
        self.biases = np.zeros(outp_units)
        self.neuron_count = outp_units

    def get_neuron_count(self):
        return self.neuron_count

    def forward(self, inp):
        return np.dot(inp, self.weights) + self.biases

    def backward(self, inp, grad_outp):
        pass


class MLP():
    def __init__(self):
        self.layers = []

    def add_layer(self, neuron_count, inp_shape=None, activation='ReLU'):
        if len(self.layers) == 0 and inp_shape is None:
            raise ValueError("Must defined input shape for first layer")

        if inp_shape is None:
            inp_shape = self.layers[-2].get_neuron_count()

        self.layers.append(Dense(inp_shape, neuron_count))
        if activation == 'sigmoid':
            self.layers.append(Sigmoid())
        elif activation == 'ReLU':
            self.layers.append(ReLU())
        else:
            raise ValueError("Unknown activation function", activation)

    def forward(self, X):
        activations = []

        layer_input = X
        for l in self.layers:
            activations.append(l.forward(layer_input))
            layer_input = activations[-1]

        return activations

    def predict(self, X):
        logits = self.forward(X)[-1]
        return logits.argmax(axis=-1)

    def fit(self, X, y):
        pass


if __name__ == '__main__':
    test = [[300, 400, 500], [2, 0, 1]]
    test = np.array(test)

    network = MLP()

    network.add_layer(5, 3, activation='ReLU')
    network.add_layer(10, activation='ReLU')
    network.add_layer(2, activation='ReLU')

    print(network.predict(test))
