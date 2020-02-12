# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 21:31:45 2020

@author: andrz
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

poznan = [3, 5, 7, 6, 4, 6, 14, 15, 16, 18, 17, 20, 25, 19]
zako   = [1, 2, 5, 4, 7, 8, 4, 3, 2, 5, 7, 6, 5, 8]
bialy = [-2, 0, 2, -2, -4, 5, 7, 10, 15, 9, 7, -2, -3, -1]

plt.plot(poznan, marker = '*', label = "Poznań")
plt.plot(zako, marker = 'v', label = "Zakopane")
plt.plot(bialy, marker = 'D', label = "Białystok")
plt.title('Wykres temperatur')
plt.xlabel('dni')
plt.ylabel('stopnie Celsjusza')
plt.legend()
plt.show()