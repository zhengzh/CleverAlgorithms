import numpy as np
from random import randrange

def onemax(x):
    return np.sum(x)

def random_bitstring(num_bits):
    return np.random.randint(2,size=num_bits)

def random_neighbor(bitstring):
    mutant = np.copy(bitstring)
    pos = randrange(0, len(bitstring))
    mutant[pos] = 1 - mutant[pos]
    return mutant

def search(num_bits, max_iter):
    current = {}
    current['vector'] = random_bitstring(num_bits)
    current['cost'] = onemax(current['vector'])

    for i in range(max_iter):
        candidate = {}
        candidate['vector'] = random_neighbor(current['vector'])
        candidate['cost'] = onemax(candidate['vector'])

        if current['cost'] <= candidate['cost']:
            current = candidate
        print " > iteration=%s, best=%s" % (i, current['cost'])

    return current

if __name__ == '__main__':
    num_bits = 64
    
    # algorithm configuration
    max_iter = 100
    # execute the algorithm
    best = search(num_bits, max_iter)
    print "Done. Best Solution: c=%s, v=%s" % (best['cost'], "".join([str(i) for i in best['vector']]))