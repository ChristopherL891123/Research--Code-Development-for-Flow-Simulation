# Special thanks to Dr. Charles Thangaraj

# Matrix generation algorithm
def GENERATE(n):
    """Generates a NxN matrix composed of 2s in the diagonal line
    and -1s in the lower and upper diagonal"""

    Matrix = []
    # set up the matrix
    for a in range(n):
        Matrix.append([])
        for b in range(n):
            Matrix[a].append(0)

    # insert values
    i = 0
    for j in range(0, n):
        Matrix[j][j] = 2
        if i == n-1:
            break
        i = j + 1
        Matrix[j][i] = -1
        Matrix[i][j] = -1

    return Matrix

def MatPrint(matrix, n):
    """Prints matrix row by row"""
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

def B_VExact_Yj_GENERATE(n, H, L, Delta_P, Nu):
    """Generates b vector, Yj points, and Exact Velocity for each Yj point"""
    Delta_Y = (2 * H) / (n + 1)
    V_max = (Delta_P * H ** 2) / (2 * Nu * L)
    F_j = (Delta_Y ** 2 * (2 * V_max)) / (H ** 2)
    B = [F_j for i in range(n)]
    EV = []
    Y_j_LIST = []
    for i in range(0, n + 2):
        Y_j = -H + i * Delta_Y
        Y_j_LIST.append(Y_j)
        EV.append(V_max * (1 - (Y_j / H) ** 2))

    return B, EV, Y_j_LIST