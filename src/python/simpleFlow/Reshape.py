import numpy as np

from .Layer import Layer

class Reshape(Layer):
    ''' TensorFlow inspired conversion layer
    Description: Assumes output flatten layer
    '''
    def __init__(self, name: str):
        super().__init__(name)
    
    # Calculates the output
    def forward(self, feature_map):
        # Initializing result to zero
        output = feature_map.flatten()

        return output