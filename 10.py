# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:54:25 2020

@author: andrz
"""
import numpy as np
from math import sqrt


def srednia(liczby):
    summary = 0
    for numer in liczby:
        summary += numer
    
    return summary / len(liczby)

def odchyl(liczby, mean):
    summary = 0
    for numer in liczby:
        summary += (numer - mean)**2
        
    return sqrt(summary/(len(liczby)))

def ux():
    numer_of_elementy = int(input('Ile elementów chcesz wprowadzić:'))
    elementy = []
    for element_numer in range(1, numer_of_elementy+1):
        elementy.append(int(input('Podaj ' + str(element_numer) + ' element')))
    
    mean = srednia(elementy)
    std_dev = odchyl(elementy, mean)
    
    print('Średnia podanych przez Ciebie elementów wynosi', mean)
    print('Średnia obliczona przez pakiet numpy to', np.mean(elementy))
    
    print('Odchylenie standardowe podanych przez Ciebie elementów wynosi', std_dev)
    print('Odchylenie standardowe obliczone przez pakiet numpy to', np.std(elementy))
    
ux()