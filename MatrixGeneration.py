import random

def GENERATE(n):
    #set up the Matrix
    """Takes in 2 parameters: 1. the blank matrix to fill with generated values
    2. the number of rows and items(generates an NxN matrix) """

    global Matrix
    Matrix = []
    #set up the matrix
    for i in range(n):
        Matrix.append([])
        for j in range(n):
            Matrix[i].append(0)

    for j in range(0,n):
        Matrix[j][j] = 2
        for i in range(j+1,n): #maybe from 1,2?
            Matrix[j][i] = -1
            Matrix[i][j] = -1
            break
    print(type(Matrix))

def MatPrint(matrix):
    n = len(matrix)
    print("__Matrix__", " = ")
    for i in range(n):
        print(matrix[i])

"""RAND(size) Makes a random square matrix of a specified size and specified range, range should be a positive number"""

def RAND(size, Range):
    R = []
    for i in range(size):
        R.append([])
        for j in range(size):
            R[i].append(random.randrange(-Range,Range))
        R[i][i] = 2
    return R

def diagonalCheck(A , num_to_check):
    check = 0
    for i in range(len(A)):
        if A[i][i] == num_to_check:
            check += 1
    if check == len(A):
        print("all diagonal elements are ",num_to_check)
    else:
        print("not all diagonal elements are ",num_to_check)
