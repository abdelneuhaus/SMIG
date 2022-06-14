import random

def palm_blinking_pattern(frames, molecules):
    bleached = int(0.4*frames)
    nbr_on_times = list(range(1,4))
    nbr_blinks = list(range(6,8))
    all_on_times = list(range(0, frames-bleached))
    
    data = []
    for j in range(molecules):
        on = []
        blink = random.choice(nbr_blinks)
        for i in range(0, blink):
            on_length = random.choice(nbr_on_times)
            tmp = random.choice(all_on_times)
            on.append(random.sample(range(tmp, tmp+on_length), on_length))
        data.append(list(set([j for i in on for j in i])))
    return data
