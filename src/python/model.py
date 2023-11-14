import numpy as np

# User defined
from Conv2D import Conv2D
from Dense import Dense

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

# Tests
print(conv_model.forward(test_matrix_conv))
print(dense_model.forward(test_matrix_dense))