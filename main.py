import LU
import MatrixGeneration as m
import matplotlib.pyplot as plt
""""Solves Ax = b """

def main():
    try:
        n = 3#int(input("Size of matrix A to generate = "))
        A = m.GENERATE(n) #Generates a matrix called Matrix
        print()
        x,y_points = LU.SOLVE(A,n,GUI=False,SHOW_LU=True,SHOW_X=True,SHOW_errors=True,SHOW_Ypoints=True,SHOW_Y_Vector=True)

        plt.plot(x, y_points)
        plt.title("Graph for {i} discrete points".format(i=n + 2))
        plt.show()

    except:
        print("ERROR: Size of matrix A must be a positive integer.")

main()