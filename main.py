import LU
import MatrixGeneration as m
import matplotlib.pyplot as plt
""""Solves Ax = b """

def main():
    try:

       x = 'y' #meant to be used as a switch that will end the program if the user does not want to make more plots

       while x == 'y':
        n = int(input("Size of matrix A to generate = "))
        A = m.GENERATE(n) #Generates a matrix called Matrix

        x,y_points = LU.SOLVE(A, n, False)

        plt.margins(x=0, y=0, tight=True)
        plt.plot(x, y_points)
        plt.title("Graph for {i} discrete points".format(i=n + 2))
        plt.show()

        x = input("Continue plotting? y/n : ")
        if x == 'y':
            continue

        else:
            print("Terminating process...")
            break

    except:
        print("ERROR: Size of matrix A must be a positive integer.")
        import traceback as t
        t.print_exc()


main()