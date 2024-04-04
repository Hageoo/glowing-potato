import numpy as np
import cProfile

class KMeans:
    def __init__(self, K=5, max_iters=100):
        self.K = K
        self.max_iters = max_iters
        self.centroids = None

    def predict(self, X):
        self.X = X
        self.n_samples, self.n_features = X.shape

        # Initialize centroids randomly from data points
        self.centroids = self.X[np.random.choice(self.n_samples, self.K, replace=False)]

        for _ in range(self.max_iters):
            # Assign samples to closest centroids
            labels = self._assign_clusters(self.X)

            # Update centroids
            new_centroids = np.array([self.X[labels == k].mean(axis=0) for k in range(self.K)])

            # Check convergence
            if np.allclose(self.centroids, new_centroids):
                break

            self.centroids = new_centroids

        return self._get_cluster_labels(labels)

    def _assign_clusters(self, X):
        # Calculate distances to centroids
        distances = np.sqrt(np.sum((X[:, np.newaxis, :] - self.centroids) ** 2, axis=2))

        # Assign samples to closest centroids
        labels = np.argmin(distances, axis=1)
        return labels

    def _get_cluster_labels(self, labels):
        return labels

if __name__ == "__main__":
    np.random.seed(42)

    # Generate a larger sample data manually
    X = np.random.randn(1000000, 2)  # Sample data generation with a million data points
    clusters = 3

    # Create an instance of kmeans
    k = KMeans(K=clusters, max_iters=150)

    # Profiling the predict method of optimized KMeans
    cProfile.run('k.predict(X)')
