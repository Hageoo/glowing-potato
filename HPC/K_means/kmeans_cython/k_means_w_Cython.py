import numpy as np
import cProfile
from k_means_cython import KMeansCython  # Import the compiled module

if __name__ == "__main__":
    np.random.seed(42)

    # Generate sample data manually
    X = np.random.randn(1000000, 2)  # Sample data generation with 100,000 data points
    clusters = 3

    # Create an instance of KMeansCython and run K-means clustering
    kmeans = KMeansCython(K=clusters, max_iters=150)

    # Profile the fit_predict method of KMeansCython
    profiler = cProfile.Profile()
    profiler.enable()
    labels = kmeans.fit_predict(X)
    profiler.disable()

    # Sort and print the profiling results
    profiler.print_stats(sort='cumulative')

    print(labels)
