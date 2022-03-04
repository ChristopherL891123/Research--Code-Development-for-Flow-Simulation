import LU
import MatrixGeneration
import GUI_RESEARCH

Matrix = MatrixGeneration.GENERATE(5) #Generates a matrix called Matrix
print(Matrix)
B = [0.95238095,
     0.95238095,
     0.95238095]
     
MatrixGeneration.MatPrint(Matrix)
# LU.DECOMP(Matrix, True)
# LU.FORWARD_SUB(True)
# LU.BACKWARD_SUB(True)   #correct results are 1.42857143,1.9047619 ,1.42857143
