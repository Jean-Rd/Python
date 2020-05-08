# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:19:07 2020

@author: DELL.E5430.SSD
"""


import numpy
import sys

fila_1 = int(input('Matriz A: Filas: '))
columna_1 = int(input('Matriz A: columna: '))
fila_2 = int(input('Matriz B: Filas: '))
columna_2 = int(input('Matriz B: columna: '))

if columna_1 != fila_2:
    print('Estas matrices no se pueden multiplicar.')
    sys.exit()


matriz_1 = numpy.zeros((fila_1,columna_1))
matriz_2 = numpy.zeros((fila_2,columna_2))
matriz_resultante = numpy.zeros((fila_1,columna_2))

for i in range(fila_1):
    for j in range(columna_1):
        matriz_1[i][j] = int(input(f'Matriz A: fila {i+1}, columna {j+1}: '))
            
for i in range(fila_2):
    for j in range(columna_2):
        matriz_2[i][j] = int(input(f'Matris B: fila {i+1}, columna {j+1}: '))
    
for i in range(fila_1):
    for j in range(columna_2):
        for k in range(fila_2):
            matriz_resultante[i][j] += matriz_1[i][k] * matriz_2[k][j]
print()
print('Matriz A')
for i in matriz_1:
    print(i)
        
print()
print('Matriz B')
for i in matriz_2:
    print(i)
    
print()
print('Matriz Resultante')
for i in matriz_resultante:
    print(i)
        