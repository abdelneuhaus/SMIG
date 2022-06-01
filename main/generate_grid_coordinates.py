import random


def generate_grid_coordinates(size_image, edge):
    side = random.sample(range(0,6), 1)[0]
    if side == 0:   
        other = random.sample(range(edge, size_image-edge), 1)
        return[random.choice(other), random.choice(other)]
    elif side == 1:
        other = random.sample(range(edge*2, size_image-(2*edge)), 1)
        return [random.choice(other), random.choice(other)-2*edge]
    elif side == 2:
        other = random.sample(range(edge*2, size_image-(2*edge)), 1)
        return [random.choice(other), random.choice(other)+2*edge-1]
    elif side == 3:
        other = random.sample(range(edge*2, size_image-(2*edge)), 1)
        return [size_image-random.choice(other), random.choice(other)]
    elif side == 4:
        other = random.sample(range(edge*2, size_image-(2*edge)), 1)
        return [random.choice(other)+2*edge-1, size_image-random.choice(other)]
    elif side == 5:
        other = random.sample(range(edge*2, size_image-(2*edge)), 1)
        return [size_image-random.choice(other)-2*edge, random.choice(other)]
