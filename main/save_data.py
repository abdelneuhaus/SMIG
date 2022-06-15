import json
import numpy as np

def save_data(points, filename):
    filename = filename.replace('.tif','')
    dictionary = dict()
    for i in range(len(points)):
        dictionary[i] = {
            'coordinates': np.array(points[i]['coordinates'], dtype='uint16').tolist(),
            'intensity': int(points[i]['intensity']),
            'on_times': np.array(points[i]['on_times'], dtype='uint16').tolist()
        }
    json_object = json.dumps(dictionary, indent = 4)
  
    with open(filename+".json", "w") as outfile:
        outfile.write(json_object)
