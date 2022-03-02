A = [2 1 3; 4 -1 3; -2 5 5]
A = sym(A)
[L , U] = lu(A)
disp("L\n")
disp(L)
disp("U\n")
disp(U)
