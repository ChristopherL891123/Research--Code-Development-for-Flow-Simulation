import LU
import MatrixGeneration as m

""""Solves Ax = b """

def main():
    try:
        n = int(input("Size of matrix A to generate = "))
        A = m.GENERATE(n) #Generates a matrix called Matrix
        print()
        LU.SOLVE(A,n)

    except:
        print("ERROR: Size of matrix A must be a positive integer.")
# main()

def main_GUI(n):
    A = m.GENERATE(n) #Generates a matrix called Matrix
    print()
    LU.SOLVE(A,n)
