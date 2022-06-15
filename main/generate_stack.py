from generate_one_frame import generate_one_frame
from create_molecules_data import create_molecules_data
from downsampling import downsampling
from add_noise import add_noise
from save_data import save_data
from save_parameters import save_parameters
from palm import palm_blinking_pattern
from storm import storm_blinking_pattern

from scipy.ndimage import gaussian_filter
import tifffile
import numpy as np

def generate_stack(frames, nb_emitters, filename, randomize=True, intensity=60000, ii_sd=0, x_image=2500, y_image=2500, length_min=1, length_max=3, 
                                   blink_min=1, blink_max=3, background_value=750, sd_bckg_value=6, blinking_seq=None, edge=0, save=True, grid=False, 
                                   circle=False, num_circle=0, binary_file=None, coordinates_binary=None, use_density=False, is_loaded=False, 
                                   loaded_data=None, use_palm=None, use_storm=None, shift=False, shift_value=0):
    points = create_molecules_data(frames, 
                                   nbr_molecules=nb_emitters, 
                                   size_image=x_image, 
                                   randomize=randomize, 
                                   value=intensity,
                                   ii_sd=ii_sd, 
                                   off_length_min=length_min, off_length_max=length_max, 
                                   number_blink_min=blink_min, number_blink_max=blink_max, own_blink=blinking_seq, 
                                   edge=edge, grid=grid, circle=circle, num_circle=num_circle, binary_file=binary_file,
                                   coordinates_binary=coordinates_binary, use_density=use_density, shift=shift, shift_value=shift_value)
    if use_palm == True:
        palm = palm_blinking_pattern(frames, nb_emitters)
        for i in points.keys():
            points[i]['on_times'] = palm[i]
    elif use_storm == True:
        storm = storm_blinking_pattern(frames, nb_emitters)
        for i in points.keys():
            points[i]['on_times'] = storm[i]
    if is_loaded == True:
        points = loaded_data
        for i in points.keys():
            points[i]['intensity'] = intensity
    if save == False:
        data = generate_one_frame(points, y_image, frame=0)
        gaussian_image = gaussian_filter(data, sigma=5)
        down_image = downsampling(gaussian_image)
        out = add_noise(down_image, bckg=background_value, sd=sd_bckg_value)
        if binary_file != None:
            a = np.rot90(out, 3)
            a = np.flip(a)
            return np.flipud(a)
        return out
    with tifffile.TiffWriter(filename) as tif:
        for i in range(frames):
            data, points = generate_one_frame(points, y_image, frame=i, shift=shift)
            gaussian_image = gaussian_filter(data, sigma=5)
            down_image = downsampling(gaussian_image)
            out = add_noise(down_image, bckg=background_value, sd=sd_bckg_value)
            if binary_file != None:
                a = np.rot90(out, 3)
                b = np.flip(a)
                out = np.flipud(b)
            tif.write(out, photometric='minisblack')
            save_data(points, filename)
        save_parameters(filename, frames, nb_emitters, intensity, length_min, length_max, blink_min, blink_max, background_value, sd_bckg_value, blinking_seq, edge)
