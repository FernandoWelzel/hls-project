# Imports
import pickle

from normalize import *
from numpy import *

def unpickle(file):
    with open(file, 'rb') as fo:
        dict = pickle.load(fo, encoding='latin1')
    return dict

def read_cifar10_batch(file_path, index):
    data_batch_1 = unpickle(file_path)

    # Read data batch
    image = data_batch_1['data'][index]

    # Transforming image to right format
    image = image.reshape(3,32,32)
    image = image.transpose(1,2,0)

    # Cropping image
    sub_image = image[4:28, 4:28]

    label = data_batch_1['labels'][index]
    print("Label is:", label)
    return label, sub_image

def write_dataset(new_file_name, file_path, index):

    label, sub_image = read_cifar10_batch(file_path, index)
    
    normalized = normalize(sub_image)

    final_image = np.transpose(normalized, (2, 0, 1))

    final_label = np.array(label, dtype=int64)

    with open(new_file_name, "wb") as file:
        final_label.tofile(file)
        final_image.tofile(file)

    return 0