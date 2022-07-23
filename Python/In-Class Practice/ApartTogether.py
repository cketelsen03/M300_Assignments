# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:39:43 2022

@author: chanm
"""

import sympy as sp
import numpy as np

sp.init_printing()

u, v = sp.symbols('u, v')

expr = 1/((u+1)*(u-1))

display(expr.apart())

# The ".together()" function does the inverse operation of this. 

display(sp.diff(cos(x), x))

display(sp.integrate(1/x, (x, 1, 3)))


# To print out the fancy text integral, use the following command: 
    # (and the same can be done for differentiaiton): 
        
display(sp.Integral((1/x), (x, 1, 3)))


# The "solve" function looks for roots of an algebraic expression: 

display(sp.solve((x**2), x)














