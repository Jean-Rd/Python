# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:53:21 2020

@author: DELL.E5430.SSD
"""


import datetime

ahora = datetime.datetime.now()
def es_perfecto(n):
    i = 1
    sumatorio = 0
    while(i < n):
        if(n % i == 0):
            sumatorio += i
        i += 1
    return sumatorio == n


numero = int(input('Digite un numero --> '))
if(es_perfecto(numero) == True):
    print(f'El numero {numero},  si es perfecto!!!')
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
else:
    print(f'El numero {numero}, no es perfecto.')
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
