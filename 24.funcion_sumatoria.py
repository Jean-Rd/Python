# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:03:43 2020

@author: DELL.E5430.SSD
"""

import datetime

def sumatoria(a,b):
    if a > b: return 0
    x = (i for i in range(a,b+1))
    return sum(x)

# Programa Principal

ahora = datetime.datetime.now()

a = int(input('Sumatoria Inicio: '))
b = int(input('Sumatoria Fin: '))

print('Resultado de la sumatoria es:',sumatoria(a,b))
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))