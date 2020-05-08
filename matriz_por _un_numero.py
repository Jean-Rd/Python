# -*- coding: utf-8 -*-
"""
Created on Thu May  7 22:06:37 2020

@author: DELL.E5430.SSD
"""


m = int(input('Digite las filas de la matriz --> '))
n = int(input('Digite las columnas de la matriz --> '))
matriz = []
for i in range(m):
    matriz.append([0]*n)
for i in range(m):
    for j in range(n):
        matriz[i][j] = int(input(f'Matriz: Fila {i+1}, columna {j+1}: '))
print()
for i in matriz:
    print(i)
producto = int(input('Digite un numero por el cual quiere multiplicar toda la matriz: '))
for i in range(m):
    for j in range(n):
        matriz[i][j] = matriz[i][j] * producto
print()
print('El producto de {producto} por la matriz es: ')
for i in matriz:
    print(i)