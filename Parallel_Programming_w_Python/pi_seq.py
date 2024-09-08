import numpy as np

def pi_sequential(N):
    dx = 1.0 / N
    total = sum(np.sqrt(1 - (i * dx) ** 2) for i in range(N))
    return 4 * total * dx




