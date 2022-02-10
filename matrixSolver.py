import statistics
import scipy.linalg as sc
import numpy as np
import time

StartTime = time.perf_counter()

l = []

for i in range(100):
    a = open('matrix.txt')

    b = a.readlines()

    for i in range(len(b)):
        b[i] = b[i].replace("\n",'')
        b[i] = b[i].replace(' ', '')


    for z in range(len(b)):
        b[z] = list(b[z]) #turn contents of b[i] into a list

    for i in range(len(b)):
        for j in range(100):
            b[i][j] = int(b[i][j])

    a.close()
    #----------------------------------------------------------------#
    a = open('determinant.txt')

    c = a.readlines()

    for i in range(len(c)):
        c[i] = c[i].replace("\n",'')
        c[i] = c[i].replace(' ', '')


    for z in range(len(c)):
        c[z] = list(c[z]) #turn contents of b[i] into a list

    for i in range(len(c)):
        for j in range(1):
            c[i][j] = int(c[i][j])

    a.close()



    Matrix = np.array(b)
    DeterminantMatrix = np.array(c)

    temp = []
    solutionSCI = sc.solve(Matrix,DeterminantMatrix)
    temp.append(solutionSCI)
    # print(" WITH SCI" , solutionSCI)

    EndTime = time.perf_counter()

    FinalTime = EndTime-StartTime
    l.append(FinalTime)

    a.close()

print("mean time is ", np.mean(l))
print(l)