import numpy as np

class Reshape:
    ''' TensorFlow inspired conversion layer
    Description: Assumes output flatten layer
    '''  
    # Calculates the output
    def forward(self, feature_map):
        # Initializing result to zero
        output = feature_map.flatten()

        return output