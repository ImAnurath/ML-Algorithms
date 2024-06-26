import numpy as np

import numpy as np

def entropy(probabilities):
    return round(-np.sum(probabilities * np.log2(probabilities)), 3)


'''def conditional_entropy(data, col_index):
    
    # Extract the specific column for analysis
    column_to_analyze = data[0:, col_index]
    
    # Count occurrences of each value in the column
    keys ,counts = np.unique(column_to_analyze, return_counts=True)
    counts = counts / len(data)
    probabilities = dict(zip(keys, np.round(counts,3)))
    # Total number of entries in the column
    conditional_entropy_result = 0
    print(probabilities)
    for val in probabilities.values():
        print(entropy(val))'''


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
#Joint entropy = H(X,Y) = - EE p(x,y)log2p(x,y)
#Conditional entropy =    - E p(y|x)log2p(y|x)     p(y|x)= p(x,y)/p(px)
#conditional_entropy(x_features,4)
'''
for i in range(len(x_features[0])):
    ent = entropy(x_features[:, i])
    print(f"Column number {i}, Entropy:{ent}")


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

results = []
for features in x_features:
    feature = features[4]
    if feature == "none":
        results.append("FALSE")
    elif feature == "some":
        results.append("TRUE")
    elif feature== "full":
        results.append("NEXT")

print(results)'''

import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

# Create a plot
fig, ax = plt.subplots()

# Draw nodes
ax.plot([1.5, 1.5], [2.99, 2.99], marker='o', markersize=10, color='blue')  # Root node
ax.plot([0.5, 0.9], [0.9, 0.6], marker='o', markersize=10, color='blue')  # Root node

# Draw edges
ax.plot([0.5, 0.1], [0.9, 0.6], color='black')  # Left branch
ax.plot([0.5, 0.9], [0.9, 0.6], color='black')  # Right branch

# Add text for nodes
ax.text(1.5, 3.1, 'Feature X', ha='center', va='center', fontsize=12)
ax.text(0.1, 0.6, 'Decision 1', ha='center', va='center', fontsize=12)
ax.text(0.9, 0.6, 'Decision 2', ha='center', va='center', fontsize=12)

# Add rectangles on top of the nodes
rect1 = Rectangle((0.1 - 0.1, 0.6 - 0.05), 0.2, 0.2, linewidth=1, edgecolor='black', facecolor='lightgray')
rect2 = Rectangle((0.9 - 0.1, 0.6 - 0.05), 0.2, 0.2, linewidth=1, edgecolor='black', facecolor='lightgray')

ax.add_patch(rect1)
ax.add_patch(rect2)

# Customize plot appearance
ax.set_xlim(0, 3)
ax.set_ylim(0, 3)
ax.axis('on')

# Display the plot
plt.show()
