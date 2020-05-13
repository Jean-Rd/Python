# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:38:45 2020

@author: DELL.E5430.SSD
"""

def es_perfecto(n):
    sumatorio = 0
    for i in range(1,n):
        if(n % i == 0):
            sumatorio += i
    return sumatorio == n


numero = int(input('Digite un numero --> '))
if(es_perfecto(numero) == True):
    print(f'El numero {numero},  si es perfecto!!!')
else:
    print(f'El numero {numero}, no es perfecto.')
