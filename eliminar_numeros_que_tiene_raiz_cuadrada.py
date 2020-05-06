# -*- coding: utf-8 -*-
"""
Created on Wed May  6 15:58:44 2020

@author: DELL.E5430.SSD
"""

numeros = [1, 2, 1, 5, 0, 3]

num = (x**(1/2) for x in numeros)
num1 = (i for i in num if i % 1 != 0)
for j in num1:
    print(round(j))