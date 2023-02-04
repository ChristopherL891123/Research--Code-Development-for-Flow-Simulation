# Christopher Lama
# Special thanks to Dr. John Starner

import MatrixGeneration


# Decomposition algorithm
def DECOMP(A, n, SHOW_LU):
    """
    Description:
        Decomposes the A matrix into L and U matrices.

    Parameters:
        A: list
            The generated matrix (the system of linear equations)

        n: int
            Size of matrix; user-given in main() function as well as in the Graphical User Interface.

        SHOW_LU: bool
            Determines whether the resulting L and U matrices will be printed out.

    Returns:
        U: list
            The U matrix

        L: list
            The L matrix
    """

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
    """
    Description:
        Performs forward substitution on the L matrix using the b vector to find the y vector.

    Parameters:
        L: list
            The calculated L matrix.

        n: int
            Size of matrix; user-given in main() function as well as in the Graphical User Interface.

        B: list
            B is the known right-hand side of the original matrix equation.

        SHOW_y: bool
            Detemrines whether the calculated y vector is to be displayed.

    Returns:
        y: list
            The y vector
        """


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
    """
    Description:
            Performs backward substitution on the U matrix using the y vector to find the x vector

    Parameters:
        U: list
            The calculated U matrix.

        n: int
            Size of matrix; user-given in main() function as well as in the Graphical User Interface.

        y: list
            y vector calculated through FORWARD_SUB()

        SHOW_x: bool
            Detemrines whether the calculated x vector is to be displayed.

    Returns:
        x: list
            The x vector
    """



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

    """
    Description:
        Returns the table with the calculated X and Y points, the solution, exact solution, and absolute and relative errors.
        Adapted from https://www.codegrepper.com/code-examples/python/how+to+create+table+format+python+console+output+without+library

    Parameters:
        Header: list
            Header of the table.
            ['k', 'Y_j points', 'Solution', 'Exact Solution', 'Absolute Error', 'Relative Error']

        Y_j: list
            Calculated list of discrete points on the channel. Calculated through B_VExact_Yj_GENERATE() function.

        EV: list

            Calculated list of the exact velocity at a particular discrete point. Calculated through B_VExact_Yj_GENERATE() function in MatrixGeneration.py.

        ABS_ERR: list

            Calculated list of the absolute error (difference between numerical solution and exact solution).
            Calculated through SOLVE() function in LU.py

        REL_ERR: list

            Calculated list of the relative error (difference between absolute error and exact solution).
            Calculated through SOLVE() function in LU.py

        n: int
            Size of matrix; user-given in main() function as well as in the Graphical User Interface in GUI.py

        x: list
            x vector calculated through BACKWARD_SUB() function in LU.py


    Returns:
        y: list
            The y vector
        """

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
    """
    Description:
        Solves the system of linear equations and graphs the results. Used both in main.py and GUI.py

    Parameters:

        A: list
            The generated matrix (the system of linear equations).

        n: int
            Size of matrix; user-given in main() function as well as in the Graphical User Interface.

        GUI: bool
            determined whether the SOLVE() function is meant to be used for a GUI or not.

        l: int
            Length of the channel

        deltaP: int
            Change in pressure.

        H: int
            Radius of the channel.

        Nu: int
            Viscosity of the blood.

        SHOW_LU: bool
            Determines whether the L and U matrices should be displayed.

        SHOW_table: bool
            Determines whether the table should be displayed.

        SHOW_LU: bool
            Determines whether the resulting L and U matrices will be printed out.
            """
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
    Absolute_error = [0.0]
    Relative_error = [0.0]
    for i in range(1, n + 1):
        Absolute_error.append(abs(x[i] - EV[i]))
        Relative_error.append(abs(Absolute_error[i] / EV[i]))
    Absolute_error.append(0.0)
    Relative_error.append(0.0)
    # make table
    table = TabPrint(n, ['k', 'Y_j points', 'Solution', 'Exact Solution',
                         'Absolute Error', 'Relative Error'], Y_j,
                     x, EV, Absolute_error, Relative_error)
    if SHOW_table:
        print(table)
    return table, x, Y_j
