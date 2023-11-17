class Layer:
    ''' TensorFlow inspired general layer
    
    Args:
        name: str
    '''
    def __init__(self, name : str):       
        # Base parameters
        self.name = name
        
    # Virtual method for all layers    
    def forward(self, feature_map):
        raise NotImplementedError()
    
    # Virtual method for loading weights and biases
    def load_weights(self, weights):
        raise NotImplementedError()

