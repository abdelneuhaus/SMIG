import numpy as np
import random
from astropy.modeling.models import Gaussian2D
import matplotlib.pyplot as plt

def generate_one_frame(molecules, image_size, frame=0, shift=0):
    y, x = np.mgrid[0:image_size, 0:image_size]
    cpt = 0
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
                gm1 = Gaussian2D(molecules[j]['intensity']/6, molecules[j]['coordinates'][0], molecules[j]['coordinates'][1], 1, 1)
                if cpt == 0:
                    g1 = gm1(x, y)
                    cpt +=1
                else:
                    g1 += gm1(x,y)
            except IndexError:
                pass
    plt.show()
    return np.array(g1, dtype='uint16'), molecules