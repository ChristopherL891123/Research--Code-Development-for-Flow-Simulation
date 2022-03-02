def RAND(size):
    R = []
    for i in range(size):
        R.append([])
        for j in range(size):
            R[i].append(random.randrange(-20,20))
    return R

a = RAND(3)
for i in range(len(a)):
    print(a[i])