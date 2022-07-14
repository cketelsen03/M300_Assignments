%--------- Question 3 ----------%

clear

A = [1 1 ; 1 2 ; 1 3]; 
b = [1; 5; 10]; 

sol = linsolve(A, b); 

S1 = A*sol; 

disp(sol)
disp(S1)
disp(b)

% The vector x does not reproduce b becase the equation represents an
% inconsistent system.% 

% ---- bonus question: plot the inconsistent system ----% 
clear 

xs = linspace(-10, 10, 100);
ys1 = 1 - xs; 
ys2 = (1/2)*(5 - xs);
ys3 = (1/3)*(10 - xs);

hold on

plot(xs, ys1)

plot(xs, ys2)

plot(xs, ys3)


