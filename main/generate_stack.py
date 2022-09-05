from json import load
from generate_one_frame import generate_one_frame
from create_molecules_data import create_molecules_data
from add_noise import add_noise
from save_data_diffusion import save_data_diffusion
from save_data import save_data
from save_parameters import save_parameters
from palm import palm_blinking_pattern
from storm import storm_blinking_pattern

import tifffile
import numpy as np
from astropy.modeling.models import Gaussian2D

def generate_stack(frames, nb_emitters, filename, randomize=True, intensity=60000, ii_sd=0, x_image=2500, y_image=2500, length_min=1, length_max=3, 
                                   blink_min=1, blink_max=3, background_value=750, sd_bckg_value=6, blinking_seq=None, edge=0, save=True, grid=False, 
                                   circle=False, num_circle=0, binary_file=None, coordinates_binary=None, use_density=False, is_loaded=False, 
                                   loaded_data=None, use_palm=None, use_storm=None, shift=False, shift_value=0, brownian_value=0, 
                                   use_brownian=False, randomwalk_value=0, use_randomwalk=False):
    if is_loaded == True:
        nb_emitters = len(loaded_data)
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
        for i in points.keys():
            points[i]['intensity'] = intensity
            points[i]['model'] = Gaussian2D(loaded_data[i]['intensity'], loaded_data[i]['coordinates'][0], loaded_data[i]['coordinates'][1], 1, 1)
            points[i]['coordinates'][0], points[i]['coordinates'][1] = loaded_data[i]['coordinates'][0], loaded_data[i]['coordinates'][1]
            points[i]['on_times'] = loaded_data[i]['on_times']
            points[i]['index'] = loaded_data[i]['index']
    if save == False:
        data, points = generate_one_frame(points, y_image, frame=0)
        out = add_noise(data, bckg=background_value, sd=sd_bckg_value)
        if binary_file != None:
            a = np.rot90(out, 3)
            a = np.flip(a)
            return np.flipud(a)
        return out
    toSave = {}
    with tifffile.TiffWriter(filename) as tif:
        k = 0
        for i in range(frames):
            data, points = generate_one_frame(points, y_image, frame=i, shift=shift_value, 
                                              brownian_value=brownian_value, use_brownian=use_brownian,
                                              randomwalk_value=randomwalk_value, use_randomwalk=use_randomwalk, is_loaded=is_loaded)
            
            for u in range(len(points)):
                if points[u]['on_times'].__contains__(i) == True:
                    if is_loaded == True:
                        toSave[k] = {
                                'frame': int(i),
                                'index': int(points[u]['index']),
                                'coordinates': list(points[u]['coordinates']),
                                'intensity': int(points[u]['intensity'])
                            }
                    else:    
                        toSave[k] = {
                                'frame': int(i),
                                'index': int(u),
                                'coordinates': list(points[u]['coordinates']),
                                'intensity': int(points[u]['intensity'])
                            }
                    k += 1
            out = add_noise(data, bckg=background_value, sd=sd_bckg_value)
            if binary_file != None:
                a = np.rot90(out, 3)
                b = np.flip(a)
                out = np.flipud(b)
            tif.write(np.array(out, dtype='uint16'), photometric='minisblack')
            if use_brownian == False:
                save_data(points, filename)
        if use_brownian == True:
            save_data_diffusion(toSave, filename)
        save_parameters(filename, frames, nb_emitters, intensity, length_min, length_max, blink_min, blink_max, background_value, sd_bckg_value, blinking_seq, edge)
