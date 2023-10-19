import numpy as np

x_features = np.array([["youth",        "high",   "no",  "fair"],
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
y_label = np.array([["NO"],
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
                    #["MAYBE"]
                    ])
# age <= 30 == youth
# 30 < age < 51 == middle age
# 50 < age == senior
given_value = np.array([["youth"],
                        ["medium"],
                        ["yes"],
                        ["fair"],
                        ])
label_counts = {}
for label in y_label:
    label_str = label[0]
    if label_str in label_counts:
        label_counts[label_str] += 1
    else:
        label_counts[label_str] = 1
print(label_counts)

#unique_labels, label_count = np.unique(y_label,return_counts=True)
num_unique_vals = len(label_counts)
#results = np.zeros(num_unique_vals) # Results size of unique labels
results = {label: 1 for label in label_counts}
print(results)
A = round(label_counts["YES"] / len(y_label), 3)
B = round(label_counts["NO"] / len(y_label), 3)
print(A, B)
#C = round(label_counts["MAYBE"] / len(y_label), 3)
# P(A|B) = (P(B ∣ A) * P(A)) / P(B)

for column in range(len(x_features[0])): #Number of columns
    count_yes = 0
    count_no  = 0
    #count_maybe = 0
    print(f"Column: {column + 1}")
    for row in range(len(x_features)):  #Number of rows
        print(f"Row: {row + 1}, Given: {given_value[column][0]}, X: {x_features[row][column]}, Yes: {count_yes}, No: {count_no}, Y:{y_label[row]}")
        if given_value[column][0] == x_features[row][column]:
            if y_label[row] == "YES":
                count_yes += 1
            elif y_label[row] == "NO":
                count_no += 1
            #elif y_label[row] == "MAYBE":
            #     count_maybe += 1
    results["YES"]      = round(results["YES"]    * (count_yes    / label_counts["YES"]),    3)
    results["NO"]       = round(results["NO"]     * (count_no     / label_counts["NO"]),     3)
    #results["MAYBE"]    = round(results["MAYBE"]  * (count_maybe  / label_counts["MAYBE"]),  3)
    print(results)
results["YES"]  = round(results["YES"] * A, 3)
results["NO"]   = round(results["NO"]  * B, 3)
print(f"End results: {results}")