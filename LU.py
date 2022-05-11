# The purpose of this file is to calculate the exact solutions of a matrix using LU decomposition.
# Special thanks to Dr. John Starner

import MatrixGeneration


# Decomposition algorithm
def DECOMP(A, n, SHOW_LU):
    """Decomposes the A matrix in LU matrices. """
    # set up U and L
    L = []
    for i in range(n):
        L.append([])
        for j in range(n):
            L[i].append(0)
    for i in range(n):
        L[i][i] = 1
    U = A.copy()

    for j in range(0, n - 1):  # j is column and represents the diagonal element
        for i in range(j + 1, n):  # i is row
            factor = U[i][j] / U[j][j]
            L[i][j] = factor
            # adjust the row
            for k in range(0, n):
                U[i][k] = U[i][k] - (factor * U[j][k])

    # print the matrices
    if SHOW_LU:
        print("U = ")
        MatrixGeneration.MatPrint(U, n)
        print("L = ")
        MatrixGeneration.MatPrint(L, n)

    return U, L


# forward substitution algorithm
def FORWARD_SUB(n, L, B, SHOW_y):
    """Performs forward substitution on the L matrix using the b vector to find the y vector"""
    # set up y
    y = []
    for i in range(n):
        y.append(0)

    for i in range(0, n):  # i is the row
        sum_row = 0
        for j in range(0, i):  # j is the column; starts from index 0 and ends the index before diagonal element
            sum_row += L[i][j] * y[j]  # get sum of elements from index 0 to element before the diagonal line
        y[i] = (-1 * sum_row) + B[i]  # calcualte the unknown value

    # print y vector
    if SHOW_y:
        print("y = ", y)

    return y


# backward substitution algorithm
def BACKWARD_SUB(y, n, U, SHOW_x):
    """Performs backward substitution on the U matrix using the y vector to find the x vector"""

    x = [0 for i in range(n + 1)]  # n+1 because of boundary conditions: velocity is zero at the walls

    for i in range(-1, -n - 1, -1):  # start from last row
        sum_row = 0
        for j in range(i, 0):  # start from diagonal element and move to last element of the row
            sum_row += U[i][j] * x[j]  # get sum of row
        x[i] = ((-1 * sum_row) + y[i]) / U[i][i]  # calculate the unknown x value for the row
    x.append(0)  # boundary conditions

    # print x
    if SHOW_x:
        MatrixGeneration.MatPrint(y, n)
    return x


def TabPrint(n, header, Y_j, x, EV, ABS_ERR, REL_ERR):
    """Returns the table with the values. Adapted from
    https://www.codegrepper.com/code-examples/python/how+to+create+table+format+python+console+output+without+library"""

    tableString = ""  # used to store the table

    b = "|{: ^8} | {: ^30} | {: ^30} | {: ^30} | {: ^30}|{: ^30}|".format(*header)  # header
    tableString += b + '\n'  # put newline
    tableString += ((len(b) + 2) * '-') + '\n'  # make division between header and body of table

    # put contents of the line into chart
    for i in range(n + 2):
        tableString += "|{: ^8} | {: ^30} | {: ^30} | {: ^30} | {: ^30}| {: ^30}|". \
                           format(i, Y_j[i], x[i], EV[i], ABS_ERR[i], REL_ERR[i]) + '\n'

    tableString += ((len(b) + 2) * '-') + '\n'  # close the table

    return tableString


def SOLVE(A, n, GUI, l=0, deltaP=0, H=0, Nu=0, SHOW_LU=False, SHOW_table=False):
    """Solves the matrix equation Ax = b and then plots the graph of the calculated velocity at the discrete points.
        Makes a table with the y points, the Exact Velocity, and the x points along with the error estimates"""

    if GUI:  # The GUI collects the user input and calls the SOLVE function using that data.
        B, EV, Y_j = MatrixGeneration.B_VExact_Yj_GENERATE(n, H, l, deltaP, Nu)  # uses collected data as values

    else:
        H = float(input("H = "))  # radius
        l = float(input("L = "))  # length of channel
        deltaP = float(input("Delta P = "))  # change in pressure
        Nu = float(input("Viscosity = "))  # viscosity
        B, EV, Y_j = MatrixGeneration.B_VExact_Yj_GENERATE(n, H, l, deltaP, Nu) # generate

    U, L = DECOMP(A, n, SHOW_LU) # decompose
    y = FORWARD_SUB(n, L, B, False) # forward elimination
    x = BACKWARD_SUB(y, n, U, False) # backward elimination

    Absolute_error = [0.0]  # velocity at the wall
    Relative_error = [0.0]  # velocity at the wall

    for i in range(1, n + 1):  # start at index 1 because x[0] = 0 and EV[0] = 0 , Absolute error is 0
        Absolute_error.append(abs(x[i] - EV[i]))
        Relative_error.append(abs(Absolute_error[i] / EV[i]))
    Absolute_error.append(0.0) # boundary conditions
    Relative_error.append(0.0)

    # make table
    table = TabPrint(n, ['k', 'Y_j points', 'Solution', 'Exact Solution', 'Absolute Error', 'Relative Error'], Y_j,
                     x, EV, Absolute_error, Relative_error)

    if SHOW_table:
        print(table)

    return table, x, Y_j
