import random


def generate_coordinates(size_image=500, edge=0):
    return [random.uniform(edge, size_image-edge), random.uniform(edge, size_image-edge)]
    