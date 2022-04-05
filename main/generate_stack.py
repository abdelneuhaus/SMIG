from generate_one_frame import generate_one_frame
from create_molecules_data import create_molecules_data
from downsampling import downsampling
from add_noise import add_noise
from save_data import save_data

from scipy.ndimage import gaussian_filter
import tifffile


def generate_stack(frames, nb_emitters, filename, randomize=True, intensity=60000, x_image=2500, y_image=2500, length_min=1, length_max=3, 
                                   blink_min=1, blink_max=3, background_value=750, sd_bckg_value=6, blinking_seq=None):
    points = create_molecules_data(frames, 
                                   nbr_molecules=nb_emitters, 
                                   size_image=x_image, 
                                   randomize=randomize, 
                                   value=intensity, 
                                   off_length_min=length_min, off_length_max=length_max, 
                                   number_blink_min=blink_min, number_blink_max=blink_max, own_blink=blinking_seq)
    with tifffile.TiffWriter(filename) as tif:
        for i in range(frames):
            data = generate_one_frame(points, y_image, frame=i)
            gaussian_image = gaussian_filter(data, sigma=5)
            down_image = downsampling(gaussian_image)
            out = add_noise(down_image, bckg=background_value, sd=sd_bckg_value)
            tif.write(out, photometric='minisblack')
            save_data(points, x_image, filename)
