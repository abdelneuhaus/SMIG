from generate_coordinates import generate_coordinates
from generate_intensity import generate_intensity
from generate_on_times import generate_on_times
from generate_grid_coordinates import generate_grid_coordinates
from generate_circle_coordinates import generate_circle_coordinates

from astropy.modeling.models import Gaussian2D
import random


def create_molecules_data(frames, nbr_molecules=20, size_image=500, randomize=True, value=100000, 
                          ii_sd=0, off_length_min=1, off_length_max=3, number_blink_min=1, number_blink_max=3, 
                          own_blink=None, edge=0, grid=False, circle=False, num_circle=0, 
                          binary_file=None, coordinates_binary=None, use_density=False, shift=False, shift_value=0):
    data = dict()
    if use_density == True:
        image = dict()
        on = off_length_max*number_blink_max
        nbr_per_frame = nbr_molecules
        total = nbr_per_frame*int(frames/on)
        # total += int(total*0.1)
        total_loc = list()
        for i in range(total):
            total_loc.append([i]*on)
        total_loc = [j for i in total_loc for j in i]

        # create frame and which molecule is ON on it
        for i in range(frames):
            tmp = list()
            for j in range(nbr_per_frame):
                a = random.choice(total_loc)
                total_loc.remove(a)
                tmp.append(a)
            image[i] = tmp

        # find at which frame a molecule is ON
        dic = dict()
        for j in range(total):
            tmp = []
            for i in (image.keys()):
                if j in image[i]:
                    tmp.append(i)
                dic[j] = tmp

        ######## DENSITY ########
        # Creation of data with binary image
        if binary_file != None:
            cpt = 0
            otp = coordinates_binary
            for i in range(nbr_molecules):
                a = (int(random.uniform(edge, size_image-edge)), int(random.uniform(edge, size_image-edge)))
                if a in otp:
                    z = random.choice(otp)
                    otp.remove(z)
                    if (own_blink == None):
                        data[cpt] = {'coordinates': list(z), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[cpt], 'shift':0}
                    else:
                        data[cpt] = {'coordinates': list(z), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink, 'shift':0}
                    cpt += 1
            for i in data.keys():
                data[i]['model'] = Gaussian2D(data[i]['intensity'], data[i]['coordinates'][0], data[i]['coordinates'][1], 1, 1)
            return data
        
        # Circle checked
        if circle == True:
            radii=[50]*num_circle
            origin = []
            for i in range(num_circle):
                x=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
                y=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
                origin.append([x, y])
                
        # General protocol        
        for i in range(total):
            if (own_blink == None):
                if grid == True:
                    data[i] = {'coordinates': generate_grid_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i], 'shift':0}
                elif circle == True:
                    data[i] = {'coordinates': generate_circle_coordinates(size_image, edge, origin=origin, radius=radii), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i], 'shift':0}
                else:
                    data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i], 'shift':0}
            else:
                if grid == True:
                    data[i] = {'coordinates': generate_grid_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i], 'shift':0}
                else:
                    data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink, 'shift':0}
        for i in data.keys():
            data[i]['model'] = Gaussian2D(data[i]['intensity'], data[i]['coordinates'][0], data[i]['coordinates'][1], 1, 1)
        return data
    
    
    ########### NO DENSITY ###########
    # Creation of data with binary image
    if binary_file != None:
        cpt = 0
        otp = coordinates_binary
        for i in range(nbr_molecules):
            a = (int(random.uniform(edge, size_image-edge)), int(random.uniform(edge, size_image-edge)))
            if a in otp:
                z = random.choice(otp)
                otp.remove(z)
                if (own_blink == None):
                    data[i] = {'coordinates': list(z), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max), 'shift':0}
                else:
                    data[cpt] = {'coordinates': list(z), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink, 'shift':0}
                cpt += 1
        for i in data.keys():
            data[i]['model'] = Gaussian2D(data[i]['intensity'], data[i]['coordinates'][0], data[i]['coordinates'][1], 1, 1)
        return data

    
    # Circle checked
    if circle == True:
        radii=[50]*num_circle
        origin = []
        for i in range(num_circle):
            x=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
            y=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
            origin.append([x, y])
            
            
    # General protocol        
    for i in range(nbr_molecules):
        if (own_blink == None):
            if grid == True:
                data[i] = {'coordinates': generate_grid_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max), 'shift':0}
            elif circle == True:
                data[i] = {'coordinates': generate_circle_coordinates(size_image, edge, origin=origin, radius=radii), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max), 'shift':0}
            else:
                data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max), 'shift':0}
        else:
            if grid == True:
                data[i] = {'coordinates': generate_grid_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max), 'shift':0}
            else:
                data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink, 'shift':0}
    
    if shift == True:
        for i in data.keys():
            data[i]['shift'] = shift_value
    for i in data.keys():
        data[i]['model'] = Gaussian2D(data[i]['intensity'], data[i]['coordinates'][0], data[i]['coordinates'][1], 1, 1)
    return data
