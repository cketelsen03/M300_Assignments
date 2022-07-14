%--------- Question 2 ---------%

A = [1 1 1; 1 2 3; 1 3 6]; 
b = [1; -5; 2]; 

X = linsolve(A, b);

disp(X)

S1 = det(A);
S2 = rank(A);

disp("The determinant of A is " + S1 +  " and it's rank is " + S2 + ".")

%--------- Alternative Solution ---------%


syms x y z

eqn1 = x + y + z == 1; 
eqn2 = x + 2*y + 3*z == -5; 
eqn3 = x + 3*y + 6*z == 2; 

sol = solve([eqn1, eqn2, eqn3], [x, y, z]); 

disp(sol.x)
disp(sol.y)
disp(sol.z)
