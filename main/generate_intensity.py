import numpy as np

def generate_intensity(value=9000, sd=0):
    return int(np.random.normal(loc=value, scale=sd))
