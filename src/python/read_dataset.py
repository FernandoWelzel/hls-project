# Imports
import numpy as np

import os
import struct
import numpy as np

def read_cifar10_batch(file_path):
    with open(file_path, 'rb') as file:
        # Use struct to unpack the binary data
        # The format string depends on the CIFAR-10 file structure
        # Each record consists of a label followed by 3072 bytes representing a 32x32 image with three color channels
        # '<' denotes little-endian byte order, 'B' denotes an unsigned char (1 byte)
        fmt = '<' + 'B' * (1 + 32 * 32 * 3)
        # TODO: insert loop to read all the file
        data = file.read(struct.calcsize(fmt))

        # Unpack the binary data using struct
        unpacked_data = struct.unpack(fmt, data)

        # Extract label and image data
        label = unpacked_data[0]
        image_data = np.array(unpacked_data[1:], dtype=np.uint8)
        print("Total length of the read data -- ON FUNCTION: ", len(image_data))
        # Reshape the image data into a 3D array (32x32 image with three color channels)
        image_array = image_data.reshape((3, 32, 32)).transpose(1, 2, 0)

    return label, image_array

# Import any binary file of the CIFAR10 dataset
File = "../../../cifar-10-python/cifar-10-batches-py/data_batch_1"
label, image_array = read_cifar10_batch(File)
# print("Length of the read image: ", image_array.shape())
print("First PIXEL [R G B]: ", image_array[0, 0, :])
print("Last PIXEL  [R G B]: ", image_array[31, 31, :])
