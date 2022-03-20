# The purpose of this file is to calculate the exact solutions of a matrix using LU decomposition.
# Special thanks to Dr. John Starner

import matplotlib.pyplot as plt
import prettytable as p
import MatrixGeneration


def DECOMP(A, n, SHOW_LU):
    """Decomposes the A matrix into LU, using Gaussian elimination. Returns both L and U matrices"""

    # set up the L matrix
    L = []
    for i in range(n):
        L.append([])  # create ith  row in L
        for j in range(n):  # will add 0s to the ith row that was just created
            L[i].append(0)

    for i in range(n):
        L[i][i] = 1
    # set up the U matrix
    global U
    U = A.copy()

    # calculate the L and the U matrices

    for j in range(0, n - 1):  # j is meant to represent the previous row
        for i in range(j + 1, n):  # i is meant to represent the current row
            # make U[i][k] = 0
            factor = U[i][j] / U[j][j]
            L[i][j] = factor
            # adjust row i
            for k in range(0, n):  # k is meant to represent the current column
                U[i][k] = U[i][k] - (factor * U[j][k])

    # print L and U
    if SHOW_LU:
        print("U = ")
        MatrixGeneration.MatPrint(U, n)
        print("L = ")
        MatrixGeneration.MatPrint(L, n)

    return U, L


# forward elimination
def FORWARD_SUB(n, L, B, SHOW_y):
    """""Performs forward substitution using the L matrix and the b vector whose value is known due to pressure difference.
         Returns y vector"""

    # set up y
    y = []
    for i in range(n):
        y.append(0)
    for i in range(0, n):
        sum_row = 0  # meant to hold the sum of all the row i
        for j in range(0, i):  # from first element, ends with diagonal element.
            sum_row += L[i][j] * y[j]
        y[i] = (-1 * sum_row) + B[i]
    if SHOW_y:
        print("y =\n", y)
    return y


# backward elimination
def BACKWARD_SUB(y, n, U, SHOW_x):
    """Performs backward substitution using the calculated U matrix and the calculated Y vector. Returns x vector"""
    # set up x
    x = [0 for i in range(n)]

    for i in range(-1, -n - 1, -1):
        sum_row = 0  # meant to hold the sum of all the row i

        for j in range(i, 0):
            sum_row += U[i][j] * x[j]
        x[i] = ((-1 * sum_row) + y[i]) / U[i][i]
    if SHOW_x:
        print("x =\n", x)

    return x


def SOLVE(A, n, GUI,SHOW_LU=False, SHOW_Y_Vector=False, SHOW_X=False, SHOW_Ypoints=False):
    """Solves the matrix equation Ax = b and then plots the graph of the calculated velocity at the discrete points.
        Makes a table with the y points, the Exact Velocity, and the x points along with the error estimates """

    H = 1  # float(input("H = "))
    L = 5  # float(input("L = "))
    deltaP = 8.0  # float(input("Delta P = "))
    Nu = 0.42  # float(input("Viscosity = "))
    B, EV_points, y_points = MatrixGeneration.B_VExact_Yj_GENERATE(n, H, L, deltaP, Nu)

    y_points.insert(0, -H)
    y_points.append(H)

    U, L = DECOMP(A, n, SHOW_LU)
    y = FORWARD_SUB(n, L, B, SHOW_Y_Vector)
    x = BACKWARD_SUB(y, n, U, SHOW_X)

    x.insert(0, 0.0)
    x.append(0.0)

    if SHOW_Ypoints:
        print("x is")
        print(x)
        print("y points are is")
        print(y_points)

    Absolute_error = [0.0]
    Relative_error = [0.0]

    for i in range(1, n + 2):
        try:
            Absolute_error.append(abs( x[i] - EV_points[i]))
            Relative_error.append(abs(Absolute_error[i] / EV_points[i]))

        except ZeroDivisionError:
            Absolute_error.append(0.0)
            Relative_error.append(0.0)

    Absolute_error.append(0.0)
    Relative_error.append(0.0)

    # update with absolute and estimate error column
    table = p.PrettyTable()
    table.field_names = ['k', 'Y_j points', 'Solution', 'Exact Solution', 'Absolute Error', 'Relative Error']
    for i in range(n + 2):
        table.add_row([i, y_points[i], x[i], EV_points[i], Absolute_error[i], Relative_error[i]])

    table.set_style(15)


    if GUI:
        GUI_table = table.get_string()
        return GUI_table,x,y_points

    print(table)
    return x,y_points

def TabPrint(n, y, x, EV):
    print("|Y_j\t|    Solution   \t|Exact Solution   |")
    for i in range(n + 2):
        print('|', 45 * '-', end='|\n', sep='')
        print("|%.4f|%.16f|%.16f|" % (y[i], x[i], EV[i]))
