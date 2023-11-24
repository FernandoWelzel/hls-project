import numpy as np
import matplotlib.pyplot as plt

# User defined
import simpleFlow as sf
from load_coeff import *
from read_dataset import *
from normalize import *

# Basic definitions
image_number = int(input("Enter image number: "))

convesion_list = [
    "airplane",										
    "automobile",										
    "bird",										
    "cat",										
    "deer",										
    "dog",										
    "frog",										
    "horse",										
    "ship",										
    "truck"
]

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
file_path = "../../data/cifar-10-python/cifar-10-batches-py/test_batch"
label, image = read_cifar10_batch(file_path, image_number)

number_of_channels = 8

# Declaring picture
fig, axs = plt.subplots(number_of_channels, 8)

axs[0, 0].title.set_text(f"Figure {image_number}")

# Showing image
for i in range(number_of_channels):
    axs[i, 0].imshow(image)

# Normalizing
image = normalize(image)

axs[0, 1].title.set_text(f"Figure {image_number} normalized")

# Printing showing normalized image
for i in range(number_of_channels):
    axs[i, 1].imshow(image)

for i in range(number_of_channels):
    if i < 3:
        axs[i, 1].imshow(image)

image = np.transpose(image, (2, 0, 1))

# for i in range(number_of_channels):
#     if i < 3:
#         print(i)
#         axs[i, 1].imshow((image + 1)/2)

# Inference using images
result = model.forward(image)

axs[0, 2].title.set_text(f"After conv1")
axs[0, 3].title.set_text(f"After pool1")
axs[0, 4].title.set_text(f"After conv2")
axs[0, 5].title.set_text(f"After pool2")
axs[0, 6].title.set_text(f"After conv3")
axs[0, 7].title.set_text(f"After pool3")

# Printing all layers
for i in range(number_of_channels):
    axs[i, 2].imshow(model.outputs[0][i])

    axs[i, 3].imshow(model.outputs[1][i])

    axs[i, 4].imshow(model.outputs[2][i])

    axs[i, 5].imshow(model.outputs[3][i])

    axs[i, 6].imshow(model.outputs[4][i])

    axs[i, 7].imshow(model.outputs[5][i])


fig.suptitle(f'label: {convesion_list[label]}\nresult: {convesion_list[np.argmax(result)]}', fontsize=30)

# print(model.layers[2].weights[0])
# print(model.outputs[1][:, 0:2, 0:2])

# Show all images
plt.show()