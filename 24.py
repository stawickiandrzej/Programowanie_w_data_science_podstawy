# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:41:31 2020

@author: andrz
"""

import numpy as np

def ux():
    liczba = int(input('Ile elementów chcesz wprowadzić: '))
    lista = []
    for liczba in range(1, liczba+1):
        lista.append(int(input('Podaj ' + str(liczba) + ' element\n')))
    print('Podane wartosci odchylają się od sredniej przeciętnie o', np.std(lista))
    
ux()
