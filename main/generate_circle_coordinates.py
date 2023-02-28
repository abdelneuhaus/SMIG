import random
import numpy as np

def generate_circle_coordinates(size_image=500, edge=0, origin=list(), radius=list()):
    j = random.randint(0, len(radius)-1)
    r = radius[j]
    origin = np.array(origin[j])
    while True:
        random_point = np.random.uniform(edge, size_image-edge, size=2)
        if np.linalg.norm(random_point - origin) <= r:
            return [round(p, 1) for p in random_point]
