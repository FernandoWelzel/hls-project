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

        # Output from each layer
        self.outputs = []

    # Calculates the convolutional output
    def forward(self, feature_map):
        temp = feature_map

        for layer in self.layers:
            temp = layer.forward(temp)

            # Store output of each layer
            self.outputs.append(temp)

        return temp
    
    # Loads the weights in the correct layer
    def load_weights(self, weights, biases):
        # Asserting that both lists share the same layers
        assert weights.keys() == biases.keys()

        layers_to_fill = weights.keys()

        # Iterates to all classes and load weights by the name of the class
        for external_layer in layers_to_fill:
            # Searches layer names in the sequential model
            for internal_layer in self.layers:
                # Loads weights only in case of a match
                if external_layer == internal_layer.name:
                    internal_layer.load_weights(weights[external_layer], biases[external_layer])
