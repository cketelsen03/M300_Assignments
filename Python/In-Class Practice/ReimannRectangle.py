# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 10:54:58 2022

@author: chanm
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle


def Reimann(f, a=0, b=1, N=10):
    
    xs = np.linspace(a, b, N)
    ys = f(xs)
    
    dx = (b-a)/N
    
    fig, ax = plt.subplots()
    
    for i in range(0, N):
        
        x_i = a + dx*i

        
        ax.plot(xs, ys)
        
        ax.add_patch(Rectangle((x_i, 0), dx, f(x_i), edgecolor="black", facecolor="purple"))

# We can also make the rectangles look pretty: 
    
    
    
    
        


























