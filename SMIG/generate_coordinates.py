import random


def generate_coordinates(size_image=5000):
    return [random.sample(range(0, size_image), 1)[0], random.sample(range(0, size_image), 1)[0]]