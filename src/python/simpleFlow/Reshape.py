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
        output = np.zeros((feature_map.shape[0]*feature_map.shape[1]*feature_map.shape[2]))

        # Initializing result to zero
        for x in range(feature_map.shape[1]):
            for y in range(feature_map.shape[2]):
                for c in range(feature_map.shape[0]):
                    output[x*feature_map.shape[0]*feature_map.shape[1]+y*feature_map.shape[0]+c] = feature_map[c, x, y]

        return output