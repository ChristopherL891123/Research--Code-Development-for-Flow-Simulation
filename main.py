import LU
import MatrixGeneration
import GUI_RESEARCH
""""Solves Ax = b """

def main():
    n = int(input("Size of matrix A to generate = "))
    A = MatrixGeneration.GENERATE(n) #Generates a matrix called Matrix
    print()
    LU.SOLVE(A,n)

main()
