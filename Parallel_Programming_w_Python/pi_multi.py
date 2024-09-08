from multiprocessing import Pool
import numpy as np

def f(i, dx):
    x = i * dx
    return np.sqrt(1 - x**2) * dx

def pi_multiprocessing(N, num_processes):
    dx = 1.0 / N
    with Pool(num_processes) as pool:
        result = pool.starmap(f, [(i, dx) for i in range(N)])

    return 4 * sum(result)








