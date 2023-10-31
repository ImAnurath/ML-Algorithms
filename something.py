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
