import LU
import MatrixGeneration
import GUI_RESEARCH

""""Solves Ax = b """
def main():
     Matrix = []
     Matrix = MatrixGeneration.GENERATE(5) #Generates a matrix called Matrix


     # b matrix is calculated in LU.FORWARD_SUB

     print(Matrix)


     MatrixGeneration.MatPrint(Matrix)

     LU.SOLVE(Matrix,True, True, True)


main()
