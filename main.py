import LU
import MatrixGeneration
import GUI_RESEARCH
""""Solves Ax = b """

def main():
    try:
        n = int(input("Size of matrix A to generate = "))
        A = MatrixGeneration.GENERATE(n) #Generates a matrix called Matrix
        print()
        LU.SOLVE(A,n)
    except:
        print("ERROR: Size of matrix A must be a positive integer.")
main()
