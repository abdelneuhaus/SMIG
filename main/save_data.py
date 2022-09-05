import json
import numpy as np

def save_data(points, filename):
    filename = filename.replace('.tif','')
    dictionary = dict()
    for i in range(len(points)):
        dictionary[i] = {
            'coordinates': points[i]['coordinates'],
            'intensity': int(points[i]['intensity']),
            'on_times': np.array(points[i]['on_times'], dtype='uint16').tolist(),
            'shift': np.array(points[i]['shift'], dtype='uint16').tolist()
        }

    json_object = json.dumps(dictionary, indent = 4)
  
    with open(filename+".json", "w") as outfile:
        outfile.write(json_object)

    with open(str(filename)+'.txt', 'w') as f:
        f.write('id \t')
        f.write('approximative coordinates (x,y) \t')
        f.write('blinking frames \n')
        for line in points.keys():
            f.write(str(line))
            f.write('\t')
            f.write(str(tuple(ti for ti in points[line]['coordinates'])[::-1]))
            f.write('\t')
            f.write(str([x+1 for x in points[line]['on_times']]))
            f.write('\n')