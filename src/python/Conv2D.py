import numpy as np

class Conv2D:
    ''' TensorFlow inspired 2D convolutional layer
    Description:
        Assuming padding='same'
    
    Args:
        kernel_size: tuple
            (kX, kY)
        input_shape: tuple
            (iX, iY, iC)
        output_shape: tuple
            (oX, oY, oC)
    
    Internal:
        weights: np.array(kX, kY, iC, oC)
        bias: np.array(kX, kY, iC, oC)
    '''
    def __init__(self, kernel_size : tuple, input_shape: tuple, output_shape : tuple):
        # Base parameters
        self.kernel_size = kernel_size
        self.output_shape = output_shape
        self.input_shape = input_shape

        # Internal matrices
        self.weights = np.ones([kernel_size[0], kernel_size[1], input_shape[2], output_shape[2]], dtype=float)
        self.bias = np.ones(output_shape[2], dtype=float)

    # Calculates the convolutional output
    def forward(self, feature_map):
        # If input is 2 dimentional, transforms into 3 dimensions
        if(feature_map.ndim == 2):
            feature_map = feature_map.reshape((1, feature_map.shape[0], feature_map.shape[1]))

        output = np.zeros(self.output_shape, dtype=float)

        # Output shapes
        rows = self.output_shape[0]
        columns = self.output_shape[1]
        channels = self.output_shape[2]

        kernelX = self.kernel_size[0]
        kernelY = self.kernel_size[1]

        # Compute each channel
        for c in range(channels):
            # Compute each row
            for x in range(rows):
                # Compute each column
                for y in range(columns):
                    sum = self.bias[c]
                    out_of_bounds = False

                    # Iterate though X of kernel
                    for m in range(kernelX):
                        x_index = x+m-1
                        x_out_of_bound = (x_index < 0) or (x_index >= self.input_shape[0])

                        # Iterate though Y of kernel
                        for n in range(kernelY):
                            y_index = y+n-1
                            y_out_of_bound = (y_index < 0) or (y_index >= self.input_shape[1])

                            out_of_bounds = x_out_of_bound or y_out_of_bound
                            
                            if(not out_of_bounds):
                                sum += feature_map[c, x_index, y_index]
                    
                    # Applies ReLU
                    if(sum < 0): sum = 0
            
                    output[x, y, c] = sum

        return output