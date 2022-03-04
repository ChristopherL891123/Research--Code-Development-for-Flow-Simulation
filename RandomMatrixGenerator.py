import random

"""RAND(size) Makes a random square matrix of a specified size and specified range, range should be a positive number"""

def RAND(size, Range):
    R = []
    for i in range(size):
        R.append([])
        for j in range(size):
            R[i].append(random.randrange(-Range,Range))
        R[i][i] = 2
    return R

#test
a = RAND(3,4)
for i in range(len(a)):
    print(a[i])

def diagonalCheck(A , num_to_check):
    check = 0
    for i in range(len(a)):
        if A[i][i] == num_to_check:
            check += 1
    if check == len(A):
        print("all diagonal elements are ",num_to_check)
    else: print("not all diagonal elements are ",num_to_check)

diagonalCheck(a,2)
