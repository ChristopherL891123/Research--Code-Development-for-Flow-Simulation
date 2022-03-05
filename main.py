import LU
import MatrixGeneration
import GUI_RESEARCH
import matplotlib as mp
""""Solves Ax = b """
def main():
    A = []
    l = int(input("Size of matrix A to generate = "))
    A = MatrixGeneration.GENERATE(l) #Generates a matrix called Matrix
    LU.SOLVE(A,True, True, True)

main()
