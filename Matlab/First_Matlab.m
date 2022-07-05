disp("Basic vector arithmetic:")
% To define some vectors, use square braces:

A = [1, 3, 5, 7];
B = [2, 4, 6, 8];
C = [1; 1; 1; 1];

% The space and/or comma is used to change columns, and the semicolon is
% used to chage rows. 

A*C; 

disp("A + B = ")
disp(A + B)

% Now try making matrices this way:

A = [1 2 ; 3 4];
B = [5 6 ; 7 8];
C = [1 2
    3 4];
D = [5 6
    7 8];

