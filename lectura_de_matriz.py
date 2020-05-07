# -*- coding: utf-8 -*-
"""
Created on Wed May  6 20:47:45 2020

@author: DELL.E5430.SSD
"""
matriz = []
m = int(input("Digite un rango para las filas de la matriz --> "))
n = int(input("Digite un rango para las columnas de la matriz --> "))

for i in range(m):
    matriz.append([0]*n)
    
for i in range(m):
    k = 1
    for j in range(n):
        matriz[i][j] = int(input(f'Digite un valor para la fila {i+1}, columna {k}: '))
        k+=1
for i in matriz:
    print(i)