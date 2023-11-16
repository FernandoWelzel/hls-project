import numpy as np

class MaxPooling2D:
    ''' TensorFlow inspired max pooling layer
    Description:
        Expects 2D input, assumes padding='same', and infers output_shape
    
    Args:
        input_shape: tuple
            (iC, ix, iy)
        strides: tuple
            (sx, sy)
        pool_size: tuple
            (px, py)
    '''
    def __init__(self, input_shape: tuple, strides : tuple, pool_size : tuple):
        # Base parameters
        self.input_shape = input_shape
        self.strides = strides
        self.pool_size = pool_size

        # Infered variables
        self.output_shape = input_shape

    # Calculates the convolutional output
    def forward(self, feature_map):
        # If input is 2 dimentional, transforms into 3 dimensions
        if(feature_map.ndim == 2):
            feature_map = feature_map.reshape((1, feature_map.shape[0], feature_map.shape[1]))

        output = np.zeros(self.output_shape, dtype=float)

        # Output shapes
        rows = self.output_shape[1]
        columns = self.output_shape[2]
        channels_out = self.output_shape[0]

        channels_in = self.input_shape[0]

        kernelX = self.pool_size[0]
        kernelY = self.pool_size[1]

        # Compute each channel
        for c_out in range(channels_out):
            # Compute each row
            for x in range(rows):
                # Compute each column
                for y in range(columns):
                    # Initializing sum
                    largest = 0
                    
                    # Iterating though input layers of the kernel
                    for c_in in range(channels_in):
                        # Iterate though X of kernel
                        for m in range(kernelX):
                            x_index = x+m-1
                            x_out_of_bound = (x_index < 0) or (x_index >= self.input_shape[1])

                            # Iterate though Y of kernel
                            for n in range(kernelY):
                                y_index = y+n-1
                                y_out_of_bound = (y_index < 0) or (y_index >= self.input_shape[2])

                                out_of_bounds = x_out_of_bound or y_out_of_bound
                                
                                if(not out_of_bounds):
                                    current = feature_map[c_in, x_index, y_index] 

                                    # Updates largest number if bigger
                                    if(current > largest):
                                        largest = current
                    
                    output[c_out, x, y] = largest
        
        return output