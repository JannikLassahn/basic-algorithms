def minmax_1(l):

    assert(len(l) > 0)

    maximum = l[0]
    minimum = l[0]

    for x in l:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    
    return (minimum, maximum)

def min_2(l):

    assert(len(l) > 0)

    minimum = l[0]

    for x in l:
        if x < minimum:
            minimum = x
    
    return minimum

def max_2(l):

    assert(len(l) > 0)

    maximum = l[0]

    for x in l:
        if x > maximum:
            maximum = x
    
    return maximum



def minmax_2(l):

    assert(len(l) > 0)

    if len(l) % 2 != 0:
        l.append(l[0])

    winner = []
    looser = []

    i = 0

    while i < len(l):
        if l[i] >= l[i + 1]:
            winner.append(l[i])
            looser.append(l[i + 1])
        else:
            winner.append(l[i + 1])
            looser.append(l[i])
        i = i + 2

    minimum = min_2(looser)
    maximum = max_2(winner)

    return (minimum, maximum)
