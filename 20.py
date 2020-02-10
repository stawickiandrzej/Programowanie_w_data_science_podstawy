# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 20:22:47 2020

@author: andrz
"""

namemonths = {'Styczeń' : 'January', 'Luty' : 'February', 'Marzec' : 'March', 'Kwiecień' : 'April', 'Maj' :'May', 'Czerwiec' :'June', 'Lipiec' : 'July', 'Sierpień' : 'August', 'Wrzesień' : 'September', 'Październik' : 'October', 'Listopad' : 'November', 'Grudzień' : 'December'}


x = str(input('Podaj nazwę miesiąca po polsku ')).capitalize()

print(x, 'po polsku to',namemonths[x],'po angielsku')
