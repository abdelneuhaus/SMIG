def calculate_molecules_density(image_size, edge, pixel_size=0.16):
    side = (image_size-(edge/5))*pixel_size
    densities = [0.1, 0.25, 0.5, 0.75, 1]
    num_mol = []
    for i in densities:
        num_mol.append(int((side*i)*(side*i)))
    return num_mol