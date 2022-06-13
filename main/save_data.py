import json

def save_data(points, filename):
    filename = filename.replace('.tif','')
    dictionary = dict()
    for i in range(len(points)):
        dictionary[i] = {
            'coordinates': points[i]['coordinates'],
            'intensity': points[i]['intensity'],
            'on_times': points[i]['on_times']
        }
    json_object = json.dumps(dictionary, indent = 4)
  
    with open(filename+".json", "w") as outfile:
        outfile.write(json_object)
