import LU
import MatrixGeneration
import GUI_RESEARCH
import matplotlib as mp
""""Solves Ax = b """

def main():
    n = int(input("Size of matrix A to generate = "))
    A = MatrixGeneration.GENERATE(n) #Generates a matrix called Matrix
    MatrixGeneration.MatPrint(A,n)
    print()
    LU.SOLVE(A,n,True, True, True)

main()
