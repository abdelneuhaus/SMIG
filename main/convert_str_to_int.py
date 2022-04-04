from re import findall as findall
from re import split as spplit

def convert_str_to_int(string_to_convert):
    a = findall('\d+', string_to_convert)
    c = spplit(',| ,|, ', string_to_convert)
    value = [[int(i)] for i in a]
    r = [[i] for i in c if '-' in i]
    new = [r[i][0].split('-') for i in range(len(r))]
    z = list()
    for l in new:
        z.append([int(x) for x in l[0:2]])
    for j in z:
        min = j[0]
        max = j[1]
        nb = list(range(min+1, max))
        value.append(nb)
   
    return sorted([j for i in value for j in i])