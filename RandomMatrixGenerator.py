import random

"""RAND(size) Makes a random square matrix of a specified size"""

def RAND(size):
    R = []
    for i in range(size):
        R.append([])
        for j in range(size):
            R[i].append(random.randrange(-20,20))
        R[i][i] = 2
    return R

#test
a = RAND(9)
for i in range(len(a)):
    print(a[i])

def diagonalCheck(A):
    check = 0
    for i in range(len(a)):
        if A[i][i] == 2:
            check += 1
    if check == len(A):
        print("all diagonal elements are two")
    else: print("not all diagonal elements are two")

diagonalCheck(a)