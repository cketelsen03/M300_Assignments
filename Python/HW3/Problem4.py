# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:41:32 2022

@author: chanm
"""

import numpy as np
import matplotlib.pyplot as plt


def midpoint(f, a=0, b=1, N=100):
    
    S = 0
    
    I = np.zeros([N])
    
    dx = (b-a)/(N)
    
    xs = np.linspace(a, b, N)
    ys = f(xs)
    
    for i in range(0, N): 
        
        x_i = ((a + dx*i) + (b + dx*(i + 1)))/2
        
        dy = f(x_i)*dx
        
        S += dy 
        
        I[i] = S
        
    
    plt.plot(xs, ys)
    plt.plot(xs, I)

























