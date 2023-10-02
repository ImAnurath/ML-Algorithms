def addition(mat1, mat2):
    row1 = len(mat1)
    col1 = len(mat1[0])
    row2 = len(mat2)
    col2 = len(mat2[0])
    if(row1 == row2 and col1 == col2):
        for outterIndex in range(len(mat1)):
            for innerIndex in range(len(mat1)):
                a = mat1[outterIndex][innerIndex] + mat2[outterIndex][innerIndex]
                print(a)
    else:
        return

def inverse_3x3_matrix(matrix):
    if len(matrix) != 3 or len(matrix[0]) != 3 or len(matrix[1]) != 3 or len(matrix[2]) != 3:
        raise ValueError("Input matrix must be a 3x3 matrix.")
    a, b, c = matrix[0]
    d, e, f = matrix[1]
    g, h, i = matrix[2]
    determinant = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    if determinant == 0:
        raise ValueError("The matrix is singular and does not have an inverse.")
    inverse = [
        [(e * i - f * h) / determinant, (c * h - b * i) / determinant, (b * f - c * e) / determinant],
        [(f * g - d * i) / determinant, (a * i - c * g) / determinant, (c * d - a * f) / determinant],
        [(d * h - e * g) / determinant, (b * g - a * h) / determinant, (a * e - b * d) / determinant]
    ]

    return inverse

def inverse_2x2_matrix(matrix):
    if len(matrix) != 2 or len(matrix[0]) != 2 or len(matrix[1]) != 2:
        raise ValueError("Input matrix must be a 2x2 matrix.")
    determinant = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]

    if determinant == 0:
        raise ValueError("The matrix is singular and does not have an inverse.")

    inverse = [
        [matrix[1][1] / determinant, -matrix[0][1] / determinant],
        [-matrix[1][0] / determinant, matrix[0][0] / determinant]
    ]

    return inverse

def transpose(matrix):
    transpose = [[0 for _ in range(len(matrix))] for _ in range(len(matrix[0]))]
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            transpose[i][j] = matrix[j][i]
    return transpose

def matrix_multiplication(matrix1, matrix2):
    # Check if the matrices can be multiplied
    if len(matrix1[0]) != len(matrix2):
        raise ValueError("Matrix dimensions are not compatible for multiplication")

    # Initialize the result matrix with zeros
    result = [[0 for _ in range(len(matrix2[0]))] for _ in range(len(matrix1))]

    # Perform the matrix multiplication
    for i in range(len(matrix1)):
        for j in range(len(matrix2[0])):
            for k in range(len(matrix2)):
                result[i][j] += matrix1[i][k] * matrix2[k][j]
    return result

def least_square(x, y):
    # Y = AX + E
    # Y -> y-axis, X -> x-axis , E -> Error, A -> gives y-intercept and slope
    # A == (X^T * X)^-1 * X^T * Y
    # A = matrix_multiplication(matrix_multiplication(inverse_2x2_matrix(matrix_multiplication(transpose(x), x)), transpose(x)), y) #The menace
    step0 = matrix_multiplication(transpose(x), x)
    step1 = inverse_2x2_matrix(step0)
    step2 = matrix_multiplication(step1, transpose(x))
    step3 = matrix_multiplication(step2, y)
    b = round(step3[0][0], 1) # y-intercept
    m = round(step3[1][0], 1) # slope
    # f(x) = b + mx
    # E = y - f(xi)
    # Next step is to create an empty matrix that has # of rows that is equal to x and y matricies
    errors = [[0.0 for _ in range(len(y[0]))] for _ in range(len(y))]
    for i in range(len(y)):
        f = round(b + m*x[i][1], 2)
        errors[i][0] = y[i][0] - f
    # Sum of square of the errors = SSE
    SSE = matrix_multiplication(transpose(errors), errors)
    print(SSE)


x = [[1,49],
     [1,69],
     [1,89],
     [1,99],
     [1,109]
     ]

y = [[124],
     [95],
     [71],
     [45],
     [18]
     ]

least_square(x,y)
#result = matrix_multiplication(x,y)
#result = inverse_2x2_matrix(x)
#result = inverse_3x3_matrix(y)
#result = transpose(x)
#for row in result:
#    print(row)
