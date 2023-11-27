import argparse
import matplotlib.pyplot as plt

import simpleFlow as sf
from load_coeff import *
from read_dataset import *
from normalize import *

# Label conversion list
convesion_list = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

def inference():
    parser = argparse.ArgumentParser(description='Prints a single inference from a image in the CIFAR-10 dataset')

    parser.add_argument('-i', '--image', help='Number of the test image', required=False, default="0")
    parser.add_argument('-t', '--type', help='Network type - Either 3x3 or 5x5', required=False, default="3x3")
    parser.add_argument('-p', '--plot', action="store_true", help='Plot inference results')
    parser.add_argument('-c', '--channels', help='Number of channels using during plotting', required=False, default="3")
    
    args = parser.parse_args()

    # Defining architectural variables
    weightsPath = f"../../data/{args.type}/"

    # Kernel size
    if(args.type == "3x3"):
        kernel_size = (3, 3)
    elif(args.type == "5x5"):
        kernel_size = (5, 5)
    else:
        raise(RuntimeError("Undefined neural network type"))

    # Creating network structure
    model = sf.Sequential([
        # 1st Conv + Pool
        sf.Conv2D(kernel_size=kernel_size, input_shape=(3, 24, 24), output_shape=(64, 24, 24), name="conv1"),
        sf.MaxPooling2D(input_shape=(64, 24, 24), pool_size=(3, 3), strides=(2, 2), name="pool1"),
        
        # 2nd Conv + Pool
        sf.Conv2D(kernel_size=kernel_size, input_shape=(64, 12, 12), output_shape=(32, 12, 12), name="conv2"),
        sf.MaxPooling2D(input_shape=(32, 12, 12), pool_size=(3, 3), strides=(2, 2), name="pool2"),
        
        # 3rd Conv + Pool
        sf.Conv2D(kernel_size=kernel_size, input_shape=(32, 6, 6), output_shape=(20, 6, 6), name="conv3"),
        sf.MaxPooling2D(input_shape=(20, 6, 6), pool_size=(3, 3), strides=(2, 2), name="pool3"),

        # Reshaping for Dense
        sf.Reshape(name="reshape1"),

        # Final fully connected
        sf.Dense(input_size=180, output_size=10, name="local3")
    ])
    
    # Loading weights into the model
    weight, bias = load_all(weightsPath=weightsPath)

    # Loading weights from weights
    model.load_weights(weight, bias)

    # Importing image
    file_path = "../../data/cifar-10-python/cifar-10-batches-py/test_batch"
    
    label, image = read_cifar10_batch(file_path, int(args.image))
    
    normalized_image = normalize(image)
    normalized_image = np.transpose(normalized_image, (2, 0, 1))

    # Inference
    result = model.forward(normalized_image)

    predicted = convesion_list[np.argmax(result)]
    
    print(f"Label/Predicted: {convesion_list[label]}/{predicted}")

    # Plotting result using MatplotLib
    if(args.plot):
        # Declaring picture
        fig, axs = plt.subplots(int(args.channels), 8)

        # Setting titles
        titles = ["Initial", "Normalized", "Conv1", "Pool1", "Conv2", "Pool2", "Conv3", "Pool3"]

        for i, title in enumerate(titles):
            axs[0, i].title.set_text(title)

        # Showing image
        for i in range(int(args.channels)):
            axs[i, 0].imshow(image)

        # Printing showing normalized image
        normalized_image = np.transpose(normalized_image, (1, 2, 0))

        for i in range(int(args.channels)):
            axs[i, 1].imshow(image)

        # Printing all layers
        for i in range(int(args.channels)):
            for j in range(6):
                axs[i, j+2].imshow(model.outputs[j][i])
        
        plt.show()
          
if __name__ == "__main__":
    inference()