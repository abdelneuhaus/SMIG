from calculate_molecules_density import calculate_molecules_density

def save_parameters(filename, frames, nb_emitters, intensity, length_min, length_max, blink_min, blink_max, background_value, sd_bckg_value, blinking_seq, edge):
    filename = filename.replace('.tif','')
    densities = calculate_molecules_density(image_size=500, edge=edge)
    with open(str(filename)+'_parameters.txt', 'w') as f:
        f.write('Number of frames: '+ str(frames))
        f.write('\n')
        f.write('Numbers of emitters: ' + str(nb_emitters))
        f.write('\n')
        f.write('Integrated Intensity: ' +str(intensity))
        f.write('\n')
        f.write('Background value: ' +str(background_value)+', sd: '+str(sd_bckg_value))
        f.write('\n')        
        f.write('ON duration: ['+ str(length_min)+', '+str(length_max)+']')
        f.write('\n')
        f.write('Number of blinks: ['+ str(blink_min)+', '+str(blink_max)+']')
        f.write('\n')
        f.write('Manual blinking sequence (if used): '+str(blinking_seq))
        f.write('\n')