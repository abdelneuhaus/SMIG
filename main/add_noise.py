import numpy as np


def add_noise(image_to_noised, baseline=498, e_per_adu=12, max_value=2000, em_gain=100, qe=1.0):
    
    ## BASIC
    gaussian = np.random.normal(loc=500, scale=100, size=image_to_noised.shape)
    poisson = np.random.poisson(image_to_noised, size=image_to_noised.shape)
    gaussian += np.array(poisson, dtype='uint16')

    return np.array(gaussian, dtype='uint16')