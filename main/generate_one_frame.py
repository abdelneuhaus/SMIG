import numpy as np

def generate_one_frame(molecules, image_size, frame=0):
    image = np.zeros((image_size, image_size))
    for j in range(len(molecules)):
        if molecules[j]['on_times'].__contains__(frame) == True:
            image[molecules[j]['coordinates'][0]][molecules[j]['coordinates'][1]] = molecules[j]['intensity']
    return np.array(image)