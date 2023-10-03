import numpy as np

# Define the matrices X and Y
X = np.array([
    [2, 1, 1],
    [16, 28, 1],
    [28, 99, 1],
    [36, 126, 1],
    [82, 128, 1],
    [114, 137, 1],
    [165, 199, 1],
    [256, 211, 1],
    [519, 300, 1]
])

Y = np.array([
    [5],
    [8],
    [11],
    [92],
    [178],
    [368],
    [427],
    [513],
    [521]
])

# Calculate the coefficients
beta = np.linalg.inv(X.T @ X) @ X.T @ Y

print("Coefficients:")
print(beta)
