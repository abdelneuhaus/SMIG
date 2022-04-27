import random


def generate_coordinates(size_image=500, edge=0):
    return [random.sample(range(edge, size_image-edge), 1)[0], random.sample(range(edge, size_image-edge), 1)[0]]