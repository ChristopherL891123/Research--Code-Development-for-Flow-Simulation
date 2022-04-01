import LU
import MatrixGeneration as m
import matplotlib.pyplot as plt
""""Solves Ax = b """

def main():
    try:
        n = int(input("Size of matrix A to generate = "))
        A = m.GENERATE(n) #Generates a matrix called Matrix

        x,y_points = LU.SOLVE(A, n, False)

        plt.plot(x, y_points)
        plt.title("Graph for {i} discrete points".format(i=n + 2))
        plt.show()

    except:
        print("ERROR: Size of matrix A must be a positive integer.")
        import traceback as t
        t.print_exc()


main()