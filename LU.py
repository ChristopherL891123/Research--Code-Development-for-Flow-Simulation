# The purpose of this file is to calculate the exact solutions of a matrix using LU decomposition.
# Special thanks to Dr. John Starner

Matrix = [[2, -1, 0],
          [-1, 2, -1],
          [0, -1, 2]]

B = [0.95,
     0.95,
     0.95]


def DECOMP(A, SHOW_LU):
    # Construct L and U matrices --> beware of zero division error , if error use pivoting

    global n
    n = len(A)

    # set up the L matrix
    global L  # will be needed in other parts of the program

    L = []
    for i in range(n):
        L.append([]) # create ith  row in L
        for j in range(n): # will add 0s to the ith row that was just created
            L[i].append(0)

    # set up the U matrix
    global U
    U = Matrix.copy()

    # calculate the L and the U matrices

    for j in range(0, n - 1): # j is meant to represent the previous row
        for i in range(j + 1, n): # i is meant to represent the current row
            # make U[i][k] = 0
            factor = U[j][i] / U[j][j]
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
            print(U[i], end="\n")

        print()

        print("L = ")
        for i in range(len(L)):
            for j in range(len(L[i])):
                L[i][j] = float(L[i][j])
            print(L[i], end="\n")
        print()


DECOMP(Matrix, True)

# set up y
y = [0 for i in range(n)]
y[0] = B[0]


# forward elimination
def FwdElim(y, SHOW_y):
    for i in range(0, n - 1):
        sum = 0
        for j in range(0, i):
            sum = sum + L[i][j] * y[j]
    if SHOW_y == True:
        print("y =\n", y)


FwdElim(y, True)


