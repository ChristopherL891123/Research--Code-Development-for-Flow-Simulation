# The purpose of this file is to calculate the exact solutions of a matrix using LU decomposition.

Matrix = [[2, -1, 0],
          [-1, 2, -1],
          [0, -1, 2]]

B = [0.95,
     0.95,
     0.95]


def DECOMP(A , SHOW_LU):

    #Construct L and U matrices --> beware of zero division error , if error use pivoting

    global n
    n = len(A)

    #set up the L matrix
    global L #will be needed in other parts of the program
    L =[ [0,0,0] for i in range(n)]

    for i in range(0, n-1):
        L[i][i] = 1

    #set up the U matrix
    global U
    U = Matrix.copy()

    # calculate the L and the U matrices

    for i in range(0,n-2):
        for j in range(i+1,n-1):
            factor = U[j][i] / U[i][i]
            L[j][i] = factor

            for k in range(0,n-1):
                U[j][k] = U[j][k] - (U[i][k]*factor)

    #print L and U
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

DECOMP(Matrix,True)

#set up y
y = [0 for i in range(n)]
y[0] = B[0]


#forward elimination
def FwdElim(y , SHOW_y):
    for i in range(0, n - 1):
        sum = 0
        for j in range(0, i):
            sum = sum + L[i][j] * y[j]
    if SHOW_y == True:
        print("y =","\n",y)

FwdElim(y,True)