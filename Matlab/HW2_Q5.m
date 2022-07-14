%--------- Question 5 ---------% 
clear
hold off 

ts = linspace(0, 4*pi, 100); 
xs = 1 + cos(2*ts);
ys = -1 + 3*sin(4*ts); 

plot(xs, ys)
