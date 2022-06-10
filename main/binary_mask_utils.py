import cv2
import numpy as np
import mahotas
import random



def get_polygons(filename):
    img = cv2.imread(filename)

    # make a mask
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(gray, 100, 255)

    # get contours # OpenCV 3.4, if you're using OpenCV 2 or 4, it returns (contours, _)
    contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # remove contours with very similar perimeters (we get back inner and outer contours)
    cutoff_percent = 0.05
    no_dupes = []
    for con in contours:
        perim = cv2.arcLength(con, closed = True);
        # check for duplicate
        dupe_flag = False
        for dupe in no_dupes:
            dupe_perim = cv2.arcLength(dupe, closed = True)
            if abs(dupe_perim - perim) < cutoff_percent * perim:
                dupe_flag = True
                break

        # add to list
        if not dupe_flag:
            no_dupes.append(con)

    return no_dupes


def get_all_coordinates(data):
    otp = []
    for i in data:
        tmp = []
        for j in i:
            for k in j:
                tmp.append(list(k))
        otp.append(list(tmp))
    return otp



def generate_coordinates_poly(poly):
    """Return polygon as grid of points inside polygon.

    Input : poly (list of lists)
    Output : output (list of lists)
    """
    xs, ys = zip(*poly)
    minx, maxx = min(xs), max(xs)
    miny, maxy = min(ys), max(ys)

    newPoly = [(int(x - minx), int(y - miny)) for (x, y) in poly]

    X = maxx - minx + 1
    Y = maxy - miny + 1

    grid = np.zeros((X, Y), dtype=np.int8)
    mahotas.polygon.fill_polygon(newPoly, grid)

    return [(x + minx, y + miny) for (x, y) in zip(*np.nonzero(grid))]




def pick_coordinates(data, n):
    coordinates = []
    for i in range(len(data)):
        for j in range(n):
            coordinates.append(random.choice(data[i]))
    return coordinates
