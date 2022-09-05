import numpy as np
import random
import math

def generate_one_frame(molecules, image_size, frame=0, shift=0, brownian_value=0, use_brownian=False, randomwalk_value=0, use_randomwalk=False, is_loaded=False):
    imshape = (image_size, image_size)
    x, y = np.indices(imshape)
    img = np.zeros(imshape)
    pipou = [True, False]
    d = brownian_value # µm²/s
    dT = 0.02 # s
    px_size = 0.16 # µm
    S = math.sqrt(2*d*dT)/px_size
    save = molecules

    for j in range(len(molecules)):    
        if (use_brownian == True) and (frame > 0) and (is_loaded == False):
            molecules[j]['coordinates'][0] += S*np.random.normal()
            molecules[j]['coordinates'][1] += S*np.random.normal()
            molecules[j]['model'].x_mean, molecules[j]['model'].y_mean = molecules[j]['coordinates'][0], molecules[j]['coordinates'][1]
        elif use_randomwalk == True and (frame > 0) and (is_loaded == False):
            xi = np.random.choice([-1, 1])*randomwalk_value
            yi = np.random.choice([-1, 1])*randomwalk_value
            molecules[j]['coordinates'][0] += (xi/math.sqrt(frame))
            molecules[j]['coordinates'][1] += (yi/math.sqrt(frame)) 
            molecules[j]['model'].x_mean, molecules[j]['model'].y_mean = molecules[j]['coordinates'][0], molecules[j]['coordinates'][1]
    
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

        if (is_loaded == True) and (use_brownian == True):
            molecules[j]['coordinates'][0] = save[j]['coordinates'][0]
            molecules[j]['coordinates'][1] = save[j]['coordinates'][1]
            molecules[j]['model'].x_mean, molecules[j]['model'].y_mean = save[j]['coordinates'][0], save[j]['coordinates'][1]
            
        if molecules[j]['on_times'].__contains__(frame) == True:
            try:
                img += molecules[j]['model'](x, y)
            except IndexError:
                pass
    return img, molecules