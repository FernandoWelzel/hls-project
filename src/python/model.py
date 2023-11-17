import numpy as np

# User defined
import simpleFlow as sf
from load_coeff import *

# Creating network structure
model = sf.Sequential([
    # 1st Conv + Pool
    sf.Conv2D(kernel_size=(3, 3), input_shape=(24, 24, 3), output_shape=(24, 24, 64), name="conv1"),
    sf.MaxPooling2D(input_shape=(24, 24, 64), pool_size=(3, 3), strides=(2, 2), name="pool1"),
    
    # 2nd Conv + Pool
    sf.Conv2D(kernel_size=(3, 3), input_shape=(12, 12, 64), output_shape=(12, 12, 32), name="conv1"),
    sf.MaxPooling2D(input_shape=(12, 12, 32), pool_size=(3, 3), strides=(2, 2), name="conv1"),
    
    # 3rd Conv + Pool
    sf.Conv2D(kernel_size=(3, 3), input_shape=(6, 6, 32), output_shape=(6, 6, 20), name="conv1"),
    sf.MaxPooling2D(input_shape=(6, 6, 20), pool_size=(3, 3), strides=(2, 2), name="conv1"),

    # Reshaping for Dense
    sf.Reshape(name="reshape1"),

    # Final fully connected
    sf.Dense(input_size=180, output_size=10, name="local3")
])

# Storing weights and biases as numpy array
weight, bias = load_all()

# Loading weights from weights
# model.load_weights(weight, bias)