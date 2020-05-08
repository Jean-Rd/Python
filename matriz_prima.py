# -*- coding: utf-8 -*-
"""
Created on Fri May  8 08:39:43 2020

@author: DELL.E5430.SSD
"""
import numpy as np
fil = []
col = []
m = int(input('Digite las filas de la matriz: '))
n = int(input('Digite las columnas de la matriz: '))

matriz = np.zeros((m,n))

for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input(f'Fila {i+1}, columna {j+1}, Digite el elemento: '))
        
for i in range(m):
    fila = 0
    for j in range(n):
        fila += matriz[i][j]
    fil.append(fila)

for i in range(m):
    columnas = 0
    for j in range(n):
        columnas += matriz[j][i]
    col.append(columnas)
for i in range(len(fil)):
    val = fil[i] in col
    if(val == True):
        print('La matriz si es prima.')
        break

print()
for i in matriz:
    print(i)
    