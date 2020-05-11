# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:16:28 2020

@author: DELL.E5430.SSD
"""


import numpy as np

a = np.arange(12).reshape(3,4)
print(a)
b = a < 5
print('a < 5')
print(b)

print()
print(a[b]) #imprime solo hasta el rango

a[b] = 0
print(a) #cambia los valors de del rango b por 0

