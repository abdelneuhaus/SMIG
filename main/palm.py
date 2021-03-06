import random


def palm_blinking_pattern(frames, molecules):
    bleached = int(0.4*frames)
    begin_bleached = int(0.6*frames)
    nbr_on_times = list(range(2,5))
    nbr_blinks = list(range(int(frames*0.25), int(frames*0.3)))
    all_times = list(range(0, frames))
    filtered_on_times = list(range(0, frames-begin_bleached))
    end_times = list(range(frames-bleached, frames))
    semi_bleach = list(range(frames-begin_bleached, frames-bleached))

    popou = [False, False, False, False, True, True, True, True, True, True]
    pipou = [False, False, False, False, False, False, False, True, True, True]
    data = []
    for j in range(molecules):
        on = []
        blink = random.choice(nbr_blinks)
        for i in range(0, blink):
            on_length = random.choice(nbr_on_times)
            tmp = random.choice(all_times)
            papou = random.choice(pipou)
            pepou = random.choice(popou)
            if tmp in semi_bleach and pepou == True:
                tmp = random.choice(semi_bleach)
            elif tmp in end_times and papou == True:
                tmp = random.choice(end_times)
            else:
                tmp = random.choice(filtered_on_times)
            on.append(random.sample(range(tmp, tmp+on_length), on_length))
        data.append(list(set([j for i in on for j in i])))
    return data
