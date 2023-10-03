import numpy as np

def leastSquares(A, Y):
    # A == (X^T * X)^-1 * X^T * Y
    trans = A.transpose()
    mult = np.matmul(trans, A)
    inv = np.linalg.inv(mult)
    sec = np.matmul(inv, trans)
    beta = np.matmul(sec, Y)
    #print(beta)
    return beta
X0 = np.array([[0],
              [1],
              [2],
              [3],
              [4]
              ])

Y0 = np.array([[0.2],
              [2.9],
              [3.3],
              [7.2],
              [8.5]
             ])

X1 = np.array([  [2,1,1],
                [16,28,1],
                [28,99,1],
                [36,126,1],
                [82,128,1],
                [114,137,1],
                [165,199,1],
                [256,211,1],
                [519,300,1]
    
])
Y1 = np.array([ [5],
               [8],
               [11],
               [92],
               [178],
               [368],
               [427],
               [513],
               [521]
    
])
X2 = np.array([ [2,1,88,4,1,1],
                [16,28,98,12,15,1],
                [28,99,99,17,22,1],
                [36,126,121,22,96,1],
                [82,128,145,35,196,1],
                [114,137,199,46,211,1],
                [165,199,217,52,214,1],
                [256,211,356,63,250,1],
                [519,300,437,75,275,1],
                [675,315,499,87,298,1],
                [852,550, 512,94, 317,1],
                [987,865, 535,98,356,1],
                [1023,987, 675,126, 398,1],
                [1124,999, 698,135,417,1],
                [1568,1022, 703,167,419,1],
                [1999,1035,712,211,550,1],
                [2500,1059, 715,2222,650,1]
               
                
    
])

Y2 = np.array([ [5],
               [8],
               [11],
               [92],
               [178],
               [368],
               [427],
               [513],
               [521],
               [567],
               [589],
               [612],
               [678],
               [698],
               [812],
               [835],
               [935]
               
               
    
])
LRG = leastSquares(X2,Y2)
test = np.linalg.lstsq(X,Y,rcond=None)
print(f"Actual: {test[0]}")
print(f"Mine: {LRG}")
