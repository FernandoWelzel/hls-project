# Imports
import pickle

from normalize import *

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

    return label, sub_image
