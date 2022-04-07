import numpy as np


def add_noise(image_to_noised, bckg=498, sd=12):
    
    ## BASIC
    gaussian = np.random.normal(loc=bckg, scale=sd, size=image_to_noised.shape)
    poisson = np.random.poisson(image_to_noised, size=image_to_noised.shape)
    gaussian += np.array(poisson, dtype='uint16')
    gaussian[gaussian < 0] = bckg
    return np.array(gaussian, dtype='uint16')