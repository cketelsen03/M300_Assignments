# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 10:30:47 2022

@author: chanm
"""

import sympy as sp
import numpy as np

pi = sp.pi

x = sp.symbols('x')
f = sp.Function('f')


f = x**3 - ((sp.cos(pi*x))**2)/(2*x**2 + 1) + 11/3*x**2 - 1

display(f.diff(x))





















