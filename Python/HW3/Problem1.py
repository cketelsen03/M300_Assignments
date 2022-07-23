# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 10:36:42 2022

@author: chanm
"""

from scipy.linalg import *
import numpy as np

A  = np.array([[1, 3], [2, 4]])
b = np.array([5, 8])

x = solve(A, b)

print("\nThe solution is the vector {}.".format(x))




















