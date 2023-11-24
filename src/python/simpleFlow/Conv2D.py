import numpy as np
import matplotlib.pyplot as plt

from .Layer import Layer

class Conv2D(Layer):
    ''' TensorFlow inspired 2D convolutional layer
    Description:
        Assuming padding='same'
    
    Args:
        kernel_size: tuple
            (kX, kY)
        input_shape: tuple
            (iC, iX, iY)
        output_shape: tuple
            (oC, oX, oY)
    
    Internal:
        weights: np.array(oC, iC, kX, kY)
        bias: np.array(oC)
    '''
    def __init__(self, kernel_size : tuple, input_shape: tuple, output_shape : tuple, name : str):
        # Checking kernel size is odd
        for size in kernel_size:
            assert size%2 == 1
        
        # Initializing base class attributes
        super().__init__(name)
        
        # Base parameters
        self.kernel_size = kernel_size
        self.output_shape = output_shape
        self.input_shape = input_shape

        # Internal matrices
        self.weights = np.ones((output_shape[0], input_shape[0], kernel_size[0], kernel_size[1]), dtype=float)
        self.bias = np.ones(output_shape[0], dtype=float)

    # Calculates the convolutional output
    def forward(self, feature_map):
        output = np.zeros(self.output_shape, dtype=float)

        # Output shapes
        rows = self.output_shape[1]
        columns = self.output_shape[2]
        channels_out = self.output_shape[0]

        channels_in = self.input_shape[0]

        kernelX = self.kernel_size[0]
        kernelY = self.kernel_size[1]

        # Compute each channel
        for c_out in range(channels_out):
            # Compute each row
            for x in range(rows):
                # Compute each column
                for y in range(columns):
                    # Initializing sum
                    sum = self.bias[c_out]
                    
                    # Iterating though input layers of the kernel
                    for c_in in range(channels_in):
                        # Iterate though X of kernel
                        for m in range(kernelX):
                            x_index = x+m-(kernelX-1)//2
                            x_out_of_bound = (x_index < 0) or (x_index >= self.input_shape[1])

                            # Iterate though Y of kernel
                            for n in range(kernelY):
                                y_index = y+n-(kernelY-1)//2
                                y_out_of_bound = (y_index < 0) or (y_index >= self.input_shape[2])

                                out_of_bounds = x_out_of_bound or y_out_of_bound
                                
                                if(not out_of_bounds):
                                    weight = self.weights[c_out, c_in, m, n]
                                    pixel = feature_map[c_in, x_index, y_index]

                                    sum += weight*pixel
                    
                    # Applies ReLU
                    if(sum < 0): sum = 0
            
                    output[c_out, x, y] = sum

        return output
    
    def load_weights(self, weights, biases):
        self.weights = weights
        self.bias = biases