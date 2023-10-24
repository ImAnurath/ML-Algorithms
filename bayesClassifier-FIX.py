import numpy as np
def naiveBayes(x_features, y_label,test):
    label_counts = {}
    for ulabel in y_label:
        label_str = ulabel[0]
        if label_str in label_counts:
            label_counts[label_str] += 1
        else:
            label_counts[label_str] = 1
    num_unique_vals = len(label_counts)
    results = {label: 1 for label in label_counts}
    proportions = {label: round(count / len(y_label), 3) for label, count in label_counts.items()} #A B C 
    #print(proportions)
    
    count = {}
    for clabel in np.unique(y_label):
        count[clabel] = 0
    
    
    
    given_value[0][0] = x_features[0][0]
    given_value[0][0] = x_features[1][0]
    given_value[0][0] = x_features[2][0]

    given_value[0][1] = x_features[0][1]
    given_value[0][1] = x_features[1][1]
    given_value[0][1] = x_features[2][1]

    
    for column in range(len(x_features[0])):
        for row in range(len(x_features)):
            if given_value[column][0] == x_features[row][column]:
                label = y_label[row][0]
                #print(label)
                count[label] = count[label] + 1 
    

    


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
# age <= 30 == youth
# 30 < age < 51 == middle age
# 50 < age == senior
given_value = np.array([["youth"],
                        ["medium"],
                        ["yes"],
                        ["fair"],
                        ["engineer"],
                        ])
naiveBayes(x_features,y_label,given_value)
label_counts = {}
for label in y_label:
    label_str = label[0]
    if label_str in label_counts:
        label_counts[label_str] += 1
    else:
        label_counts[label_str] = 1
#print(label_counts)

num_unique_vals = len(label_counts)
results = {label: 1 for label in label_counts}

count = {}
for clabel in np.unique(y_label):
    count[clabel] = 0
#print(count)

A = round(label_counts["YES"] / len(y_label), 3)
B = round(label_counts["NO"] / len(y_label), 3)
C = round(label_counts["MAYBE"] / len(y_label), 3)

# P(A|B) = (P(B ∣ A) * P(A)) / P(B)


for column in range(len(x_features[0])): #Number of columns
    count_yes = 0
    count_no  = 0
    count_maybe = 0
    #print(f"Column: {column + 1}")
    for row in range(len(x_features)):  #Number of rows
        #print(f"Row: {row + 1}, Given: {given_value[column][0]}, X: {x_features[row][column]}, Yes: {count_yes}, No: {count_no}, Y:{y_label[row]}")
        if given_value[column][0] == x_features[row][column]:
            l = y_label[row][0]
            count[l] = count[l] + 1

            if y_label[row] == "YES":
                count_yes += 1
            elif y_label[row] == "NO":
                count_no += 1
            elif y_label[row] == "MAYBE":
                 count_maybe += 1
    results["YES"]      = round(results["YES"]    * (count_yes    / label_counts["YES"]),    3)
    results["NO"]       = round(results["NO"]     * (count_no     / label_counts["NO"]),     3)
    results["MAYBE"]    = round(results["MAYBE"]  * (count_maybe  / label_counts["MAYBE"]),  3)
    #print(results)
results["YES"]   = round(results["YES"]  * A, 3)
results["NO"]    = round(results["NO"]   * B, 3)
results["MAYBE"] = round(results["MAYBE"]* C, 3)
print(count)
#print(f"End results: {results}")