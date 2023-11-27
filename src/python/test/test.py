import numpy as np

# User defined
import simpleFlow as sf

# Convolutional layer
conv_model = sf.Conv2D(kernel_size=(3, 3), output_shape=(1, 5, 5), input_shape=(1, 5, 5), name="conv1")

test_matrix_conv = np.array((
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
))

# Dense layer
dense_model = sf.Dense(output_size=5, input_size=5, name="dense1")

test_matrix_dense = np.array((
    [1, 2, 3, 4, 5]
))

# MaxPooling layer
pool_model = sf.MaxPooling2D(input_shape=(1, 5, 5), strides=(1, 1), pool_size=(3, 3), name="pool1")

# Tests 1
# print(conv_model.forward(test_matrix_conv))
# print(dense_model.forward(test_matrix_dense))
# print(pool_model.forward(test_matrix_conv))

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
# print(conv_model.forward(test_matrix_conv))

# 3 channel convolutional model
conv_3C_model = sf.Conv2D(kernel_size=(3, 3), output_shape=(2, 5, 5), input_shape=(3, 5, 5), name="conv3c")

test_matrix_conv_3C = np.array((
   [[1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]],

   [[1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]],

   [[1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3, 4, 5, 6]],
))

# print(conv_3C_model.forward(test_matrix_conv_3C))

# Creating network structure
model = sf.Sequential([
    # 1st Conv + Pool
    sf.Conv2D(kernel_size=(3, 3), input_shape=(3, 6, 6), output_shape=(3, 6, 6), name="conv1"),
    sf.MaxPooling2D(input_shape=(3, 6, 6), pool_size=(3, 3), strides=(2, 2), name="pool1")
])

model.forward(test_matrix_conv_3C)

print(model.outputs[0])
print(model.outputs[1])