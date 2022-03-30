# Special thanks to Dr. Charles Thangaraj
import random


def GENERATE(n):
    # set up the Matrix
    """Takes in 2 parameters: 1. the blank matrix to fill with generated values
    2. the number of rows and items(generates an NxN tridiagonal matrix) """
    Matrix = []
    # set up the matrix
    for i in range(n):
        Matrix.append([])
        for j in range(n):
            Matrix[i].append(0)

    for j in range(0, n):  # represents the previous row
        Matrix[j][j] = 2
        for i in range(j + 1, n):  # represents the next row
            Matrix[j][i] = -1
            Matrix[i][j] = -1  # stores -1 on the next row
            break
    return Matrix


def MatPrint(matrix, n):
    for i in range(n):
        print(matrix[i])
    return


def MultMatrix(a, b):
    """returns the product of two square matrices"""
    c = []
    n = len(a)
    # set up the matrix
    for i in range(n):
        c.append([])
        for j in range(n):
            c[i].append(0)

    for i in range(n):
        for j in range(n):
            sum = 0
            for k in range(n):
                sum += a[i][k] * b[k][j]
            c[i][j] = sum

    return c


def RAND(size, Range):
    """RAND(size) Makes a random square matrix of a specified size and specified range, range should be a positive number"""

    R = []
    for i in range(size):
        R.append([])
        for j in range(size):
            R[i].append(random.randrange(-Range, Range))
        R[i][i] = 2
    return R


def dCheck(A, num_to_check):
    check = 0
    for i in range(len(A)):
        if A[i][i] == num_to_check:
            check += 1
    if check == len(A):
        print("all diagonal elements are ", num_to_check)
    else:
        print("not all diagonal elements are ", num_to_check)
    return


def B_VExact_Yj_GENERATE(n, H, L, Delta_P, Nu):
    Delta_Y = (2 * H) / (n + 1)
    V_max = (Delta_P * H ** 2) / (2 * Nu * L)
    F_j = (Delta_Y ** 2 * (2 * V_max)) / (H ** 2)  #in terms of Vmax, equation 75,pg 29

    B = [F_j for i in range(n)]

    EV = []
    Y_j_LIST = []

    # calculate Y_j and V_exact and append it to their respective lists for data processing
    for i in range(0, n + 2):
        Y_j = -H + i * Delta_Y
        Y_j_LIST.append(Y_j)
        EV.append(V_max * (1 - (Y_j / H) ** 2))

    return B, EV, Y_j_LIST
