import xarray as xr
import numpy as np

def downsampling(big_image, downsampling_factor=5):
    downsampled_image = xr.DataArray(big_image, dims=['x', 'y']).coarsen(x=downsampling_factor, y=downsampling_factor).sum()
    return np.array(downsampled_image.values, dtype='uint16')
