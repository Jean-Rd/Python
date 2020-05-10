# -*- coding: utf-8 -*-
"""
Created on Fri May  8 03:39:27 2020

@author: DELL.E5430.SSD
"""
import numpy

fila_1 = int(input('Matriz A: Filas: '))
columna_1 = int(input('Matriz A: columna: '))

matriz_1 = numpy.zeros((fila_1,columna_1))
matriz_2 = numpy.zeros((columna_1,fila_1))

for i in range(fila_1):
    for j in range(columna_1):
        matriz_1[i][j] = int(input(f'Fila {i+1}, columna{j+1}, digite un elemento: '))
        matriz_2[j][i] = matriz_1[i][j]
        
for i in matriz_1:
    print(i)
    
    
     
for i in matriz_2:
    print(i)
    
