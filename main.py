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
#
# local_taxes_ca = 0
# local_taxes_tx = 0
# local_taxes_ny = 0
# net_salary = 0
# g_salary = int(input("enter your gross salary: "))
# state = input("enter your state: ")
# # in the space below write your code
#
# if g_salary >= 1000000000:
# 	net_salary = g_salary // 2
# if state == "CA" or state == "California" or state == "CALIFORNIA":
# 	net_salary = g_salary*(1-local_taxes_ca)
# if state == "TX" or state == "Texas" or state == "TEXAS":
# 	net_salary = g_salary*(1-local_taxes_tx)
# if state == "NY" or state == "New York" or state == "NEW YORK":
# 	net_salary = g_salary*(1-local_taxes_ny)
#
# if (state != "NY" and state != "New York" and state != "NEW YORK") and (state != "CA" and state != "California" and state != "CALIFORNIA") and (state != "TX" and state != "Texas" and state != "TEXAS"):
# 	print("state unknown")
#
# print(net_salary)


#Q2: when count is 20, the program won't enter into the while. The while loop acts like a mix between
# the for loop and the if condition: it loops through a block of code if and as long as its condition is true.
# count = 20
# c = 0
# while (count < 20):
# 	count += 20
# 	c += 1
# print(c)
