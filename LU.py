# The purpose of this file is to calculate the exact solutions of a matrix using LU decomposition.
# Special thanks to Dr. John Starner
import tkinter

import prettytable.prettytable as p
import MatrixGeneration


def DECOMP(A, n, SHOW_LU):
    """Decomposes the A matrix into LU, using Gaussian elimination. Returns L and U matrices"""

    # set up the L matrix
    L = []
    for i in range(n):
        L.append([])  # create ith  row in L
        for j in range(n):  # will add 0s to the ith row that was just created
            L[i].append(0)

    for i in range(n):
        L[i][i] = 1
    # set up the U matrix
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

    # zero velocity at the walls
    x.insert(0, 0.0)
    x.append(0)

    if SHOW_x:
        print("x =\n", x)

    return x


def SOLVE(A, n, GUI, SHOW_LU=False, SHOW_x=False, SHOW_Yj=False,SHOW_errors=False,l=0,deltaP=0,H=0,Nu=0):
    """Solves the matrix equation Ax = b and then plots the graph of the calculated velocity at the discrete points.
        Makes a table with the y points, the Exact Velocity, and the x points along with the error estimates """

    # if the parameter GUI is true, it will take the collected values from the textboxes and used them to generate the b vector, the exct velocty and the Y_j points
    # else it asks the user for the input, this is for the console version of the program.
    if GUI:
      B, EV, Y_j = MatrixGeneration.B_VExact_Yj_GENERATE(n, H, l, deltaP, Nu)
    else:
      H = float(input("H = "))  # radius
      l = float(input("L = "))  # length of channel
      deltaP = float(input("Delta P = "))  # change in pressure
      Nu = float(input("Viscosity = "))  # viscosity
      B, EV, Y_j = MatrixGeneration.B_VExact_Yj_GENERATE(n, H, l, deltaP, Nu)
      # y_points.insert(0, -H)

    U, L = DECOMP(A, n, SHOW_LU)
    y = FORWARD_SUB(n, L, B, False)
    x = BACKWARD_SUB(y, n, U, False)


    Absolute_error = [0.0]  #velocity at the wall
    Relative_error = [0.0]  # velocity at the wall

    for i in range(1, n+1): # start at index 1 because x[0] = 0 and EV[0] = 0 , Absolute error is 0
            Absolute_error.append(abs(x[i] - EV[i]))
            Relative_error.append(abs(Absolute_error[i] / EV[i]))

    Absolute_error.append(0.0)
    Relative_error.append(0.0)

    if GUI:
        GUI_table = TabPrint(n,['k', 'Y_j points', 'Solution', 'Exact Solution', 'Absolute Error', 'Relative Error'],Y_j,x,EV,Absolute_error,Relative_error,2)
        return GUI_table, x, Y_j

    if SHOW_Yj:
         print("Y_j: ",Y_j)

    if SHOW_x:
        print("x: ",x)

    if SHOW_errors:
         print("Absolute error: ",Absolute_error)
         print("Relative error: ",Relative_error)


    print(TabPrint(n,['k', 'Y_j points', 'Solution', 'Exact Solution', 'Absolute Error', 'Relative Error'],Y_j,x,EV,Absolute_error,Relative_error,1))

    return x, Y_j


def TabPrint(n,header, Y_j,x,EV,ABS_ERR,REL_ERR, option):
    ''''prints the table with the values, option == 1 means that '''

    tableString = ""

    b = "|{: ^8} | {: ^30} | {: ^30} | {: ^30} | {: ^30}|{: ^30}|".format(*header)
    tableString += b + '\n'
    tableString += ((len(b)+2) * '-') + '\n'

    for i in range(n+2):
        t = [i, Y_j[i], x[i], EV[i], ABS_ERR[i], REL_ERR[i]]
        tableString += "|{: ^8} | {: ^30} | {: ^30} | {: ^30} | {: ^30}| {: ^30}|".format(*t) +'\n'

    tableString += ((len(b)+2) * '-') + '\n'

    if option == 1:
        print(tableString)
        return

    if option == 2:
        return tableString


