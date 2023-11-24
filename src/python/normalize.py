# Imports
import numpy as np

""" Normalize a 3D numpy array
    Args:
        image : np.array
            (c, x, y)
"""

def normalize(image):
    assert(image.ndim == 3)

    channels = image.shape[0]
    x_dimen = image.shape[1]
    y_dimen = image.shape[2]

    new_image = np.zeros((channels, x_dimen, y_dimen))

    # Normalizing for each channel
    for channel in range(channels):
        channel_array = image[channel] 
        
        mean = np.mean(channel_array)
        std = np.std(channel_array)

        # Normalizing image
        for i in range(x_dimen):
            for j in range(y_dimen):
                new_pixel = (channel_array[i, j] - mean)/max(std, (x_dimen*y_dimen)**(-1/2))

                if new_pixel < -1: new_pixel = -1
                elif new_pixel > 1: new_pixel = 1
 
                new_image[channel, i, j] = new_pixel 
        
    return new_image
