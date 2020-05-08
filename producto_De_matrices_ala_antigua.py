# -*- coding: utf-8 -*-
"""
Created on Thu May  7 23:00:47 2020

@author: DELL.E5430.SSD
"""


p = int(input('Digite el nuemro de filas de A: '))
q = int(input('Digite el numeros de columnas de A,(filas de B): '))
r = int(input('Digite el numeros de columnas de B: '))

matriz_a = []
matriz_b = []
for i in range(p):
    matriz_a.append([0]*q)
    
for i in range(q):
    matriz_b.append([0]*r)

print()
print('Matriz A')
for i in range(p):
    for j in range(q):
      matriz_a[i][j] = int(input(f'Matriz A; fila {i+1}, columnas {j+1}: '))
      
print()
print('Matriz B')
for i in range(q):
    for j in range(r):
        matriz_b[i][j] = int(input(f'Matriz B: fila {i+1}, columnas {j+1}: '))

print()
matriz_producto = []
for i in range(p):
    matriz_producto.append([0]*r)

# EL CALCULO

for i in range(p):
    for j in range(r):
        for k in range(q):
            matriz_producto[i][j] += matriz_a[i][k] * matriz_b[k][j]

print('Matriz A')
for i in matriz_a:
    print(i)
print()
print('Matriz B')
for i in matriz_b:
    print(i)
print()
print('Matriz C')
for i in matriz_producto:
    print(i)