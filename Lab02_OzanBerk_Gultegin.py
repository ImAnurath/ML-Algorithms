import numpy as np

def euclidean_distance(x, y):
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    return np.sqrt(np.sum((x - y) ** 2))

def kNN(feautre, label, k):
    #distances = np.array([euclidean_distance(feautre_point[:2], new_data) for feautre_point in feautre])
    distances = np.zeros(len(feautre))
    for i, feautre_point in enumerate(feautre):
        distances[i] = euclidean_distance( label, feautre_point[:len(feautre[0])-1]) #len(feautre[0])-1: Number of feautres in the matrix = 3
    nearest_indices = np.argsort(distances)[:k]                                      #Assumed the last column is for label
    nearest_labels = feautre[nearest_indices, len(feautre[0])-1] #len(feautre[0])-1
    unique_labels, counts = np.unique(nearest_labels, return_counts=True)
    max_count = np.max(counts)
    if np.sum(counts == max_count) > 1:
        return 'UNIDENTIFIED'
    else:
        predicted_label = unique_labels[np.argmax(counts)]
        return predicted_label
feautre1 = np.array([
    [35, 35,  3,  'NO'],
    [22, 50,  2,  'YES'],
    [63, 200, 1,  'NO'],
    [59, 170, 1,  'NO'],
    [25, 40,  4,  'YES'],
])
feautre2 = np.array([
    [35, 35,  3,  'NO'],
    [22, 50,  2,  'YES'],
    [63, 200, 1,  'NO'],
    [59, 170, 1,  'NO'],
    [25, 40,  4,  'YES'],
    [35, 50,  1,  'MAYBE'],
    [55, 80,  3,  'YES'],
    [22, 120, 4,  'MAYBE']
])
label = np.array([37, 50, 2])
print("Test 1 Results: ")
for k in range(1,6):
    print(f"K= {k}  kNN: {kNN(feautre1,label,k)}")
print("Test 2 Results: ")
for k in range(1,9):
    print(f"K= {k}  kNN: {kNN(feautre2,label,k)}")

