# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 11:38:58 2022

@author: chanm
"""

import CircleClass as crc
import matplotlib.pyplot as plt
import numpy as np
import random


c1 = crc.circle(cx = random.randint(1, 25), cy = random.randint(1, 25), r = random.randint(1, 25))

circle_plot = plt.Circle((c1.cx, c1.cy), c1.r, fill = False)

fig, ax = plt.subplots()
ax.axis([-50, 50, -50, 50])

ax.add_artist(circle_plot)

plt.show()














