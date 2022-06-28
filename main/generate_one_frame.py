import numpy as np
import random


def generate_one_frame(molecules, image_size, frame=0, shift=0):
    imshape = (image_size, image_size)
    x, y = np.indices(imshape)
    img = np.zeros(imshape)
    pipou = [True, False]
    for j in range(len(molecules)):
        if molecules[j]['on_times'].__contains__(frame) == True:
            a = random.choice(pipou)
            b = random.choice(pipou)
            if a == True and shift !=0:
                molecules[j]['coordinates'][0] += molecules[j]['shift']
                molecules[j]['model'].x_mean += molecules[j]['shift']
            elif a == False and shift != 0:
                molecules[j]['coordinates'][0] -= molecules[j]['shift']
                molecules[j]['model'].x_mean -= molecules[j]['shift']
            if b == True and shift !=0:
                molecules[j]['coordinates'][1] += molecules[j]['shift']
                molecules[j]['model'].y_mean += molecules[j]['shift']
            elif b == False and shift != 0:
                molecules[j]['coordinates'][1] -= molecules[j]['shift']
                molecules[j]['model'].y_mean -= molecules[j]['shift']
            try:
                img += molecules[j]['model'](x, y)
            except IndexError:
                pass
    return img, molecules