import LU
import MatrixGeneration
import GUI_RESEARCH
""""Solves Ax = b """

def main():
    global n
    n = int(input("Size of matrix A to generate = "))
    A = MatrixGeneration.GENERATE(n) #Generates a matrix called Matrix
    MatrixGeneration.MatPrint(A)
    print()
    LU.SOLVE(True, True, True)

main()
