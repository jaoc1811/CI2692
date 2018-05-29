import random

def read_file(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    col1 = []
    col2 = []
    for line in lines:
        c1, c2 = line.strip().split("\t")
        col1.append(c1)
        col2.append(c2)
    return (col1, col2)

def Random(a, b):
    return lrand(a, b + 1)

def lrand(a, b):
    if 1 + a == b:
        return a
    else:
        return random.randrange(a, b)

def sample_with_replacement(n, m):
    indices = xrange(n)
    return [ random.choice(indices) for i in xrange(m) ]

def sample_with_replacement_from_lists(lst1, lst2, m):
    indices = xrange(len(lst1))
    samples = xrange(m)
    chosen1 = []
    chosen2 = []
    for i in samples:
        witness = random.choice(indices)
        chosen1.append(lst1[witness])
        chosen2.append(lst2[witness])
    return (chosen1,chosen2)

def sample_without_replacement(n, m):
    return random.sample(range(n), m)

def sample_without_replacement_from_list(lst, m):
    return random.sample(lst, m)

def random_shuffle(lst):
    return random.sample(lst, k = len(lst))

