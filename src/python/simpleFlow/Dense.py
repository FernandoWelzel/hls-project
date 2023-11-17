import numpy as np

from .Layer import Layer

class Dense(Layer):
    ''' TensorFlow inspired densenly connected layer
    Description:
        Expects flatten input and assumes ReLU activation
    
    Args:
        input_size: int
        output_size: int
    
    Internal:
        weights: np.array(input_size, output_size)
        bias: np.array(output_size)
    '''
    def __init__(self, input_size: int, output_size : int, name : str):
        # Initializing base class attributes
        super().__init__(name)
        
        # Base parameters
        self.output_size = output_size
        self.input_size = input_size

        # Internal matrices
        self.weights = np.ones([input_size, output_size], dtype=float)
        self.bias = np.ones([output_size], dtype=float)

    # Calculates the output
    def forward(self, feature_map):
        # Initializing result to zero
        output = np.zeros([self.output_size], dtype=float)

        # Compute each channel
        for i in range(self.output_size):
            sum = self.bias[i]
            
            # Iterate though X of kernel
            for j in range(self.input_size):
                sum += self.weights[j, i]*feature_map[j]
            
            # Applies ReLU
            if(sum < 0): sum = 0
            
            output[i] = sum

        return output
    

    def load_weights(self, weights, biases):
        self.weights = weights
        self.bias = biases