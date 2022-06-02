import random


def generate_on_times(frames, randomize=True, off_length_min=1, off_length_max=3, number_blink_min=1, number_blink_max=3, beads=False):
    number_blink = random.choice(list(range(number_blink_min, number_blink_max+1)))
    blink = []
    if beads == True:
        return list(range(0,frames))
    if randomize == True:
        for i in range (number_blink):
            off_length = random.choice(list(range(off_length_min, off_length_max+1)))
            a = random.randint(0, frames-off_length+1)
            blink.append(random.sample(range(a, a+off_length), off_length))
        return sorted(set([j for i in blink for j in i]))
    else:
        return list(range(frames-10, frames+1, 1))[::1]