import numpy as np

class Sequential:
    ''' TensorFlow sequential model
    Description:
        Creates a chained neural network model from layers
    
    Args:
        layers: list
    '''
    def __init__(self, layers : list):
        # Base parameters
        self.layers = layers

    # Calculates the convolutional output
    def forward(self, feature_map):
        for layer in self.layers:
            output = np.zeros(self.output_shape, dtype=float)

        return output