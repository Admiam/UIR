import numpy as np
import matplotlib.pyplot as plt


def fit(data, labels):
    centroids = {}
    classes = np.unique(labels)
    for c in classes:
        # print()
        arr = []
        for i in range(len(data)):
            # print(i)
            if c == labels[i]:
                # print(data[i])
                arr.append(data[i])

        centroids[c] = np.mean(arr, axis=0)
        # print(self.centroids[c])
    return centroids

def predict(centroids, X_test, classes):
    predictions = []
    c = np.unique(classes)
    print("Nearest centroids")
    for x in X_test:
        distances = [np.linalg.norm(x - centroid) for centroid in centroids.values()]
        # print(distances)
        pairs = zip(distances, c)
        predicted_class = min(pairs)
        print(predicted_class)
        predictions.append(predicted_class)
    return predictions


class KNNClassifier:
    def __init__(self, k=1):
        self.k = k

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        print("KNN Classifier")
        for x in X_test:
            distances = [np.linalg.norm(x - x_train) for x_train in self.X_train]
            nearest_indices = np.argsort(distances)[:self.k]
            nearest_classes = [self.y_train[i] for i in nearest_indices]
            predicted_class = max(set(nearest_classes), key=nearest_classes.count)
            # print(nearest_indices)
            print(predicted_class, nearest_indices)
            predictions.append(predicted_class)
        return predictions


# class DecisionTreeClassifier:
#     def __init__(self, max_depth=None):
#         self.max_depth = max_depth
#
#     def fit(self, X_train, y_train):
#         pass  # To be implemented
#
#     def predict(self, X_test):
#         pass  # To be implemented


# Read data from file
def read_data(file_path):
    with open(file_path, "r") as f:
        data = []
        labels = []
        X_test = []
        f.readline()
        file_data = f.readline().strip()

        while file_data != "test.x;test.y":
            parts = file_data.split(";")
            # print(file_data)
            data.append([int(parts[0]), int(parts[1])])
            labels.append(parts[2])
            file_data = f.readline().strip()

        # print("Centroids")
        file_data = f.readline().strip()
        while file_data:
            # print(file_data)
            parts = file_data.split(";")
            X_test.append([int(parts[0]), int(parts[1])])
            file_data = f.readline().strip()

    return np.array(data),np.array(labels), np.array(X_test)


# Sample usage
data, labels, X_test = read_data("cv8_vstup.txt")
# X_test = np.array([[1, 1], [17, 12], [43, 34], [18, 28]])

centroids = fit(data, labels)
nc_predictions = predict(centroids, X_test, labels)

knn_classifier = KNNClassifier(k=1)
knn_classifier.fit(data, labels)
knn_predictions = knn_classifier.predict(X_test)


plt.figure(figsize=(8, 6))

for label in np.unique(labels):
    plt.scatter(data[labels == label][:, 0], data[labels == label][:, 1], label=f'Training Class {label}')

for i, (prediction, test_point) in enumerate(zip(nc_predictions, X_test)):
    plt.scatter(test_point[0], test_point[1], color='blue', marker=f'${prediction[1]}$', label=f'Test Point {i+1}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('Nearest Centroid Predictions')
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))

for label in np.unique(labels):
    plt.scatter(data[labels == label][:, 0], data[labels == label][:, 1], label=f'Training Class {label}')

for i, (prediction, test_point) in enumerate(zip(knn_predictions, X_test)):
    plt.scatter(test_point[0], test_point[1], color='red', marker=f'${prediction}$', label=f'Test Point {i+1}')

plt.xlabel('x')
plt.ylabel('y')
plt.title('KNN Predictions')
plt.legend()
plt.grid(True)
plt.show()

