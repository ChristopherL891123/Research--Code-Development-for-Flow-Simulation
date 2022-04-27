# The purpose of this file is to calculate the exact solutions of a matrix using LU decomposition.
# Special thanks to Dr. John Starner

import MatrixGeneration


# Decomposition algorithm
def DECOMP(A, n, SHOW_LU):
    L = []
    for i in range(n):
        L.append([])
        for j in range(n):
            L[i].append(0)
    for i in range(n):
        L[i][i] = 1
    U = A.copy()
    for j in range(0, n - 1):
        for i in range(j + 1, n):
            factor = U[i][j] / U[j][j]
            L[i][j] = factor
            for k in range(0, n):
                U[i][k] = U[i][k] - (factor * U[j][k])
    return U, L

# forward substitution algorithm
def FORWARD_SUB(n, L, B, SHOW_y):
    y = []
    for i in range(n):
        y.append(0)
    for i in range(0, n):
        sum_row = 0
        for j in range(0, i):
            sum_row += L[i][j] * y[j]
        y[i] = (-1 * sum_row) + B[i]
    return y


# backward substitution algorithm
def BACKWARD_SUB(y, n, U, SHOW_x):
    x = [0 for i in range(n + 1)]
    for i in range(-1, -n - 1, -1):
        sum_row = 0
        for j in range(i, 0):
            sum_row += U[i][j] * x[j]
        x[i] = ((-1 * sum_row) + y[i]) / U[i][i]
    return x


def TabPrint(n, header, Y_j, x, EV, ABS_ERR, REL_ERR):
    """Returns the table with the values. Adapted from
    https://www.codegrepper.com/code-examples/python/how+to+create+table+format+python+console+output+without+library"""

    tableString = ""

    b = "|{: ^8} | {: ^30} | {: ^30} | {: ^30} | {: ^30}|{: ^30}|".format(*header)
    tableString += b + '\n'
    tableString += ((len(b) + 2) * '-') + '\n'

    for i in range(n + 2):
        t = [i, Y_j[i], x[i], EV[i], ABS_ERR[i], REL_ERR[i]]
        tableString += "|{: ^8} | {: ^30} | {: ^30} | {: ^30} | {: ^30}| {: ^30}|".format(*t) + '\n'

    tableString += ((len(b) + 2) * '-') + '\n'

    return tableString


def SOLVE(A, n, GUI, l=0, deltaP=0, H=0, Nu=0, SHOW_LU=False, SHOW_table=False):
    """Solves the matrix equation Ax = b and then plots the graph of the calculated velocity at the discrete points.
        Makes a table with the y points, the Exact Velocity, and the x points along with the error estimates"""
    if GUI:
        B, EV, Y_j = MatrixGeneration.B_VExact_Yj_GENERATE(n, H, l, deltaP, Nu)
    else:
        H = float(input("H = "))  # radius
        l = float(input("L = "))  # length of channel
        deltaP = float(input("Delta P = "))  # change in pressure
        Nu = float(input("Viscosity = "))  # viscosity
        B, EV, Y_j = MatrixGeneration.B_VExact_Yj_GENERATE(n, H, l, deltaP, Nu)
    U, L = DECOMP(A, n, SHOW_LU)
    y = FORWARD_SUB(n, L, B, False)
    x = BACKWARD_SUB(y, n, U, False)
    Absolute_error = [0.0]  # velocity at the wall
    Relative_error = [0.0]  # velocity at the wall
    for i in range(1, n + 1):  # start at index 1 because x[0] = 0 and EV[0] = 0 , Absolute error is 0
        Absolute_error.append(abs(x[i] - EV[i]))
        Relative_error.append(abs(Absolute_error[i] / EV[i]))
    Absolute_error.append(0.0)
    Relative_error.append(0.0)

    table = TabPrint(n, ['k', 'Y_j points', 'Solution', 'Exact Solution', 'Absolute Error', 'Relative Error'], Y_j,
                     x, EV, Absolute_error, Relative_error)

    if SHOW_table:
        print(table)

    return table, x, Y_j


