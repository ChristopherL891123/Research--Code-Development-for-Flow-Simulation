# The purpose of this file is to calculate the discrete points for the research.
# Research material provided by Dr. Arati Nanda Pati and Dr. Kehinde O. Ladipo
# Code developed by Christopher Ian Lama


import numpy as np
from scipy import linalg as ln
from tabulate import tabulate as tb
import time


# if the matrix size changes, update the size of the dependent matrix, the first for loop, the size of the table.

# --> Calculations <--



H = 1
L = 5
Delta_P = 8.0
Viscosity = 0.42
Delta_Y = (2 * H) / 4
V_max = (8 * 1 ** 2) / (2 * 0.42 * 5)

F_j = (2 * ((8 * 1) / (2 * 0.42 * 5)))
F_j *= 0.5 ** 2

V_exact_LIST = []
Y_j_LIST = []

# calculate Y_j and V_exact and append it to their respective lists for data processing
for i in range(5):
    Y_j = (-H + i * Delta_Y)
    Y_j_LIST.append(Y_j)
    V_exact_LIST.append(V_max * (1 - (Y_j / H) ** 2))

Y_j_LIST.insert(0, 'blank')  # for adding this to the table( 'blank' will not be displayed on the table )

# create matrix
Matrix = np.array([[2, -1, 0],
                   [-1, 2, -1],
                   [0, -1, 2]])

print("A Matrix: \n", Matrix)

# create dependent variable matrix
Dependent_Matrix = np.array([[F_j], [F_j], [F_j]])

print("\n B Matrix: \n", Dependent_Matrix)

# solve the matrix using the solve function in Numpy library, this function returns another matrix(ndarray)
# where the solutions are stored. Does not show zeros.
#result_withNumPy = np.linalg.solve(Matrix, Dependent_Matrix)

# verified my answer using SciPy library
result_withNumPy = np.linalg.solve(Matrix , Dependent_Matrix)


# --> Display results <--


#create table of size 6 rows, 3 columns. 1 row is for the header and 5 rows are for the results.




Table = [[0.0, 0.0, 0.0] for i in range(6)]


# add the values of Y_j to the table
counter1 = 0  # used to reference the index of Y_j_LIST
for nested_lists in Table:
    nested_lists[0] = Y_j_LIST[counter1]
    counter1 += 1

# add values of solutions to table
counter2 = 0
counter3 = 0  # since values of row 2 and last row will always be 0, we need to skip those rows. This is the purpose of this variable
for nested_lists2 in Table:
    counter3 += 1
    if counter3 <= 2:
        continue
    nested_lists2[1] = result_withNumPy[counter2][0]
    counter2 += 1

    if counter2 == len(result_withNumPy):
        break

# add values of exact velocities to table
counter4 = 0
counter5 = 0  # since values of row 2 and last row will always be 0, we need to skip those rows. This is the purpose of this variable
for nested_lists3 in Table:
    counter5 += 1
    if counter5 <= 1:
        continue
    nested_lists3[2] = V_exact_LIST[counter4]
    counter4 += 1

    if counter4 == len(V_exact_LIST):
        break

# assign values for the headers (first row)
Table[0][0] = "Y_j"
Table[0][1] = "Solution"
Table[0][2] = "V Exact"




print("Table: \n", tb(Table, tablefmt='fancy_grid'),sep='')
#NOTE: use showindex=True to count how many rows there are in the table

del Y_j_LIST[0]
import matplotlib.pyplot as pt

pt.plot(V_exact_LIST,Y_j_LIST)
pt.show()


