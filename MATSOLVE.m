A = [2 -1 0; -1 2 -1; 0 -1 2]
A = sym(A)
[L , U] = lu(A)
disp("L\n")
disp(L)
disp("U\n")
disp(U)
