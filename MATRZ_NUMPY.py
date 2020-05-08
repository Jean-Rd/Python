# -*- coding: utf-8 -*-
"""
Created on Fri May  8 01:19:07 2020

@author: DELL.E5430.SSD
"""


import numpy

filas = int(input('Digite el nuemro de filas de A: '))
columna_fila2 = int(input('Digite el numeros de columnas de A,(filas de B): '))
columna2 = int(input('Digite el numeros de columnas de B: '))

matriz_1 = numpy.zeros((filas, columna_fila2))
matriz_2 = numpy.zeros((columna_fila2, columna2))
matriz_resultante = numpy.zeros((filas, columna2))
print()
print('Matriz A')
for i in range(filas):
    for j in range(columna_fila2):
        matriz_1[i][j] = int(input(f'Matriz A: fila {i+1}, columna {j+1}: '))
print()
print('Matriz B')
for i in range(columna_fila2):
    for j in range(columna2):
        matriz_2[i][j] = int(input(f'Matriz A: fila {i+1}, columna {j+1}: '))
        
print()
for i in range(filas):
    for j in range(columna2):
        for k in range(columna_fila2):
            matriz_resultante[i,j] = matriz_1[i, k] * matriz_2[k, j]
            
print()
print('Matriz Resultante: ')
for i in matriz_resultante:
    print(i)