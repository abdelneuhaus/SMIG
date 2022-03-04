import random


def generate_intensity(value=9000):
    return random.sample(range(value, value+5), 1)[0]