import LU
import MatrixGeneration
import GUI_RESEARCH

""""Solves Ax = b """
A = []
A = MatrixGeneration.GENERATE(5) #Generates a matrix called Matrix



LU.SOLVE(A,True, True, True)


