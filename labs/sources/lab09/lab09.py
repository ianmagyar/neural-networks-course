from keras.layers import Input, Dense
from keras.models import Model
from keras.datasets import mnist
import numpy as np
import matplotlib.pyplot as plt


def plot_results(x_test, encoded_imgs, decoded_imgs, n=10):
    plt.figure(figsize=(40, 4))
    for i in range(n):
        # display original
        ax = plt.subplot(3, n, i + 1)
        plt.imshow(x_test[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display encoded
        ax = plt.subplot(3, n, i + 1 + n)
        plt.imshow(encoded_imgs[i].reshape(8, 4))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)

        # display reconstruction
        ax = plt.subplot(3, n, i + 1 + n * 2)
        plt.imshow(decoded_imgs[i].reshape(28, 28))
        plt.gray()
        ax.get_xaxis().set_visible(False)
        ax.get_yaxis().set_visible(False)
    plt.show()


(mnist_train, _), (mnist_test, _) = mnist.load_data()

x_train =  # TODO: normalize data to interval 0-1
x_test =  # TODO: normalize data to interval 0-1
x_train =  # TODO: reshape to flattened input: (len, 28, 28) -> (len, 784)
x_test =  # TODO: reshape to flattened input: (len, 28, 28) -> (len, 784)

input_img =  # TODO: define input layer with size

encoded =  # TODO: define hidden layer - 32 neurons, relu; connect to input
decoded =  # TODO: define output layer, same as input, use sigmoid act

autoencoder =  # TODO: define entire model
encoder =  # TODO: define encoder part

encoded_input =  # TODO: define new input layer for encoded code
decoder_layer =  # TODO: load last autoencoder layer, connect with previous
decoder =  # TODO: define decoder model

autoencoder.compile(  # TODO: add parameters
)
autoencoder.fit(  # TODO: add parameters
)

encoded_imgs = encoder.predict(x_test)
decoded_imgs = autoencoder.predict(x_test)

plot_results(x_test, encoded_imgs, decoded_imgs)
