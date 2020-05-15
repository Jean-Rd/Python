# -*- coding: utf-8 -*-
"""
Created on Thu May 14 20:42:55 2020

@author: DELL.E5430.SSD
"""
# ax + b = 0

import datetime

def primer_grado(a,b):
    if a != 0: 
        x = -b/a
        return x

# Programa Principal

ahora = datetime.datetime.now()
a = float(input('Digite el valor de a: '))
b = float(input('Digite el valor de b: '))
if(a == 0):
    if(b != 0):
        print('La ecuacion no tiene solucion.')
    if(b == 0):
        print('La ecuacion tiene infinitas soluciones.')
print(f'La solucion ala eciacion [{a}x + {b} = 0], es: ',primer_grado(a,b))
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
