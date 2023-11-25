# Imports
import numpy as np

""" Normalize a 3D numpy array
    Args:
        image : np.array
            (c, x, y)
"""
def normalize(image):
    assert(image.ndim == 3)

    N = image.shape[1]*image.shape[2]

    mean = np.mean(image)
    std = np.std(image)

    new_image = (image - mean)/max(std, N**(-1/2))
    
    return new_image
