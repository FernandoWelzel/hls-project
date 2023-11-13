import numpy as np

# Convolutional neural network layer - Inspired by TensorFlow
class Conv2D:
    def __init__(self, output_shape, input_shape, stride):
        # Base parameters
        self.output_shape = output_shape
        self.input_shape = input_shape
        self.stride = stride

        # Internal matrices
        self.weights = np.zeros([output_shape], dtype=float)
        self.bias = np.zeros([output_shape], dtype=float)

    # Calculates the convolutional output
    def forward():
        return 0