import random

def GENERATE(n):
    #set up the Matrix
    """Takes in 2 parameters: 1. the blank matrix to fill with generated values
    2. the number of rows and items(generates an NxN matrix) """
    Matrix = []
    #set up the matrix
    for i in range(n):
        Matrix.append([])
        for j in range(n):
            Matrix[i].append(0)

    for j in range(0,n): # represents the previous row
        Matrix[j][j] = 2
        for i in range(j+1,n): # represents the next row
            Matrix[j][i] = -1
            Matrix[i][j] = -1 # stores -1 on the next row
            break
    return Matrix

def MatPrint(matrix,n):
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

def dCheck(A , num_to_check):
    check = 0
    for i in range(len(A)):
        if A[i][i] == num_to_check:
            check += 1
    if check == len(A):
        print("all diagonal elements are ",num_to_check)
    else:
        print("not all diagonal elements are ",num_to_check)

def B_VExact_Yj_GENERATE(n,H,L,Delta_P,Viscosity):
    Delta_Y = (2 * H) / 4
    V_max = (Delta_P * H ** 2) / (2 * Viscosity * L)

    F_j = ((Delta_Y)**2 * (2*V_max))/(H**2)

    B = []
    for i in range(n):
        B.append(0)

    for i in range(n):
        B[i] = F_j

    V_exact_LIST = []
    Y_j_LIST = []

    # calculate Y_j and V_exact and append it to their respective lists for data processing
    for i in range(n):
        Y_j = (-H + i * Delta_Y)
        Y_j_LIST.append(Y_j)
        V_exact_LIST.append(V_max * (1 - (Y_j / H) ** 2))

    return B,V_exact_LIST,Y_j_LIST
