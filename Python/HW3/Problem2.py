# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:44:03 2022

@author: chanm
"""

import numpy as np
import matplotlib.pyplot as plt


def s(N): 
    
    global d
    
    d = np.zeros(N)
    S = 0
    
    for n in range(1, N):
        
        d[n] = ((-1)**(n-1)*(n**(-1)))
        S += d[n-1]
        
    
    return S

N = int(input("Index n goes from 1 to ___: "))

print("\nThis finite alternating harmonic series evaluates to {}.".format(str(s(N))))

index = np.arange(0, N, 1)
plt.plot(index, d)










