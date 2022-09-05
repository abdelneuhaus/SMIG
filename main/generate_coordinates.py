import random


def generate_coordinates(size_image=500, edge=0):
    return [round(random.uniform(edge, size_image-edge), 3), round(random.uniform(edge, size_image-edge), 3)]
    