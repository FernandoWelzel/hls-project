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
        temp = feature_map

        for layer in self.layers:
            temp = layer.forward(temp)

        return temp
    
    # Loads the weights in the correct layer
    def load_weights(self, weights):
        # Iterates to all classes and load weights by the name of the class
        for layer_weight in weights:
            for layer in self.layers:
                if layer.name == layer_weight.name:
                    layer.load_weights(layer_weight)