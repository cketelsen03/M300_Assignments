%--------- Question 4 ---------% 
clear 

T = 0;

for q = 1:20

    S = 0; 
    i = 0; 

    while S <= 20
        S = S + rand; 
        i = i + 1; 
    end

    disp("It took " + i + " iterations for the sum to exceed twenty.")
    T = T + i;
end

Average = T / 20; 
    
disp("The average number of iterations is: " + Average)
    
