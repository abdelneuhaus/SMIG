import numpy as np


def add_noise(image_to_noised, baseline=750, e_per_adu=6, max_value=65535, em_gain=100, qe=1.0):
    readout_sigma = (em_gain*qe)/e_per_adu
    
    photons = np.random.RandomState(42).poisson(image_to_noised, size=image_to_noised.shape)
    electrons = np.random.RandomState(42).normal(scale=readout_sigma, size=image_to_noised.shape)
    electrons += photons
    electrons /= e_per_adu
    electrons += baseline
    electrons[electrons > max_value] = max_value
    
    return np.array(electrons, dtype='uint16')