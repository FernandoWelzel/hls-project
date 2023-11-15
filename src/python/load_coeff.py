# Imports
import numpy as np
import string


# Defining path to weights file
weightsPath = "../../../SEI_data/3x3/"

def load_weight(argument: string, coefficient:dict, verbose:bool) -> dict:
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
    argument.replace("_biases", "")
    # TODO: Get correct argument
    coefficient.update({argument : data_update})

    
