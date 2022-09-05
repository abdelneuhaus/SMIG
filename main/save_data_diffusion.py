import json
import numpy as np

def save_data_diffusion(points, filename):
    filename = filename.replace('.tif','')
    json_object = json.dumps(points, indent = 4)
  
    with open(filename+"_diffusion.json", "w") as outfile:
        outfile.write(json_object)
    with open(str(filename)+'_diffusion.txt', 'w') as f:
        f.write('frame \t')
        f.write('id \t')
        f.write('coordinates (x,y) \n')
        for line in points.keys():
            f.write(str(points[line]['frame']))
            f.write('\t')
            f.write(str(points[line]['index']))
            f.write('\t')
            f.write(str(tuple(ti for ti in points[line]['coordinates'])[::-1]))
            f.write('\n')