import numpy as np

def naiveBayes(x_features, y_label, input):
    label_counts = {}
    for ulabel in y_label:
        label_str = ulabel[0]
        if label_str in label_counts:
            label_counts[label_str] += 1
        else:
            label_counts[label_str] = 1

    results = {label: 1 for label in label_counts} #end results
    counts = {label: 0 for label in label_counts}  #to keep the count of occurance
    label_probabilities = {label: round(count / len(y_label), 3) for label, count in label_counts.items()} #C1 C2 C3...
    for column in range(len(x_features[0])):
        for row in range(len(x_features)):
            if input[column][0] == x_features[row][column]:
                l = y_label[row][0]
                counts[l] = counts[l] + 1
        for label in label_counts:
            results[label] = round(results[label] * counts[label] / label_counts[label],3)
        counts = {key: 0 for key in counts} #Reseting the count
    for l in label_probabilities:
        results[l] = round(results[l] * label_probabilities[l], 3)
    #print(results)
    return results


x_features1 = np.array([["youth",        "high",   "no",  "fair"],
                       ["youth",        "high",   "no",  "excellent"],
                       ["middle aged",  "high",   "no",  "fair"],
                       ["senior",       "medium", "no",  "fair"],
                       ["senior",       "low",    "yes", "fair"],
                       ["senior",       "low",    "yes", "excellent"],
                       ["middle aged",  "low",    "yes", "excellent"],
                       ["youth",        "medium", "no",  "fair"],
                       ["youth",        "low",    "yes", "fair"],
                       ["senior",       "medium", "yes", "fair"],
                       ["youth",        "medium", "yes", "excellent"],
                       ["middle aged",  "medium", "no",  "excellent"],
                       ["middle aged",  "high",   "yes", "fair"],
                       ["senior",       "medium", "no",  "excellent"],
                       ])
y_label1 = np.array([["NO"],
                    ["NO"],
                    ["YES"],
                    ["YES"],
                    ["YES"],
                    ["NO"],
                    ["YES"],
                    ["NO"],
                    ["YES"],
                    ["YES"],
                    ["YES"],
                    ["YES"],
                    ["YES"],
                    ["NO"],
                    ])

input1 = np.array([["youth"],
                        ["medium"],
                        ["yes"],
                        ["fair"],
                        ])

#-------------------------------------------------------------------------------------------------------------------

x_features2 = np.array([["youth",        "high",   "no",  "fair",      "engineer"],
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
y_label2 = np.array([["NO"],
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
input2 = np.array([      ["youth"],
                        ["medium"],
                        ["yes"],
                        ["fair"],
                        ["engineer"],
                        ])

test1 = naiveBayes(x_features1, y_label1, input1)
test2 = naiveBayes(x_features2, y_label2, input2)
print(f"Test 1 restuls: {test1}\nTest 2 results: {test2}")