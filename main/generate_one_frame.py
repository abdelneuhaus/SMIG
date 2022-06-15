import numpy as np
import random

def generate_one_frame(molecules, image_size, frame=0, shift=0):
    image = np.zeros((image_size, image_size))
    pipou = [True, False]
    for j in range(len(molecules)):
        if molecules[j]['on_times'].__contains__(frame) == True:
            a = random.choice(pipou)
            b = random.choice(pipou)
            if a == True and shift !=0:
                molecules[j]['coordinates'][0] += molecules[j]['shift']
            elif a == False and shift != 0:
                molecules[j]['coordinates'][0] -= molecules[j]['shift']
            if b == True and shift !=0:
                molecules[j]['coordinates'][1] += molecules[j]['shift']
            elif b == False and shift != 0:
                molecules[j]['coordinates'][1] -= molecules[j]['shift']
            molecules[j]['shift'] += shift
            try:
                image[molecules[j]['coordinates'][0]][molecules[j]['coordinates'][1]] = molecules[j]['intensity']
            except IndexError:
                pass
    return np.array(image), molecules