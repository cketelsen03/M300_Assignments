# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:55:22 2022

@author: chanm
"""

import math 

def sum2(N, x = []):         # This declares the datatype of local variable "x" as an array. 
    x_totals = []
    for k in range(len(x)): 
        for i in range(N+1): 
            
            total = 0
            total += ((-1)**i)*(x[k]**(2*i))/(math.factorial(2*i))
            
            x_totals.append(total)
            
        plt.plot(x, x_totals)
        
        # return x_totals