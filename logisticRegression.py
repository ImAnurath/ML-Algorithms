import numpy as np

def sigmoid(t):
    # t = Teta^T * x
    return 1 / (1 + np.exp(-t))
def questionTwo(p_given):
    result =  - np.log((1/p_given) - 1)
    return round((result - intercept) / slope, 2)
    
def logloss(data):
    #i = data.index()
    #jTeta = - np.power(y,i) * np.log(np.power(p,i)) + (1 - np.power(y,i)) * np.log(1 - np.power(p,i))
    '''Proably redundant ^^'''
    #AI suggestion
   
    min = 1e-15 # 0.000000000000001 to prevent log(0)
    p = np.clip(p, min, 1 - min) #if less than min set to min, if greater than 1 - min then set to 1-min
    #Prett much = (p, min, max)
    if(sigmoid(p) >= 0.5):
        y = 1
    else:
        y = 0
    jTeta = - (y * np.log(p) + (1 - y) * np.log(1 - p))

# ln(odds) = intercept + slope * data
value = 33
intercept = -64
slope = 2
data = 33

t = intercept + slope * data
p = round(sigmoid(t), 2)
print(p)


p_given = 0.95
new_data = questionTwo(p_given)
print(new_data)

'''result =  - np.log((1/p_given) - 1)
new_data = round((result - intercept) / slope, 2)'''



'''test_values = [-5, -2, -1, 0, 1, 2, 5]
t = 1 #Place holder
if(sigmoid(t) >= 0.5):
    binaryClassification = 1
else:
    binaryClassification = 0
'''


'''def gradientDescent():
    tetaOld = 1
    alpha = 5 #Rate of learning hyperparameter
    tetaNew = tetaOld - alpha * np.gradient(logloss(tetaOld))'''