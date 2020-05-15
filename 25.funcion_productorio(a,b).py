# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:14:35 2020

@author: DELL.E5430.SSD
"""

# Productorio de a ^ b

import datetime

def Productorio(a,b):
    if a > b: return 0
    if 0 in range(a,b): return 0
    producto = 1
    for i in range(a,b+1):
        producto *= i
    return producto

# Programa Principal

ahora = datetime.datetime.now()

a = int(input('Productorio Inicio: '))
b = int(input('Productorio Fin: '))
print()
print('El productorio es:',Productorio(a,b))
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))