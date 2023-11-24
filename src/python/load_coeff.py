# Imports
import numpy as np
import string


# Defining path to weights file
weightsPath = "../../data/3x3/"

def load_weight(argument: string, coefficient:dict, verbose:bool = False) -> dict:
    # argument: name of the file containing data
    # coefficient: dictionary of coefficients to be imported
    # verbose: argument to show prints
    
    # Debugging message
    if (verbose): print("Opening File:", weightsPath + argument)
    
    # Opening File
    inFile = open(weightsPath+argument, 'r')
    
    # Initializing empty string
    data = ""

    for line in inFile:
        data += line
    
    # Updating variable
    data_update = np.array(eval(data), dtype=float)
    # conv1_biases
    replace_bias = argument == "conv1_biases.txt" or argument == "conv2_biases.txt" or argument == "conv3_biases.txt"  or argument == "local3_biases.txt"
    if(replace_bias): new_argument = argument.replace("_biases.txt", "")
    else: new_argument = argument.replace("_weights.txt", "")

    if(verbose): print("After string modification", new_argument)
    # TODO: Get correct argument
    coefficient.update({new_argument : data_update})
    if(verbose): print("End of Function")
    return coefficient

def load_all():
    # Dictionaries Definition
    Weights = {
        "conv1": [],
        "conv2": [],
        "conv3": [],
        "local3": [],
    }

    Biases = {
        "conv1": [],
        "conv2": [],
        "conv3": [],
        "local3": [],  
    }

    # Loading for each file
    load_weight(argument="conv1_biases.txt", coefficient=Biases)
    load_weight(argument="conv1_weights.txt", coefficient=Weights)
    load_weight(argument="conv2_biases.txt", coefficient=Biases)
    load_weight(argument="conv2_weights.txt", coefficient=Weights)
    load_weight(argument="conv3_biases.txt", coefficient=Biases)
    load_weight(argument="conv3_weights.txt", coefficient=Weights)
    load_weight(argument="local3_biases.txt", coefficient=Biases)
    load_weight(argument="local3_weights.txt", coefficient=Weights)

    # Converting to correct sized np.arrays
    for name in Weights.keys():
        print(f"Weights.shape: {Weights[name].shape}")

        # Create correct sized numpy array
        if name in ["conv1", "conv2", "conv3"]:
            weight_transposed = np.transpose(Weights[name], (4, 3, 1, 2, 0)).squeeze()
        else:
            weight_transposed = np.transpose(Weights[name], (1, 2, 0)).squeeze()
        
        print(weight_transposed.shape)
        
        bias_transposed = np.array(Biases[name])
        
        Weights.update({name: weight_transposed})     
        Biases.update({name: bias_transposed})
    
    # Reshaping np.arrays for correct size
    return Weights, Biases

