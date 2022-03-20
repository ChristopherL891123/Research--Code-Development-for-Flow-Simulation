import LU
import MatrixGeneration as m
import matplotlib.pyplot as plt
""""Solves Ax = b """

def main():
    # try:
        n = 3#int(input("Size of matrix A to generate = "))
        A = m.GENERATE(n) #Generates a matrix called Matrix
        print()
        x,y_points = LU.SOLVE(A,n,GUI=False)

        plt.plot(x, y_points)
        plt.title("Graph for {i} discrete points".format(i=n + 2))
        plt.show()

    # except:
    #     print("ERROR: Size of matrix A must be a positive integer.")


def main_GUI(n):
    A = m.GENERATE(n) #Generates a matrix called Matrix
    print()
    global GUI_table
    GUI_table,x,y_points = LU.SOLVE(A,n,GUI=True)

    plt.plot(x, y_points)
    plt.title("Graph for {i} discrete points".format(i=n + 2))
    plt.show()

# main()