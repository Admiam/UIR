import numpy as np
import matplotlib.pyplot as plt

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def assign_clusters(data, centroids):
    clusters = {}
    for point in data:
        distances = [euclidean_distance(point, centroid) for centroid in centroids]
        cluster_idx = np.argmin(distances)
        if cluster_idx not in clusters:
            clusters[cluster_idx] = []
        clusters[cluster_idx].append(point)
    return clusters

def update_centroids(clusters):
    centroids = []
    for cluster_points in clusters.values():
        cluster_points = np.array(cluster_points)
        centroid = np.mean(cluster_points, axis=0)
        centroids.append(centroid)
    return np.array(centroids)

def k_means(data, initial_centroids, num_clusters, max_iterations=100):
    centroids = initial_centroids
    for _ in range(max_iterations):
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if np.array_equal(centroids, new_centroids):
            break
        centroids = new_centroids
    return clusters, centroids

# Example usage:
data = np.array([[2, 4], [15, 18], [5, 50], [30, 34], [65, 2], [4, 5]])
initial_centroids = np.array([[2, 4], [15, 18]])

clusters, centroids = k_means(data, initial_centroids, num_clusters=2)

# Plotting
plt.figure(figsize=(8, 6))
colors = ['r', 'g', 'b', 'c', 'm', 'y', 'k']
for i, cluster_points in clusters.items():
    cluster_points = np.array(cluster_points)
    plt.scatter(cluster_points[:, 0], cluster_points[:, 1], color=colors[i], label=f'Cluster {i+1}')
plt.scatter(centroids[:, 0], centroids[:, 1], color='black', marker='x', label='Centroids')
plt.xlabel('X')
plt.ylabel('Y')
plt.title('k-Means Clustering')
plt.legend()
plt.grid(True)
plt.show()
