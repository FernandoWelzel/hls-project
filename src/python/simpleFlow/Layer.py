class Layer:
    ''' TensorFlow inspired general layer
    
    Args:
        name: str
    '''
    def __init__(self, name : str):       
        # Base parameters
        self.name = name
        
    # Virtual method for all layers    
    def forward():
        raise NotImplementedError()

