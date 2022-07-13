import random


def generate_on_times(frames, randomize=True, off_length_min=1, off_length_max=3, number_blink_min=1, number_blink_max=3, beads=False):
    number_blink = random.choice(list(range(number_blink_min, number_blink_max+1)))
    if number_blink_max == number_blink_min:
        number_blink = number_blink_min
    blink = []
    if beads == True and frames > 1:
        a=random.choice(list(range(0, int(frames*0.1))))
        b=random.choice(list(range(int(frames*0.9), frames)))
        return list(range(a,b))
    if randomize == True:
        if off_length_max != off_length_min or number_blink_max != number_blink_min:
            for i in range(number_blink):
                off_length = random.choice(list(range(off_length_min, off_length_max+1)))
                a = random.randint(0, frames-off_length+1)
                blink.append(random.sample(range(a, a+off_length), off_length))
            
        elif off_length_min == off_length_max and number_blink_max == number_blink_min:
            for i in range(number_blink):
                pattern = list(range(0, frames))
                if number_blink_max == 1:
                    for i in range(frames-off_length_min):
                        i = random.randrange(len(pattern)) # get random index
                        pattern[i], pattern[-1] = pattern[-1], pattern[i]    # swap with the last element
                        pattern.pop()
                        blink = pattern
                elif off_length_max == off_length_min and off_length_min == 1:
                    for i in range(frames-number_blink_max):
                        blink.append(random.randint(0,frames))
                else:           
                    a = random.choice(pattern)
                    b = list(range(a-1, a+off_length_min))
                    pattern = list(set(pattern) - set(b))
                    blink += b[1:]
            return blink
        
        elif off_length_max == off_length_min and number_blink_max != number_blink_min:
            for i in range(number_blink):
                blink.append(random.choice(list(range(0, frames+1))))
            
        elif off_length_max == off_length_min and off_length_min == frames:
            for i in range(number_blink):
                blink.append(list(range(0, frames)))
        return sorted(set([j for i in blink for j in i]))
    else:
        return list(range(frames-10, frames+1, 1))[::1]