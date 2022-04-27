from generate_coordinates import generate_coordinates
from generate_intensity import generate_intensity
from generate_on_times import generate_on_times


def create_molecules_data(frames, nbr_molecules=20, size_image=2500, randomize=True, value=100000, ii_sd=0, off_length_min=1, off_length_max=3, number_blink_min=1, number_blink_max=3, own_blink=None, edge=0):
    data = dict()
    for i in range (nbr_molecules):
        if (own_blink == None):
            data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': generate_on_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max)}
        else:
            data[i] = {'coordinates': generate_coordinates(size_image, edge), 'intensity': generate_intensity(value, ii_sd), 'on_times': own_blink}
    return data
