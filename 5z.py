"""
Created on Fri Feb 14 21:41:17 2020

@author: andrz
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_style('darkgrid')

titanic = pd.read_csv(r'C:\Users\andrz\OneDrive\Dokumenty\python\csv.csv', sep = ';')
titanic.head()

titanic['Age'].hist(bins=20)

