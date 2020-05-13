# -*- coding: utf-8 -*-
"""
Created on Tue May 12 22:37:25 2020

@author: DELL.E5430.SSD
"""

import datetime

def biesto(year):
    if(year % 4 == 0 and year % 100 != 0):
        return True
    elif(year % 4 == 0 and year % 100 == 0 and year % 400 == 0):
        return True
    else:
        return False
   
    
year = int(input('Digite el year: '))
if(biesto(year) == True):
    print(f'El year {year}, si es biesto; Tiene 366 dias.')
else:
    print(f'El year {year}, no es biesto; Tiene 365 dias.')
    
