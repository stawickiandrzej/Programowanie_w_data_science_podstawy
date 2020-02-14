# -*- coding: utf-8 -*-
"""
Created on Tue Feb 11 20:13:03 2020

@author: andrz
"""
from numpy import corrcoef

def pearson():
    liczba = int(input('Po ile elementów chcesz wprowadzić: '))
    x = []
    for liczba in range(1, liczba+1):
        x.append(float(input('Podaj ' + str(liczba) + ' element\n')))
    
    y = []
    for liczba in range(1, liczba+1):
        y.append(float(input('Podaj ' + str(liczba) + ' element\n'))) 
    
    print('Wartosć współczynnika korelacji Pearsona dla podanych liczb wynosi', pearson)
    return pearson    

