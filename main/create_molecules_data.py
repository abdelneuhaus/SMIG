from generate_coordinates import generate_coordinates
from generate_intensity import generate_intensity
from generate_on_times import generate_on_times
from generate_grid_coordinates import generate_grid_coordinates
from generate_circle_coordinates import generate_circle_coordinates
import random 


def create_molecules_data(frames, nbr_molecules=20, size_image=2500, randomize=True, value=100000, ii_sd=0, off_length_min=1, off_length_max=3, number_blink_min=1, number_blink_max=3, own_blink=None, edge=0, grid=False, circle=False, num_circle=0):
    data = dict()
    if circle == True:
        radii=[300]*num_circle
        origin = []
        for i in range(num_circle):
            x=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
            y=random.sample(range(edge+(max(radii)), size_image-edge-(max(radii))), 1)[0]
            origin.append([x, y])
    for i in range (nbr_molecules):
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
    # for j in range(nbr_molecules, int(nbr_molecules*1.33)):
    #     if (grid == True) or (circle == True):
    #         data[j] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(int(value/3), int(value/15)), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=frames-1, off_length_max=frames-1, number_blink_min=0, number_blink_max=1, beads=True)}
    return data
