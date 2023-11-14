import numpy as np

from Conv2D import Conv2D

new_model = Conv2D(kernel_size=(3, 3), output_shape=(5, 5, 1), input_shape=(5, 5, 1))

test_matrix = np.array((
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
))

print(new_model.forward(test_matrix))
