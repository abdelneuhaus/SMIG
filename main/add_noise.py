import numpy as np
def add_noise(image_to_noised, bckg=498, sd=12):
    gaussian = np.random.normal(loc=bckg, scale=sd, size=image_to_noised.shape)
    gaussian += np.random.poisson(image_to_noised, size=image_to_noised.shape)
    gaussian[gaussian < 0] = bckg
    return np.array(gaussian, dtype='uint16')


# def add_noise(image_to_noised, bckg=498, sd=20):
#     baseline = 100
#     qe = 0.95
#     em_g = 300
#     readsigma = 74.4
#     e_adu = 12
    
#     n_ie = np.random.poisson(qe * image_to_noised + 0.002)
#     n_oe = np.random.gamma(n_ie, em_g)
#     n_oe = n_oe + np.random.normal(baseline, readsigma)
#     ADU_out = n_oe * e_adu + baseline
#     # saturation = 2**16
#     ADU_out[ADU_out < 0] = baseline
#     # camera = np.random.poisson(image_to_noised * qe + 0.002)
#     # out = np.random.gamma(camera, scale=em_g)
#     # out += np.random.normal(baseline, readsigma, size=camera.shape)
#     # camera *= e_adu
#     # camera += bckg
#     # camera[camera < 0] = baseline
#     return np.array(ADU_out, dtype='uint16')
