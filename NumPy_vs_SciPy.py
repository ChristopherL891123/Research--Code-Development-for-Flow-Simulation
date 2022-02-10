import statistics

a = open("results.txt")

b = a.readlines()

b[0] = b[0].replace('\n','')
b[0] = b[0].replace(' ','')

L1 = b[0].split(',')

counter = 0
for i in range(len(L1)):
    L1[counter] = float(L1[counter])
    counter += 1

b[1] = b[1].replace('\n','')
b[1] = b[1].replace(' ','')

L2 = b[1].split(',')

counter = 0
for i in range(len(L1)):
    L2[counter] = float(L2[counter])
    counter += 1

print(statistics.mean(L1))
print(statistics.mean(L2))
if statistics.mean(L1) < statistics.mean(L2) :
    print("SciPy is faster than NumPy   " , statistics.mean(L1) ,'vs ', statistics.mean(L2))
else: print("NumPy is faster than SciPy")

