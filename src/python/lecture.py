# Imports


# Defining path to weights file
weightsPath = "../../../SEI_data/"

# Verbose Flag for debugging
verbose = True

# Function to be called - should return a dictionary
# def create_dict (weightsweightsPath):

# Creating Dictionaries
Weights = {
  "conv_1": [],
  "conv_2": [],
  "conv_3": [],
  "local_3": [],
}

Biases = {
  "conv_1": [],
  "conv_2": [],
  "conv_3": [],
  "local_3": [],  
}

# Status message
if (verbose): print("Opening File, Path: ", weightsPath)

# Opening files
inFile = open(weightsPath + "CNN_coeff_3x3.txt", 'r')
outFile = open(weightsPath + "outFile.txt", 'w')

# Initializing empty string
data = ""
# Initializing code word
code = "tensor_name"

 # Removing end of line 
for line in inFile:
  stripped_line = line.rstrip()
  data += stripped_line

# if (verbose): print("Modified: ", data[0:200])

# Writing File without end of lines
outFile.write(data)

# Looking for code word
occurrences = [data.find("tensor_name", 0)]

# Loop to look for the code word
for i in range (len(data)):
    if (data.find("tensor_name", i) == occurrences[-1]): continue
    else: occurrences.append(data.find("tensor_name", i))
    
# Removing meanless element
occurrences.pop()

if (verbose): print(occurrences)    

# Closing files
inFile.close()
outFile.close()