# Imports
import numpy as np

# Defining path to weights file
weightsPath = "../../../SEI_data/3x3/"

# Verbose Flag for debugging
verbose = True

# Function to be called - should return a dictionary
# def create_dict (weightsweightsPath):

# Creating Dictionaries
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

# Status message
if (verbose): print("Opening File, Path: ", weightsPath)

argument = "conv1_weights.txt"
# Opening files
inFile = open(weightsPath + argument, 'r')
outFile = open(weightsPath + "outFile.txt", 'w')

# Initializing empty string
data = ""
# Initializing code word
# code = "tensor_name: "

# Removing end of line 
for line in inFile:
    # stripped_line = line.rstrip()
    data += line


# if (verbose): print("Modified: ", data[0:200])

data_update = np.array(eval(data), dtype = float)
outFile.write(data)
Weights.update({"conv1": data_update})

print(Weights)
# Writing File without end of lines
# print("\n\nData before manipulation: ", data)
# data = data.replace("conv1/biases", "")
# print("\n\nData after manipulation: ", data)
# values_str = data[1:(len(data)-1)].split()
# print("\n\nData after split mode", values_str)
# values = np.array(values_str, dtype=float)
# Biases.update({"conv_1": values})


# Looking for code word
# occurrences = [data.find(code, 0)]

# Loop to look for the code word
# for i in range (len(data)):
#     if (data.find(code, i) == occurrences[-1]): continue
#     else: occurrences.append(data.find(code, i))

# # Removing meanless element
# occurrences.pop()

# if (verbose): print(occurrences)    

# # Separating string in between occurrences
# aux = data.split("tensor_name")

# # if (verbose):
#     # print("\nFirst tensor_name occurrence:")
#     # print(data[0:occurrences[1]])
#     # print("\nLast tensor_name occurrence:")
#     # print(data[occurrences[-1]:])

# print("Number of elements in the splitted string: ", len(aux))

# offset = 0
# counter = 0
# for i in aux:
#     print("IN LOOP, iteration", counter)
#     if (counter == 0):
#         code_intern = "conv1/biases["
#         begin = aux[counter+1].find(code_intern)
#         end = aux[counter+1].find("]")
#         start = len(code_intern) + len(code) + offset + 1
#         finish = (end-2) + len(code) + offset
#         # values_str = (data[(len(code_intern)+len(code)+1):((end-2)+len(code))]).split()
#         values_str = (data[start:finish]).split()
#         values = np.array(values_str, dtype=float)
#         Biases.update({"conv_1": values})
#         if(verbose):
#             print("Found begin at position", begin)
#             print("Found end at position", end)
#             print("Cut string: ", values_str)
#             print("Transformed into an array", values)
#     else: 
#         if(counter == 1):
#             code_intern = "conv1/weights[[[["
#             print("Length of SECOND TERM:" , len(aux[counter+1]))
#             begin = aux[counter+1].find(code_intern)
#             print("Found begin at position", begin)
#             end = aux[counter+1].find("]")
#             start = len(code_intern) + 1
#             finish = end + len(code)
#             print(aux[counter+1][start:finish])
#             values_str = (aux[counter+1][start:finish]).split()
#             print("Cut string: ", values_str)
#             values = np.array(values_str, dtype=float)
#             print("Transformed into an array", values)
#             Weights.update({"conv_1": values})
#     counter +=1




# # print("Type of values cut from original string", type(values))
# print (Biases)
# print (Weights)

# # Closing files
inFile.close()
outFile.close()