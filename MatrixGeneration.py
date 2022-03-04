def GENERATE(n):
    #set up the Matrix
    Matrix  = []
    difference = n-1
    for i in range(n):
        Matrix.append([])
        for j in range(n):
            Matrix[i].append(0)

    for j in range(0,n):#j=0
        Matrix[j][j] = 2
        for i in range(j+1,n):#n=5 --> 1-->5
            Matrix[j][i] = -1
            Matrix[i][j] = -1
            break


    print("A= \n")
    for i in range(n):
        print(Matrix[i])

GENERATE(5)
