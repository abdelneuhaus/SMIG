import random


def generate_circle_coordinates(size_image=500, edge=0, origin=list(), radius=list()):
    j = random.sample(range(0, len(radius)), 1)[0]
    r = radius[j]
    x_circle = origin[j][0]
    y_circle = origin[j][1]
    for i in range(1):
        x=random.uniform(edge, size_image-edge)
        y=random.uniform(edge, size_image-edge)
        while (x-x_circle)*(x-x_circle) + (y-y_circle)*(y-y_circle) > r*r:
            x=random.uniform(edge, size_image-edge)
            y=random.uniform(edge, size_image-edge)
        return [round(x, 1), round(y, 1)]