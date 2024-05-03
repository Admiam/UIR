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

def update_medoids(clusters):
    medoids = []
    for cluster_points in clusters.values():
        cluster_points = np.array(cluster_points)
        min_cost = float('inf')
        best_medoid = None
        for point in cluster_points:
            cost = sum(euclidean_distance(point, other_point) for other_point in cluster_points)
            if cost < min_cost:
                min_cost = cost
                best_medoid = point
        medoids.append(best_medoid)
    return np.array(medoids)

def k_means(data, initial_centroids, num_clusters, max_iterations=100):
    centroids = initial_centroids
    iterations = 0
    for _ in range(max_iterations):
        iterations += 1
        clusters = assign_clusters(data, centroids)
        new_centroids = update_centroids(clusters)
        if np.array_equal(centroids, new_centroids):
            print("Iteration ", iterations, ": centroids", centroids)
            break
        centroids = new_centroids
        print("Iteration ",iterations,": centroids", centroids)
    return clusters, centroids

def read_file(file_name):
    with open(file_name, "r") as f:
        data = []
        initial_centroids = []
        f.readline()
        file_data = f.readline()

        while file_data != "init.x;init.y":
            parts = file_data.split(";")
            print(file_data)
            data.append([int(parts[0]), int(parts[1])])
            file_data = f.readline().strip()

        print("Centroids")
        file_data = f.readline()
        while file_data:
            print(file_data)
            parts = file_data.split(";")
            initial_centroids.append([int(parts[0]), int(parts[1])])
            file_data = f.readline().strip()

    return np.array(data), np.array(initial_centroids)



# Example usage:
if __name__ == "__main__":
    data, initial_centroids = read_file("cv7_vstup.txt")

    length = initial_centroids.shape[0]

    clusters, centroids = k_means(data, initial_centroids, num_clusters=length)

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
