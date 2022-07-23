# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 11:33:50 2022

@author: chanm
"""

import random

class ellipse():
    
    def __init__(self, cx = 0, cy = 0, r = 1):
        
        self.cx = cx
        self.cy = cy
        self.r = r
        
class circle(ellipse):
    def __init__(self):
        self.cx = self.cy        
        
        
circles = [circle(cx = random.randint(1, 25), cy = random.randint(1, 25)) for i in range(25)]




















