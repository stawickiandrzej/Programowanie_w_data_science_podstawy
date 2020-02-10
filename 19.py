# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:04:16 2020

@author: andrz
"""

months = {1 : 31, 2 : 28, 3:31, 4:30,5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
namemonths = {1 : 'Styczeń', 2 : 'Luty', 3:'Marzec', 4:'Kwiecień',5:'Maj', 6:'Czerwiec', 7:'Lipiec', 8:'Sierpień', 9:'Wrzesień', 10:'Październik', 11:'Listopad', 12:'Grudzień'}
x = int(input("Podaj numer miesiąca dla którego chcesz poznać liczbę dni "))

print(namemonths[x],'ma', months[x], 'dni')
