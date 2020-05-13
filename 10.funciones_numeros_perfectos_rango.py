# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:57:30 2020

@author: DELL.E5430.SSD
"""


import datetime

ahora = datetime.datetime.now()
perfectos = []
def es_perfecto(n):
    if(n < 6):
        return False
    else:
        for i in range(6,n+1):
            sumatorio = 0
            for j in range(1,i):
                if(i % j == 0):
                    sumatorio += j
            if(sumatorio == i):
                perfectos.append(i)
        return perfectos


rango = int(input('Digite la cantidad de numeros que desea examinar: '))
if(es_perfecto(rango) == False):
    print(f'En este rango no hay numeros perfectos.')
else:
    print(f'Los numeros perfectos son: {perfectos}')