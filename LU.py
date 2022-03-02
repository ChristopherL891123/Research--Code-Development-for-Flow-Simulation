# The purpose of this file is to calculate the exact solutions of a matrix using LU decomposition.
# Special thanks to Dr. John Starner

Matrix = [[1, 1, -1],
         [1, -2, 3],
         [2, 3, 1]]

B = [4,
     -6,
     7]

def DECOMP(A, SHOW_LU):
    # Construct L and U matrices --> beware of zero division error , if error use pivoting

    global n
    n = len(A)

    # set up the L matrix
    global L  # will be needed in other parts of the program

    # set up the L matrix
    L = []
    for i in range(n):
        L.append([]) # create ith  row in L
        for j in range(n): # will add 0s to the ith row that was just created
            L[i].append(0)

    for i in range(n):
        L[i][i] = 1
    # set up the U matrix
    global U
    U = Matrix.copy()

    # calculate the L and the U matrices

    for j in range(0, n - 1): # j is meant to represent the previous row
        for i in range(j + 1, n): # i is meant to represent the current row
            # make U[i][k] = 0
            factor = U[i][j] / U[j][j]
            L[i][j] = factor
            # adjust row i
            for k in range(0, n): # k is meant to represent the current column
                U[i][k] = U[i][k] - (factor * U[j][k])

    # print L and U
    if SHOW_LU == True:
        print("U = ")
        for i in range(len(U)):
            for j in range(len(L[i])):
                U[i][j] = float(U[i][j])
            print(U[i])


        print("L = ")
        for i in range(len(L)):
            for j in range(len(L[i])):
                L[i][j] = float(L[i][j])
            print(L[i])



# forward elimination
def FORWARD_E(SHOW_y):
    # set up y
    global y
    y = [0 for i in range(n)]
    for i in range(0,n):
        sum_row = 0 # meant to hold the sum of all the row i
        for j in range(0, i): #from first element, ends with diagonal element.
            sum_row += L[i][j] * y[j]
        y[i] = (-1 * sum_row) + B[i]
    if SHOW_y == True:
        print("y =\n", y)

# backward elimination
def BACKWARD_E(SHOW_x):
    # set up x
    global x
    x = [0 for i in range(n)]

    for i in range(-1,-n-1,-1):
        sum_row = 0  # meant to hold the sum of all the row i

        for j in range(i,0):  # from first element, ends with diagonal element.
            sum_row += U[i][j] * x[j]
        x[i] = ((-1 * sum_row) + y[i])/U[i][i]
    if SHOW_x == True:
        print("x =\n", x)


DECOMP(Matrix, True)
FORWARD_E(True)
BACKWARD_E(True)


