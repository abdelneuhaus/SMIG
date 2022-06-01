import random


def generate_circle_coordinates(size_image=500, edge=0, origin=list(), radius=list()):
    j = random.sample(range(0, len(radius)), 1)[0]
    r = radius[j]
    x_circle = origin[j][0]
    y_circle = origin[j][1]
    # (x - center_x)² + (y - center_y)² < radius²
    for i in range(1):
        x=random.sample(range(edge, size_image-edge), 1)[0]
        y=random.sample(range(edge, size_image-edge), 1)[0]
        while (x-x_circle)*(x-x_circle) + (y-y_circle)*(y-y_circle) > r*r:
            x=random.sample(range(edge, size_image-edge), 1)[0]
            y=random.sample(range(edge, size_image-edge), 1)[0]
        return [x, y]