def save_data(points, x_image, filename):
    filename = filename.replace('.tif','')
    with open(str(filename)+'.txt', 'w') as f:
        f.write('id \t')
        f.write('approximative coordinates (x,y) \t')
        f.write('blinking frames \n')
        for line in points.keys():
            f.write(str(line))
            f.write('\t')
            f.write(str(tuple(ti/(x_image/500) for ti in points[line]['coordinates'])[::-1]))
            f.write('\t')
            f.write(str([x+1 for x in points[line]['on_times']]))
            f.write('\n')
