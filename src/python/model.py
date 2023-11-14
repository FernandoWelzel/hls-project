import numpy as np

# User defined
from Conv2D import Conv2D
from Dense import Dense
from MaxPooling2D import MaxPooling2D

# Convolutional layer
conv_model = Conv2D(kernel_size=(3, 3), output_shape=(5, 5, 1), input_shape=(5, 5, 1))

test_matrix_conv = np.array((
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
))

# Dense layer
dense_model = Dense(output_size=5, input_size=5)

test_matrix_dense = np.array((
    [1, 2, 3, 4, 5]
))

# MaxPooling layer
pool_model = MaxPooling2D(input_shape=(5, 5, 1), strides=(1, 1), pool_size=(3, 3))

# Tests
print(conv_model.forward(test_matrix_conv))
print(dense_model.forward(test_matrix_dense))
print(pool_model.forward(test_matrix_conv))