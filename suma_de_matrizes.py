# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:30:25 2020

@author: DELL.E5430.SSD
"""


m = int(input('Digite la cantidad de filas: '))
n = int(input('Digite la cantidad de columnas: '))

matriz_a = []
matriz_b = []
matriz_suma = []

for i in range(m):
    matriz_a.append([0]*n)
    
for i in range(m):
    matriz_b.append([0]*n)
        
print('Matriz A:')
for i in range(m):
    for j in range(n):
        matriz_a[i][j] = int(input(f'Matriz A --> Fila {i+1}, columna {j+1}: '))
print()
        
print('Matriz B:')
for i in range(m):
    for j in range(n):
        matriz_b[i][j] = int(input(f'Matriz B --> Fila {i+1}, columna {j+1}: '))
print()
    
print('Matriz A')
for i in matriz_a:
    print(i)
print()
    
print('Matriz B')
for i in matriz_b:
    print(i)
print()

#sumamos

for i in range(m):
    matriz_suma.append([0]*n)
    
for i in range(m):
    for j in range(n):
        matriz_suma[i][j] = matriz_a[i][j] + matriz_b[i][j]
        
print('La matriz suma es: ')
for i in matriz_suma:
    print(i)