# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:04:17 2020

@author: DELL.E5430.SSD
"""


numeros = [1, 2, 1, 5, 0, 3]

num = (x**(1/2) for x in numeros)
num1 = (i for i in num if i % 1 != 0)
num2 = (k**2 for k in num1)
for j in num2:
    print(round(j))