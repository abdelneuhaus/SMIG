from generate_coordinates import generate_coordinates
from generate_intensity import generate_intensity
from generate_on_times import generate_on_times
from generate_grid_coordinates import generate_grid_coordinates
from generate_circle_coordinates import generate_circle_coordinates
import random


def create_molecules_data(frames, nbr_molecules=20, size_image=2500, randomize=True, value=100000, 
                          ii_sd=0, off_length_min=1, off_length_max=3, number_blink_min=1, number_blink_max=3, 
                          own_blink=None, edge=0, grid=False, circle=False, num_circle=0, 
                          binary_file=None, coordinates_binary=None, use_density=False):
    data = dict()
    if use_density == True:
        image = dict()
        on = int(((off_length_max+off_length_min)/2)*((number_blink_min+number_blink_max)/2))
        nbr_per_frame = nbr_molecules
        total = int(nbr_per_frame*(frames/on))
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

        # find at which frame a molecule is blinking
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
            otp = coordinates_binary
            for i in range(total):
                z = random.choice(otp)
                otp.remove(z)
                if (own_blink == None):
                    data[i] = {'coordinates': list(z), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i]}
                else:
                    data[i] = {'coordinates': list(z), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink}
            return data
        
        # Circle checked
        if circle == True:
            radii=[300]*num_circle
            origin = []
            for i in range(num_circle):
                x=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
                y=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
                origin.append([x, y])
                
                
        # General protocol        
        for i in range(total):
            if (own_blink == None):
                if grid == True:
                    data[i] = {'coordinates': generate_grid_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i]}
                elif circle == True:
                    data[i] = {'coordinates': generate_circle_coordinates(size_image, edge, origin=origin, radius=radii), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i]}
                else:
                    data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i]}
            else:
                if grid == True:
                    data[i] = {'coordinates': generate_grid_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': dic[i]}
                else:
                    data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink}
        return data

    
    
    ########### NO DENSITY ###########
    # Creation of data with binary image
    if binary_file != None:
        otp = coordinates_binary
        for i in range(nbr_molecules):
            z = random.choice(otp)
            otp.remove(z)
            if (own_blink == None):
                data[i] = {'coordinates': list(z), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max)}
            else:
                data[i] = {'coordinates': list(z), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink}
        return data
    
    # Circle checked
    if circle == True:
        radii=[300]*num_circle
        origin = []
        for i in range(num_circle):
            x=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
            y=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
            origin.append([x, y])
            
            
    # General protocol        
    for i in range(nbr_molecules):
        if (own_blink == None):
            if grid == True:
                data[i] = {'coordinates': generate_grid_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max)}
            elif circle == True:
                data[i] = {'coordinates': generate_circle_coordinates(size_image, edge, origin=origin, radius=radii), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max)}
            else:
                data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max)}
        else:
            if grid == True:
                data[i] = {'coordinates': generate_grid_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max)}
            else:
                data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink}
    return data
