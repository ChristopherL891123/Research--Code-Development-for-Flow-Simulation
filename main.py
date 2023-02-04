# Christopher Lama

import LU
import MatrixGeneration as m
import matplotlib.pyplot as plt

# console executable
def main():

    """
   Description:
       Console executable that gathers the dimensions of the matrix form the user and solves for the matrix. Then graphs the results using matplotlib.

   Parameters:
       none

   Returns:
       none
   """

    try:

        user_input = 'y'  # meant to be used as a switch that will end the program if the user does not want to make more plots

        while user_input == 'y':
            n = int(input("Size of matrix A to generate = "))
            A = m.GENERATE(n)  # Generates the A matrix

            table, x, y_points = LU.SOLVE(A, n, False, SHOW_table=True) # generates x,y points and the table

            # set up the graph
            plt.margins(x=0, y=0)
            plt.plot(x, y_points)
            plt.title("Graph for {i} discrete points".format(i=n + 2))
            plt.xlabel("Velocity", fontsize=12)
            plt.ylabel("y", rotation="horizontal", fontsize=12)
            plt.show()

            user_input = input("Continue plotting? y/n : ")

    except:
        print("ERROR: values provided caused an error")
        import traceback as t
        t.print_exc()


main()