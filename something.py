# Lab05_[AD_SOYAD_NUMARA].py

import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Veri işleme ve karar ağacı oluşturma işlevi
def greedyAlgorithm(feature_matrix, label_matrix, training_data, training_label):
    X = feature_matrix
    y = label_matrix

    # Bir DecisionTreeClassifier oluşturun ve eğitin
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Karar ağacını görselleştirin
    plt.figure(figsize=(12, 8))
    plot_tree(clf, filled=True, feature_names=training_data[0])
    plt.savefig('decision_tree.png')

if __name__ == '__main__':
    # Eğitim verisini ve etiketini tanımlayın
    training_data = [
        ["Alt", "Bar", "Fri", "Hun", "Pat", "Price", "Rain", "Res", "Typ", "Est"],
        ["yes", "no", "no", "yes", "some", "$$$", "no", "yes", "French", "0-10"],
        ["yes", "no", "no", "yes", "full", "$", "no", "no", "Thai", "30-60"],
        ["no", "yes", "no", "no", "some", "$", "no", "no", "Burger", "0-10"],
        ["yes", "no", "yes", "yes", "full", "$", "yes", "no", "Thai", "10-30"],
        ["yes", "no", "yes", "no", "full", "$$$", "no", "yes", "French", ">60"],
        ["no", "yes", "no", "yes", "some", "$$", "yes", "yes", "Italian", "0-10"],
        ["no", "yes", "no", "no", "none", "$", "yes", "no", "Burger", "0-10"],
        ["no", "no", "no", "yes", "some", "$$", "yes", "yes", "Thai", "0-10"],
        ["no", "yes", "yes", "no", "full", "$", "yes", "no", "Burger", ">60"],
        ["yes", "yes", "yes", "yes", "full", "$$$", "no", "yes", "Italian", "10-30"],
        ["no", "no", "no", "no", "none", "$", "yes", "no", "Thai", "0-10"],
        ["yes", "yes", "yes", "yes", "full", "$", "no", "no", "Burger", "30-60"],
    ]

    training_label = ["yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "no", "no", "yes"]

    # Eğitim verisini özellik ve etiket matrislerine dönüştürün
    feature_matrix = np.array(training_data[1:]).T
    label_matrix = np.array([training_label])

    # Özellik ve etiket matrisleri ile greedyAlgorithm fonksiyonunu çağırın
    greedyAlgorithm(feature_matrix, label_matrix, training_data, training_label)
00000000000000000000000000000000000000000000000000000000000000000000000000000000000000
plt.clf()
import numpy as np
import matplotlib.pyplot as plt

def entropy(probabilities):
    return round(-np.sum(probabilities * np.log2(probabilities)), 3)

def information_gain():
    
    pass

# Define the Greedy Algorithm function for creating the decision tree
def greedyAlgorithm(features, labels):
    # Your implementation of the Greedy algorithm to build the decision tree goes here
    # This involves selecting the best feature to split the data, creating nodes, etc.
    # This code should recursively build the decision tree.

    # Placeholder for illustration
    plt.figure(figsize=(6, 4))
    plt.text(0.5, 0.5, 'Decision Tree\n(Not Implemented)', ha='center', va='center', size=20, alpha=0.5)
    plt.axis('off')
    plt.show()

    # This function should return the decision tree or the rules obtained from the data



x_features = np.array([#["Alt", "Bar", "Fri", "Hun", "Pat", "Price","Rain","Res", "Type",     "Est"],
                        ["yes", "no",  "no",  "yes", "some", "$$$", "no",  "yes", "French",  "0-10"],
                        ["yes", "no",  "no",  "yes", "full", "$",   "no",  "no",  "Thai",    "30-60"],
                        ["no",  "yes", "no",  "no",  "some", "$",   "no",  "no",  "Burger",  "0-10"],
                        ["yes", "no",  "yes", "yes", "full", "$",   "yes", "no",  "Thai",    "10-30"],
                        ["yes", "no",  "yes", "no",  "full", "$$$", "no",  "yes", "French",  ">60"],
                        ["no",  "yes", "no",  "yes", "some", "$$",  "yes", "yes", "Italian", "0-10"],
                        ["no",  "yes", "no",  "no",  "none", "$",   "yes", "no",  "Burger",  "0-10"],
                        ["no",  "no",  "no",  "yes", "some", "$$",  "yes", "yes", "Thai",    "0-10"],
                        ["no",  "yes", "yes", "no",  "full", "$",   "yes", "no",  "Burger",  ">60"],
                        ["yes", "yes", "yes", "yes", "full", "$$$", "no",  "yes", "Italian", "10-30"],
                        ["no",  "no",  "no",  "no",  "none", "$",   "no",  "no",  "Thai",    "0-10"],
                        ["yes", "yes", "yes", "yes", "full", "$",   "no",  "no",  "Burger",  "30-60"],
])
y_label = np.array([ ['YES'],
                     ['NO'],
                     ['YES'],
                     ['YES'],
                     ['NO'],
                     ['YES'],
                     ['NO'],
                     ['YES'],
                     ['NO'],
                     ['NO'],
                     ['NO'],
                     ['YES'],
                     ]
)


# Lab05_[AD_SOYAD_NUMARA].py

import numpy as np
from sklearn.tree import DecisionTreeClassifier, plot_tree
import matplotlib.pyplot as plt

# Veri işleme ve karar ağacı oluşturma işlevi
def greedyAlgorithm(feature_matrix, label_matrix, training_data, training_label):
    X = feature_matrix
    y = label_matrix

    # Bir DecisionTreeClassifier oluşturun ve eğitin
    clf = DecisionTreeClassifier()
    clf.fit(X, y)

    # Karar ağacını görselleştirin
    plt.figure(figsize=(12, 8))
    plot_tree(clf, filled=True, feature_names=training_data[0])
    plt.savefig('decision_tree.png')

if __name__ == '__main__':
    # Eğitim verisini ve etiketini tanımlayın
    training_data = [
        ["Alt", "Bar", "Fri", "Hun", "Pat", "Price", "Rain", "Res", "Typ", "Est"],
        ["yes", "no", "no", "yes", "some", "$$$", "no", "yes", "French", "0-10"],
        ["yes", "no", "no", "yes", "full", "$", "no", "no", "Thai", "30-60"],
        ["no", "yes", "no", "no", "some", "$", "no", "no", "Burger", "0-10"],
        ["yes", "no", "yes", "yes", "full", "$", "yes", "no", "Thai", "10-30"],
        ["yes", "no", "yes", "no", "full", "$$$", "no", "yes", "French", ">60"],
        ["no", "yes", "no", "yes", "some", "$$", "yes", "yes", "Italian", "0-10"],
        ["no", "yes", "no", "no", "none", "$", "yes", "no", "Burger", "0-10"],
        ["no", "no", "no", "yes", "some", "$$", "yes", "yes", "Thai", "0-10"],
        ["no", "yes", "yes", "no", "full", "$", "yes", "no", "Burger", ">60"],
        ["yes", "yes", "yes", "yes", "full", "$$$", "no", "yes", "Italian", "10-30"],
        ["no", "no", "no", "no", "none", "$", "yes", "no", "Thai", "0-10"],
        ["yes", "yes", "yes", "yes", "full", "$", "no", "no", "Burger", "30-60"],
    ]

    training_label = ["yes", "no", "yes", "yes", "no", "yes", "no", "yes", "no", "no", "no", "no", "yes"]

    # Eğitim verisini özellik ve etiket matrislerine dönüştürün
    feature_matrix = np.array(training_data[1:]).T
    label_matrix = np.array([training_label])

    # Özellik ve etiket matrisleri ile greedyAlgorithm fonksiyonunu çağırın
    greedyAlgorithm(feature_matrix, label_matrix, training_data, training_label)
