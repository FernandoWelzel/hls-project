import numpy as np

class Reshape:
    ''' TensorFlow inspired conversion layer
    '''
    def __init__(self):
        return
    
    # Calculates the output
    def forward(self, feature_map):
        # Initializing result to zero
        output = np.zeros([feature_map.size], dtype=float)

        return output