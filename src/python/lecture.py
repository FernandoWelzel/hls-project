# Imports


# Defining path to weights file
weightsPath = "../../../SEI_data/"

# Verbose Flag for debugging
verbose = False

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

# Separating string in between occurrences
aux = data.split("tensor_name")

if (verbose):
    print("\nFirst tensor_name occurrence:")
    print(data[0:occurrences[1]])
    print("\nLast tensor_name occurrence:")
    print(data[occurrences[-1]:])

print("Number of elements in the splitted string: ", len(aux))
print("First element of splitted string: \n", aux[1])

counter = 0
for i in aux:
    print("In loop, element:", counter)
    if (counter == 0):
        begin = aux[1].find("conv1/biases[")
        print("Found begin at position", begin)
        end = aux[1].find("]")
        print("Found end at position", end)
        Biases.update({"conv_1": data[(15+len(code)):(end+16+len(code))]})
    counter += 1


print (Biases)

# Closing files
inFile.close()
outFile.close()