import numpy as np

def pi_sequential(N):
    dx = 1.0 / N
    total = sum(np.sqrt(1 - (i * dx) ** 2) for i in range(N))
    return 4 * total * dx

N = 1000000
pi_approx_sequential = pi_sequential(N)
print(f"Sequential π approximation: {pi_approx_sequential}")




