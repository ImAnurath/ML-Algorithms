import numpy as np

def euclidean_distance(point1, point2):
    point1 = np.asarray(point1, dtype=np.float64)  # Ensure point1 is a numeric array
    point2 = np.asarray(point2, dtype=np.float64)  # Ensure point2 is a numeric array
    return np.sqrt(np.sum((point1 - point2) ** 2))

def knn_classifier(sample, new_data, k):
    #distances = np.array([euclidean_distance(sample_point[:2], new_data) for sample_point in sample])
    
    distances = np.zeros(len(sample))
    for i, sample_point in enumerate(sample):
        #distances[i] = euclidean_distance(sample_point[:2], new_data)
        distances[i] = euclidean_distance( new_data, sample_point[:2])
    nearest_indices = np.argsort(distances)[:k]
    nearest_labels = sample[nearest_indices, 2]
    unique_labels, counts = np.unique(nearest_labels, return_counts=True)
    predicted_label = unique_labels[np.argmax(counts)]
    return predicted_label

sample = np.array([
    [150, 0.8, 'Apple'],
    [130, 0.7, 'Apple'],
    [120, 0.9, 'Banana'],
    [140, 0.8, 'Banana'],
    [160, 0.95, 'Orange'],
    [155, 0.92, 'Orange'],
    [40, 0.3, 'Grape'],
    [45, 0.25, 'Grape']
])
new_data = np.array([165, 0.85])
k = 2
print(knn_classifier(sample, new_data, k))
