import random

def generate_on_times(frames, randomize=True, off_length_min=1, off_length_max=3, number_blink_min=1, number_blink_max=3, beads=False):
    number_blink = random.choice(range(number_blink_min, number_blink_max+1))
    if number_blink_max == number_blink_min:
        number_blink = number_blink_min
    blink = []
    if beads and frames > 1:
        a = random.choice(range(0, int(frames*0.1)))
        b = random.choice(range(int(frames*0.9), frames))
        return list(range(a,b))
    if randomize:
        for i in range(number_blink):
            off_length = random.choice(range(off_length_min, off_length_max+1))
            a = random.randint(0, frames-off_length)
            blink += list(range(a, a+off_length))
        return sorted(set(blink))
    else:
        return list(range(frames-10, frames+1))