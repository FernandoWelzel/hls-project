import argparse

import simpleFlow as sf
from load_coeff import *
from read_dataset import *
from normalize import *

# Label conversion list
convesion_list = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

def main():
    parser = argparse.ArgumentParser(description='Evaluates the performance of a pretrained CNN for the CIFAR-10 dataset.')

    parser.add_argument('-s', '--steps', help='Number of simulations steps', required=True)
    parser.add_argument('-t', '--type', help='Network type - Either 3x3 or 5x5', required=False, default="3x3")
    
    args = parser.parse_args()

    # Defining architectural variables
    weightsPath = f"../../data/{args.type}/"

    # Kernel size
    if(args.type == "3x3"):
        kernel_size = (3, 3)
    elif(args.type == "5x5"):
        kernel_size = (5, 5)
    else:
        raise(RuntimeError())

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

    correct = 0

    for s in range(int(args.steps)):
        label, image = read_cifar10_batch(file_path, s)

        image = normalize(image)

        image = np.transpose(image, (2, 0, 1))

        result = model.forward(image)

        print(f"Label/Predicted: {convesion_list[label]}/{convesion_list[np.argmax(result)]}")

        if(np.argmax(result) == label):
            correct += 1
        
    print(f"Accuracy: {correct}/{int(args.steps)} = {correct*100/int(args.steps):.2f}%")    

if __name__ == "__main__":
    main()