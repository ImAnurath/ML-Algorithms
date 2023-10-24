import numpy as np

def naiveBayes(x_features, y_label, given_value):
    label_counts = {}
    label_values = np.unique(y_label)
    for label in label_values:
        label_str = label[0]
        label_counts[label_str] = np.sum(y_label == label)
    
    results = {label_str: 1 for label_str in label_counts}
    
    probabilities = {}
    for label_str in label_counts:
        probabilities[label_str] = label_counts[label_str] / len(y_label)
    
    for column in range(len(x_features[0])):
        for label_str in label_counts:
            count = np.sum((y_label == label_str) & (x_features[:, column] == given_value[column][0]))
            results[label_str] *= count / label_counts[label_str]
    
    for label_str in label_counts:
        results[label_str] *= probabilities[label_str]

    return results

x_features = np.array([["youth",        "high",   "no",  "fair",      "engineer"],
                       ["youth",        "high",   "no",  "excellent", "lawyer"],
                       ["middle aged",  "high",   "no",  "fair",      "engineer"],
                       ["senior",       "medium", "no",  "fair",      "lawyer"],
                       ["senior",       "low",    "yes", "fair",      "engineer"],
                       ["senior",       "low",    "yes", "excellent", "engineer"],
                       ["middle aged",  "low",    "yes", "excellent", "engineer"],
                       ["youth",        "medium", "no",  "fair",      "lawyer"],
                       ["youth",        "low",    "yes", "fair",      "lawyer"],
                       ["senior",       "medium", "yes", "fair",      "lawyer"],
                       ["youth",        "medium", "yes", "excellent", "engineer"],
                       ["middle aged",  "medium", "no",  "excellent", "lawyer"],
                       ["middle aged",  "high",   "yes", "fair",      "engineer"],
                       ["senior",       "medium", "no",  "excellent", "lawyer"],
                       ["youth",        "low",    "no",  "excellent", "lawyer"],
                       ["middle aged",  "high",   "yes", "fair",      "engineer"],
                       ["senior",       "medium", "no",  "excellent", "lawyer"],
                       ])
y_label = np.array([["NO"],
                    ["NO"],
                    ["YES"],
                    ["MAYBE"],
                    ["YES"],
                    ["NO"],
                    ["MAYBE"],
                    ["NO"],
                    ["YES"],
                    ["MAYBE"],
                    ["YES"],
                    ["YES"],
                    ["MAYBE"],
                    ["NO"],
                    ["MAYBE"],
                    ["NO"],
                    ["NO"]
                    ])
given_value = given_value = np.array([["youth"],
                        ["medium"],
                        ["yes"],
                        ["fair"],
                        ["engineer"],
                        ])

results = naiveBayes(x_features, y_label, given_value)
print(f"End results: {results}")
