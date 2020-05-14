# -*- coding: utf-8 -*-
"""
Created on Wed May 13 23:49:00 2020

@author: DELL.E5430.SSD
"""


from math import sqrt
import datetime


def cuadrado(x):
    return x**2

def suma_cuadrados(v):
    s = 0
    for i in v:
        s += cuadrado(i)
    return s

# Programa Principal
vector = []
ahora = datetime.datetime.now()
for i in range(3):
    vector.append(float(input('Dame un numero: ')))
y = suma_cuadrados(vector)
print('Distancia al origen:',sqrt(y))

# Coordenada Temporal
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))