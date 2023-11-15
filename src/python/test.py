import numpy as np

# User defined
import simpleFlow as sf

# Convolutional layer
conv_model = sf.Conv2D(kernel_size=(3, 3), output_shape=(5, 5, 1), input_shape=(5, 5, 1))

test_matrix_conv = np.array((
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
))

# Dense layer
dense_model = sf.Dense(output_size=5, input_size=5)

test_matrix_dense = np.array((
    [1, 2, 3, 4, 5]
))

# MaxPooling layer
pool_model = sf.MaxPooling2D(input_shape=(5, 5, 1), strides=(1, 1), pool_size=(3, 3))

# Tests 1
print(conv_model.forward(test_matrix_conv))
print(dense_model.forward(test_matrix_dense))
print(pool_model.forward(test_matrix_conv))

# Changing weights
conv_model.weights = np.array((
    [0, 0, 0],
    [0, 1, 0],
    [0, 0, 0]
))

conv_model.bias = np.array((
    [0, 0, 0, 0, 0]
))

# Tests 2
print(conv_model.forward(test_matrix_conv))

# 3 channel convolutional model
conv_3C_model = sf.Conv2D(kernel_size=(3, 3), output_shape=(5, 5, 2), input_shape=(5, 5, 3))

test_matrix_conv_3C = np.array((
   [[1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]],
   [[1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]],
   [[1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]]
))

print(conv_3C_model.forward(test_matrix_conv_3C))
