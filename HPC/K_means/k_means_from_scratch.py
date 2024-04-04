import cProfile
import random
import math

# Almost from scratch, importing a couple models for convenience, either way we are not making the most out of it as we do not include arrays from NumPy

class KMeans:

    def __init__(self, K=5, max_iters=100):
        self.K = K
        self.max_iters = max_iters

        # list of sample indices for each cluster
        self.clusters = [[] for _ in range(self.K)]

        # the centers (mean vector) for each cluster
        self.centroids = []

    def predict(self, X):
        self.X = X
        self.n_samples, self.n_features = self.X.shape

        # initialize
        random_sample_idxs = random.sample(range(self.n_samples), self.K)
        self.centroids = [self.X[idx].tolist() for idx in random_sample_idxs]

        # optimize clusters
        for _ in range(self.max_iters):
            # assign samples to closest centroids (create clusters)
            self.clusters = self._create_clusters(self.centroids)

            # calculate new centroids from the clusters
            centroids_old = self.centroids
            self.centroids = self._get_centroids(self.clusters)

            if self._is_converged(centroids_old, self.centroids):
                break

        # classify samples as the index of their clusters
        return self._get_cluster_labels(self.clusters)

    def _get_cluster_labels(self, clusters):
        # each sample will get the label of the cluster it was assigned to
        labels = [None for _ in range(self.n_samples)]
        for cluster_idx, cluster in enumerate(clusters):
            for sample_idx in cluster:
                labels[sample_idx] = cluster_idx

        return labels

    def _create_clusters(self, centroids):
        # assign the samples to the closest centroids
        clusters = [[] for _ in range(self.K)]
        for idx, sample in enumerate(self.X):
            centroid_idx = self._closest_centroid(sample.tolist(), centroids)
            clusters[centroid_idx].append(idx)
        return clusters

    def _closest_centroid(self, sample, centroids):
        # distance of the current sample to each centroid
        distances = [self._euclidean_distance(sample, point) for point in centroids]
        closest_idx = min(range(len(distances)), key=distances.__getitem__)
        return closest_idx

    def _get_centroids(self, clusters):
        # assign mean value of clusters to centroids
        centroids = [[] for _ in range(self.K)]
        for cluster_idx, cluster in enumerate(clusters):
            cluster_mean = self._mean(cluster)
            centroids[cluster_idx] = cluster_mean
        return centroids

    def _is_converged(self, centroids_old, centroids):
        # distances between old and new centroids, for all centroids
        distances = [self._euclidean_distance(centroids_old[i], centroids[i]) for i in range(self.K)]
        return sum(distances) == 0

    def _euclidean_distance(self, x1, x2):
        return math.sqrt(sum([(a - b) ** 2 for a, b in zip(x1, x2)]))

    def _mean(self, cluster):
        return [sum(col) / len(col) for col in zip(*[self.X[idx] for idx in cluster])]

# Testing
if __name__ == "__main__":
    random.seed(42)
    from sklearn.datasets import make_blobs

    X, y = make_blobs(
        centers=3, n_samples=1000000, n_features=2, shuffle=True, random_state=40
    )
    print(X.shape)

    clusters = len(set(y))
    print(clusters)

    # Create an instance of KMeans
    k = KMeans(K=clusters, max_iters=150)

    # Profiling the predict method of KMeans
    cProfile.run('k.predict(X)')
