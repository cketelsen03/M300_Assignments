%--------- Question 1 ----------%


A = [ 2 -1 4 
    9 6 2 
    1 3 8];

B = ones(3); 

x = [3; 6; 8]; 

y = [5 10 15];

%--------- Solutions to Computation Questions ----------%

S1 = A*B; 
S2 = A*x; 
S3 = x'*B; 
%S4 = B*y; 
%S5 = x*A;
S6 = x*y;
S7 = y*x;
%S8 = x*y'; 
S9 = x.*y; 
S10 = A .*B; 

%-------------------------------------------------------%
 
disp("The following multiplies each column vector of B by the matrix A: ")
disp(S1)
disp("This multiplies the vector x by the matrix A, returning a single vector: ")
disp(S2)
disp("The transpose of x is a row vector. Each column of B is matrix-multiplied so we expect a row vector output as well: ")
disp(S3)
disp("The vector y cannot multiply into A because the number of rows in y mismatches the number of columns in A.")
disp("Similarly, the number of rows in A mismatches the number of columns in x.")
disp("Column vector x times row vector y should return a 3x3 matrix: ")
disp(S6)
disp("Conversely, y times x returns a 1x1 matrix. This is just a number: ")
disp(S7)
disp("The transpose of y mismatches its number of rows to columns of x, so x * y' DNE.")
disp("This is entrywise multiplication of x and y: ")
disp(S9)
disp("Here is a larger-scale entrywise multiplication: ")
disp(S10)

clear