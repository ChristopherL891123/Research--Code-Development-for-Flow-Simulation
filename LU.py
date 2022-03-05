# The purpose of this file is to calculate the exact solutions of a matrix using LU decomposition.
# Special thanks to Dr. John Starner
import matplotlib.pyplot as plt
import MatrixGeneration

def DECOMP(A,n, SHOW_LU):
    # Construct L and U matrices
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
    U = A.copy()

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
def FORWARD_SUB(n,SHOW_y):

    global B

    # set up y
    y = []
    for i in range(n):
        y.append(0)
    for i in range(0,n):
        sum_row = 0 # meant to hold the sum of all the row i
        for j in range(0, i): #from first element, ends with diagonal element.
            sum_row += L[i][j] * y[j]
        y[i] = (-1 * sum_row) + B[i]
    if SHOW_y == True:
        print("y =\n", y)
    return y

# backward elimination
def BACKWARD_SUB(y,n,SHOW_x):
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
    return x

def SOLVE(A,SHOW_LU,SHOW_Y,SHOW_X):
    import matplotlib.pyplot as pt
    global B
    global n

    n = len(A)

    H = int(float(input("H = ")))
    L = int(float(input("L = ")))
    deltaP = int(float(input("Delta P = ")))
    Nu = int(float(input("Viscosity = ")))
    print("\n***GENERATING***\n")
    B,VE_points,y_points = MatrixGeneration.B_VExact_Yj_GENERATE(n,H,L,deltaP,Nu)

    y_points.insert(0,y_points[0]-0.5) # add one more Yj point to the list, for graphing purposes
    y_points.append(y_points[-1]+0.5)


    DECOMP(A,n,SHOW_LU)
    y = FORWARD_SUB(n,SHOW_Y)
    x = BACKWARD_SUB(y,n,SHOW_X)

    x.insert(0,0)
    x.append(0)
    print("x is")
    print(x)
    print("y is")
    print(y_points)


    plt.plot(x,y_points)
    plt.show()



