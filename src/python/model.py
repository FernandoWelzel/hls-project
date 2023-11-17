import numpy as np

# User defined
import simpleFlow as sf
from load_coeff import *
from read_dataset import *

# Creating network structure
model = sf.Sequential([
    # 1st Conv + Pool
    sf.Conv2D(kernel_size=(3, 3), input_shape=(3, 24, 24), output_shape=(64, 24, 24), name="conv1"),
    sf.MaxPooling2D(input_shape=(64, 24, 24), pool_size=(3, 3), strides=(2, 2), name="pool1"),
    
    # 2nd Conv + Pool
    sf.Conv2D(kernel_size=(3, 3), input_shape=(64, 12, 12), output_shape=(32, 12, 12), name="conv2"),
    sf.MaxPooling2D(input_shape=(32, 12, 12), pool_size=(3, 3), strides=(2, 2), name="pool2"),
    
    # 3rd Conv + Pool
    sf.Conv2D(kernel_size=(3, 3), input_shape=(32, 6, 6), output_shape=(20, 6, 6), name="conv3"),
    sf.MaxPooling2D(input_shape=(20, 6, 6), pool_size=(3, 3), strides=(2, 2), name="pool3"),

    # Reshaping for Dense
    sf.Reshape(name="reshape1"),

    # Final fully connected
    sf.Dense(input_size=180, output_size=10, name="local3")
])

# Storing weights and biases as numpy array
weight, bias = load_all()

# Loading weights from weights
model.load_weights(weight, bias)

# Loading image
file_path = "../../../cifar-10-python/cifar-10-batches-py/data_batch_1"
label, image = read_cifar10_batch(file_path)

print(image.shape())

# Inference using images
# model.forward(image)