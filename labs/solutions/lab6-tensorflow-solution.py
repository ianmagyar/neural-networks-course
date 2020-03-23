import tensorflow as tf

# create the nodes in the graph, and initialize values
a = tf.constant(13, name="a")
b = tf.constant(37, name="b")

# add together the two values
c = tf.add(a, b, name="c")
print(c)

# create the nodes in the graph, and initialize values
a = tf.constant(2.5, name="a")
b = tf.constant(6.5, name="b")

c = tf.add(a, b, name="c")
d = tf.subtract(b, 1, name="d")
e = tf.multiply(c, d, name="e")

print(e)


# simple perceptron with two input nodes
def my_perceptron(x):
    # define some arbitrary weights for the two input values
    W = tf.constant([[3, -2]], shape=(1, 2), dtype=tf.float32)

    # define the bias of the perceptron
    b = 1

    # compute weighted sum (hint: check out tf.matmul)
    z = tf.matmul(x, W, transpose_b=True) + b

    # apply the sigmoid activation function (hint: use tf.sigmoid)
    output = tf.sigmoid(z)

    return output


sample_input = tf.constant([[-1, 2]], shape=(1, 2), dtype=tf.float32)

# this should give you a tensor with value 0.002
result = my_perceptron(sample_input)
print(result)


# x: input values
# n_in: number of input nodes
# n_out: number of output nodes
def my_dense_layer(x, n_in, n_out):
    # define variable weights as a matrix and biases
    # initialize weights for one
    # initialize biases for zero
    W = tf.Variable(tf.ones((n_in, n_out)))
    b = tf.Variable(tf.zeros((1, n_out)))

    # compute weighted sum (hint: check out tf.matmul)
    z = tf.matmul(x, W) + b

    # apply the sigmoid activation function (hint: use tf.sigmoid)
    output = tf.sigmoid(z)

    return output


sample_input = tf.constant([[1, 2.]], shape=(1, 2))
print(my_dense_layer(sample_input, n_in=2, n_out=3))
