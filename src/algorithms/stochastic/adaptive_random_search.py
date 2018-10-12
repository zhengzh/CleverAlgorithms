import numpy as np

def objective_function(x):
    return np.sum(x*x)

def random_vector(minmax):
    return minmax[:,0]+(minmax[:,1]-minmax[:,0])*np.random.rand(minmax.shape[0])

def large_step_size(iter_step, step_size, s_factor, l_factor, iter_mult):
    if iter_step > 0 and iter_step % iter_mult == 0:
        return step_size * l_factor 
    return step_size * s_factor

def take_step(minmax, current, step_size):
    hi = np.minimum(minmax[:,1], current+step_size)
    lo = np.maximum(minmax[:,0], current-step_size)
    return random_vector(np.stack((hi, lo), axis=-1))

def take_steps(bounds, current, step_size, big_stepsize):
    step, big_step = {}, {}
    # print take_step(bounds, current, step_size)
    step['vector'] = take_step(bounds, current['vector'], step_size)
    step['cost'] = objective_function(step['vector'])
    big_step['vector'] = take_step(bounds, current['vector'], big_stepsize)
    big_step['cost'] = objective_function(big_step['vector'])
    return step, big_step

def search(bounds, init_factor, s_factor, l_factor, iter_mult, max_no_impr):
    step_size = (bounds[:,0]-bounds[:,1])*init_factor
    count, current = 0, {}
    current['vector'] = random_vector(bounds)
    current['cost'] = objective_function(current['vector'])

    for i in range(max_iter):
        big_stepsize = large_step_size(i, step_size, s_factor, l_factor, iter_mult)
        step, big_step = take_steps(bounds, current, step_size, big_stepsize)
        if step['cost'] <= current['cost'] or big_step['cost'] <= current['cost']:
            if step['cost'] > big_step['cost']:
                step_size, current = big_stepsize, big_step
            else:
                current = step
        else:
            count += 1
            if count >= max_no_impr:
                count, step_size = 0, (step_size/s_factor) 

        print " > iteration=%s, best=%s" % (i, current['cost'])
    return current

if __name__ == '__main__':
    problem_size = 2
    search_space = np.ones((problem_size, 2))*np.array([-5, 5])

    # algorithm configuration
    max_iter = 100
    init_factor = 0.05
    s_factor = 1.3
    l_factor = 3.0
    iter_mult = 10
    max_no_impr = 30
    # execute the algorithm
    best = search(search_space, init_factor, s_factor, l_factor, iter_mult, max_no_impr)
    print "Done. Best Solution: c=%s, v=%s" % (best['cost'], best['vector'])