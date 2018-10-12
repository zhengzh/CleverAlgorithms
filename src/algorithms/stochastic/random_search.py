import numpy as np

def objective_function(x):
    return np.sum(x*x)

def random_vector(minmax):
    return minmax[:,0]+(minmax[:,1]-minmax[:,0])*np.random.rand(minmax.shape[0])
        
def search(search_space, max_iter):
    best, best_vector = None, None
    for i in range(max_iter):
        vector = random_vector(search_space)
        # print vector
        cost = objective_function(vector)
        if best == None or best > cost:
            best = cost
            best_vector = vector
        print " > iteration=%s, best=%s" % (i, best)
    return (best, best_vector)

if __name__ == '__main__':
    problem_size = 2
    search_space = np.ones((problem_size, 2))*np.array([-5, 5])
    
    # algorithm configuration
    max_iter = 1000
    # execute the algorithm
    best = search(search_space, max_iter)
    print "Done. Best Solution: c=%s, v=%s" % (best[0], best[1])