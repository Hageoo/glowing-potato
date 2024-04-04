import numpy as np
cimport numpy as np

cdef class KMeansCython:
    cdef int K
    cdef int max_iters
    cdef np.ndarray centroids

    def __cinit__(self, int K, int max_iters):
        self.K = K
        self.max_iters = max_iters
        self.centroids = np.empty((K, 2), dtype=np.float64)

    cpdef fit_predict(self, np.ndarray[np.float64_t, ndim=2] X):
        cdef int n_samples = X.shape[0]
        cdef int n_features = X.shape[1]
        cdef np.ndarray[np.int32_t, ndim=1] labels = np.empty(n_samples, dtype=np.int32)
        cdef np.ndarray[np.float64_t, ndim=2] distances = np.empty((n_samples, self.K), dtype=np.float64)
        cdef np.ndarray[np.float64_t, ndim=2] new_centroids = np.zeros((self.K, n_features), dtype=np.float64)
        cdef np.ndarray[np.int32_t, ndim=1] cluster_counts = np.zeros(self.K, dtype=np.int32)
        
        # Initialize centroids
        for i in range(self.K):
            self.centroids[i] = X[np.random.randint(0, n_samples)]
        
        for _ in range(self.max_iters):
            # Compute distances between points and centroids
            for i in range(self.K):
                distances[:, i] = np.sum((X - self.centroids[i])**2, axis=1)
            
            # Assign samples to closest centroids
            labels = np.argmin(distances, axis=1).astype(np.int32)
            
            # Update centroids incrementally
            new_centroids.fill(0)
            cluster_counts.fill(0)
            for i in range(n_samples):
                cluster_idx = labels[i]
                new_centroids[cluster_idx] += X[i]
                cluster_counts[cluster_idx] += 1
            for i in range(self.K):
                if cluster_counts[i] > 0:
                    self.centroids[i] = new_centroids[i] / cluster_counts[i]
        
        return labels
