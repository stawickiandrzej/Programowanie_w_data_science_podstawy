# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 19:42:26 2020

@author: andrz
"""


def iteracyjna_silnia(number):
    if number <= 2:
        return number
    
    result = 1
    for i in range(2, number+1):
        result *= i
        
    print(result)

def rekur_silnia(number, result=0):
    if result == 0:
        result = number
        
    if number-1 >= 1:
        result *= (number-1)
        rekur_silnia(number-1, result=result)
    else:
        print(result)
        

number = int(input('Podaj liczbę'))
iteracyjna_silnia(number)
rekur_silnia(number)