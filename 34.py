# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 21:21:30 2020

@author: andrz
"""

class Kwadrat:
    def __init__(self,a):
        self.a = a
    description = "Klasa kwadratu"
    def dlugosc(self):
        return self.a
    def powierzchnia(self):
        return self.a * self.a
    def obwod(self):
        return 4 * self.a
