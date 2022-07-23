# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 10:40:43 2022

@author: chanm
"""

import numpy as np

class circle():
    
    def __init__(self, cx = 0, cy = 0, r = 1):
        
        self.cx = cx
        self.cy = cy
        self.r = r
        
        
    def area(self):
        
            # Code to return area of a particular circle
            
            return np.pi*(self.r)**2
        
        
    def circumference(self):
        
        # Code to return the circumference of a circle
        
        return 2*np.pi*self.r
    
    def inside(self, x, y):
        
        # Return boolean value based on a position (x, y) and the circle's position
        
        d = np.sqrt((self.cx - x) ** 2 + (self.cy - y) ** 2)
        
        return d <= self.r 











