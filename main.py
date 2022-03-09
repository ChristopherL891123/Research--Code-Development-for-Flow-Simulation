import LU
import MatrixGeneration
import GUI_RESEARCH
import matplotlib as mp
""""Solves Ax = b """

def main():
    l = int(input("Size of matrix A to generate = "))
    A = MatrixGeneration.GENERATE(l) #Generates a matrix called Matrix
    MatrixGeneration.MatPrint(A)
    print()
    LU.SOLVE(True, True, True)

main()
