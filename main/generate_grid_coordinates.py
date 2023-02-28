import random

def generate_grid_coordinates(size_image, edge):
    side = random.choice(range(5))
    other_range = (edge*2, size_image-(2*edge))
    if side == 0:
        other = round(random.uniform(*other_range), 1)
        return [other, other]
    offset_options = [
        (0, 1),
        (0, -1),
        (1, 0),
        (-1, 0),
    ]
    offset = random.choice(offset_options)
    other = round(random.uniform(*other_range), 1)
    return [round(size_image/2 + offset[0] * edge + offset[1] * other, 1), round(size_image/2 + offset[1] * edge + offset[0] * other, 1)]

