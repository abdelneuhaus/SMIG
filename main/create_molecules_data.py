from generate_coordinates import generate_coordinates
from generate_intensity import generate_intensity
from generate_off_times import generate_off_times


def create_molecules_data(frames, nbr_molecules=20, size_image=2500, randomize=True, value=100000, off_length_min=1, off_length_max=3, number_blink_min=1, number_blink_max=3):
    data = dict()
    for i in range (nbr_molecules):
        data[i] = {'coordinates': generate_coordinates(size_image), 'intensity': generate_intensity(value), 'off_times': generate_off_times(frames, randomize=randomize, off_length_min=off_length_min, off_length_max=off_length_max, number_blink_min=number_blink_min, number_blink_max=number_blink_max)}
    return data
