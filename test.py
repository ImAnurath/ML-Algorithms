import numpy as np

def sigmoid(t):
    return 1 / (1 + np.exp(-t))
def logloss(p, y):
    J_theta = - (y * np.log(p) + (1 - y) * np.log(1 - p))
    return J_theta

def gradientDescent(x_input, y_label, alpha):
    #theta = theta - alpha * np.gradient(logloss(p,y))
    theta = np.random.rand()
    #theta = theta - alpha * np.gradient()
    p = sigmoid(x_input[1][0])
    for i in range(len(x_input)):
        
    logloss(p,y_label[1][0])
    print(logloss(p,y_label[1][0]))
    print(f"Initial theta: {theta}")
    print(f"Optimized theta: {theta}")

learning_rate = 2

x_input = np.array([[29],
                    [15],
                    [33],
                    [28],
                    [39]])
y_label = np.array([[1],
                    [0],
                    [1],
                    [0],
                    [1]])
#gradientDescent(x_input,y_label,learning_rate)
gradientDescent(x_input,y_label,learning_rate)
