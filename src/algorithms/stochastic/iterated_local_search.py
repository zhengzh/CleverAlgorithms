import numpy as np
import math
import random

def euc_2d(a, b):
    return round(math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2))

def cost(permutation, cities):
    distance = 0
    for i, c1 in enumerate(permutation):
        c2 = permutation[0] if i==len(permutation)-1 else permutation[i+1]
        distance += euc_2d(cities[c1], cities[c2])
    return distance

def stochastic_two_opt(permutation):
    perm = list(permutation)
    c1 = random.randrange(0, len(perm)-1) 
    c2 = random.randrange(c1+1, len(perm))
    perm[c1:c2+1] = reversed(perm[c1:c2+1])
    return perm

def local_search(best, cities, max_no_improv):
    count = 0
    while count <= max_no_improv:
        candidate = {'vector': stochastic_two_opt(best['vector'])}
        candidate['cost'] = cost(candidate['vector'], cities)
        count = count+1 if candidate['cost'] > best['cost'] else 0
        if candidate['cost'] <= best['cost']: best = candidate
    return best

def double_bridge_move(perm):
    pos1 = 1 + random.randrange(len(perm)/4)
    pos2 = pos1 + random.randrange(len(perm)/4)
    pos3 = pos2 + random.randrange(len(perm)/4)
    p1 = perm[0:pos1] + perm[pos3:len(perm)]
    p2 = perm[pos2:pos3]+perm[pos1:pos2]
    return p1 + p2

def perturbation(cities, best):
    candidate = {}
    candidate['vector'] = double_bridge_move(best['vector'])
    candidate['cost'] = cost(candidate['vector'], cities)
    return candidate

def search(cities, max_iter, max_no_improv):
    best = {}
    best['vector'] = list(range(len(cities)))
    random.shuffle(best['vector'])
    best['cost'] = cost(best['vector'], cities)
    best = local_search(best, cities, max_no_improv)
    for i in range(max_iter):
        candidate = perturbation(cities, best)
        candidate = local_search(candidate, cities, max_no_improv)
        if candidate['cost'] <= best['cost']: best = candidate
        print " > iteration %s, best=%s" % (i, best['cost'])
    return best

if __name__ == '__main__':
    # problem configuration
    berlin52 = [[565,575],[25,185],[345,750],[945,685],[845,655],
        [880,660],[25,230],[525,1000],[580,1175],[650,1130],[1605,620],
        [1220,580],[1465,200],[1530,5],[845,680],[725,370],[145,665],
        [415,635],[510,875],[560,365],[300,465],[520,585],[480,415],
        [835,625],[975,580],[1215,245],[1320,315],[1250,400],[660,180],
        [410,250],[420,555],[575,665],[1150,1160],[700,580],[685,595],
        [685,610],[770,610],[795,645],[720,635],[760,650],[475,960],
        [95,260],[875,920],[700,500],[555,815],[830,485],[1170,65],
        [830,610],[605,625],[595,360],[1340,725],[1740,245]]
    # algorithm configuration
    max_iterations = 100
    max_no_improv = 50
    # execute the algorithm
    best = search(berlin52, max_iterations, max_no_improv)
    print "Done. Best Solution: c=%s, v=%s" % (best['cost'], best['vector'])
