# -*- coding: utf-8 -*-
"""
Created on Mon Jul 18 11:06:37 2022

@author: chanm
"""

import sympy as sp
import numpy as np

a = np.pi
b = sp.pi

print(a)
print(b)

# Also, you can evaluate symbolic values to "10" using the ".evalf()" extension: 
    
print(b.evalf(10))

# Now the shell prints out a floating point value. 
# SymPy enormously slows down the computation speed, but it's still very useful 
#   at the right times. 

x, y = sp.symbols("x, y")
sp.var('u, v')

display(x + x + y)

expr = (u + v)**4

display(expr.expand())

newexpr = expr.expand()

display(newexpr.factor())

display(newexpr.subs(u, 2))

display(newexpr.subs(u, 2).factor())




























