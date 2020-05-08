# -*- coding: utf-8 -*-
"""
Created on Thu May  7 21:18:16 2020

@author: DELL.E5430.SSD
"""

# Difirencia de dos matrices, lea por teclado

m = int(input('Digite la cantidad de filas --> '))
n = int(input('Digite la cantidad de colunmas --> '))

matriz_1 = []
matriz_2 = []
matriz_diferencia = []

for i in range(m):
    matriz_1.append([0]*n)
    matriz_2.append([0]*n)
    
for i in range(m):
    for j in range(n):
        matriz_1[i][j] = int(input(f'Matriz A: fila {i+1}, columna {j+1}: '))
print()       

for i in range(m):
    for j in range(n):
        matriz_2[i][j] = int(input(f'Matriz B: fila {i+1}, columna {j+1}: '))
print()
print('Matriz A')
for i in matriz_1:
    print(i)
print()
print('Matriz B')
for i in matriz_2:
    print(i)
print()
for i in range(m):
    matriz_diferencia.append([0]*n)
for i in range(m):
    for j in range(n):
        matriz_diferencia[i][j] = matriz_1[i][j] - matriz_2[i][j]   

print('La matriz diferencia es: ')
print()
for i in matriz_diferencia:
    print(i)