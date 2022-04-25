import xarray as xr
import numpy as np


def downsampling(big_image, downsampling_factor=5):
    b = big_image.shape[0]//downsampling_factor
    downsampled_image = big_image.reshape(-1, downsampling_factor, b, downsampling_factor).sum((-1, -3))
    return np.array(downsampled_image, dtype='uint16')
