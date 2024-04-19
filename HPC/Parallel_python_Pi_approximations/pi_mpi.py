from mpi4py import MPI
import numpy as np

def pi_mpi4(N):
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    local_n = N // size + (rank < N % size)
    start = rank * local_n
    end = start + local_n

    x = np.linspace(start/N, end/N, local_n, endpoint=False)
    local_sum = np.sum(np.sqrt(1 - x**2)) * (1.0 / N)

    pi_approx = 4 * comm.reduce(local_sum, op=MPI.SUM, root=0)

    # Root process prints the result
    if rank == 0:
        print("Pi with MPI:", pi_approx)




