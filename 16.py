# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:12:26 2020

@author: andrz
"""

import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns

def wykres():
    liczba = int(input('Po ile elementów chcesz wprowadzić: '))
    x = []
    for liczba in range(1, liczba+1):
        x.append(float(input('Podaj ' + str(liczba) + '. argument\n')))
    
    y = []
    for liczba in range(1, liczba+1):
        y.append(float(input('Podaj ' + str(liczba) + '. wartosc\n'))) 
    
    plt.plot(x, y,  marker = 'v', label = "Xy")
    plt.title('Wykres podanych przez Ciebie wartosci')
    plt.xlabel('Xy')
    plt.ylabel('Yki')
    plt.legend()
    plt.show()
    
wykres()