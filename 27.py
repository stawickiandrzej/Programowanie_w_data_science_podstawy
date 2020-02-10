# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 21:03:40 2020

@author: andrz
"""

from scipy.stats import kurtosis

def ux():
    liczba = int(input('Ile elementów chcesz wprowadzić: '))
    lista = []
    for liczba in range(1, liczba+1):
        lista.append(int(input('Podaj ' + str(liczba) + ' element\n')))
    print('Wartosć kurtozy dla podanych liczb wynosi', kurtosis(lista))
    
ux()
