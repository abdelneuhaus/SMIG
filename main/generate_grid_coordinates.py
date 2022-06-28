import random


def generate_grid_coordinates(size_image, edge):
    side = random.sample(range(0,5), 1)[0]
    if side == 0:   
        other = random.uniform(edge, size_image-edge)
        return[round(other, 1), round(other, 1)]
    elif side == 1:
        other = random.uniform(edge*2, size_image-(2*edge))
        return [round(other, 1), round(other-edge, 1)]
    elif side == 2:
        other = random.uniform(edge*2, size_image-(2*edge))
        return [round(other, 1), round(other+edge, 1)]
    elif side == 3:
        other = random.uniform(edge*2, size_image-(2*edge))
        return [round(size_image-other, 1), round(other, 1)]
    elif side == 4:
        other = random.uniform(edge*2, size_image-(2*edge))
        return [round(other+edge, 1), round(size_image-other, 1)]
