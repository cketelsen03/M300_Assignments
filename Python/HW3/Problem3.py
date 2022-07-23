# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 10:31:08 2022

@author: chanm
"""

import numpy as np
import matplotlib.pyplot as plt



def s(x, N=10): 
    
    S = 0 
    
    for n in range(1, N): 
        
        S += (x**n)/(n)
    
    return S

xs = np.linspace(0, 10, 1000)
ys = s(xs, N=10**2)

plt.plot(xs, ys)





















