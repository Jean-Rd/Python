# -*- coding: utf-8 -*-
"""
Created on Fri May 15 21:19:19 2020

@author: DELL.E5430.SSD
"""

import datetime

def es_perfecto(n):
    
    sumatorio = 0
    
    for i in range(1,n):
    
        if n % i == 0:
        
            sumatorio += i
    
    return sumatorio == n


def tabla_perfecto(m):
    
    for i in range(1,m+1):

        if es_perfecto(i):

            print(i, 'Es un numero perfecto.')

# Programa Principal
ahora =  datetime.datetime.now()

numero = int(input('Dame un numero: '))

print(tabla_perfecto(numero))
print()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))