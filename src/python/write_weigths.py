import argparse

from load_coeff import *
from read_dataset import *

"""
This function saves the coefficients for our neural network model into a binary file.

Usage example:
    python write_weigths.py -t 3x3
"""
def main():
    parser = argparse.ArgumentParser(description='Writes CIFAR10 weigths into binary files that can be read in C.')

    parser.add_argument('-t', '--type', help='Network type - Either 3x3 or 5x5', required=False, default="3x3")
    parser.add_argument('-o', '--output_path', help='Path to the output file', required=True)
    
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
    
    # Loading weights into the model
    weight, bias = load_all(weightsPath=weightsPath)

    # Saving weights into the output path file
    write_weights(args.output_path, weight, bias)

if __name__ == "__main__":
    main()
