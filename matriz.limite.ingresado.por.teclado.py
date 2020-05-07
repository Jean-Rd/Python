# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:37:15 2020

@author: DELL.E5430.SSD
"""

import datetime
matriz = []
c = 0

date_time = datetime.datetime.now()
n = int(input('Digite un digito: '))
print()

for i in range(n):
    matriz.append([0]*n)

for i in range(n):
    matriz[i][i] = n
    matriz[i][-i-1] = n
    
for i in matriz:
    print(i)
print()
print(date_time.strftime('%d/%m/%Y %H:%M:%S'))