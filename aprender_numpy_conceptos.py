# -*- coding: utf-8 -*-
"""
Created on Fri May  8 11:59:17 2020

@author: LustrosoBurbuja
"""
# Introduccion a numpy

import numpy as np
'''
np.array() --> aca creamos la matriz,(inicio,fin menos 1), solo los parametros de nuestra matriz
.reshape(filas,columnas) --> las dimensiones de nuestra matriz
agregamos re para ingresar los parametros
'''
a = np.arange(0,15).reshape(3,5)
print(a,'\n')
'''
matriz_name.shape --> con esta linea imprimimos las dimensiones de nuestra matriz
'''
print(a.shape,'\n')
'''
name_matriz.ndim --> El numeros de ejes de nuestra matriz en este caso son 2 eje 'x'^'y'
'''
print(a.ndim,'\n')
'''
name_matriz.dtype.name --> Nos regresa el tipo de datos que contien la matriz (int, float, bool, str)
'''
print(a.dtype.name, '\n')
'''
tipo de dato, en este caso es una clase de numpy
'''
print(type(a))

print('------------------------------------------------------------------')
'''
A continuacion ingresaremos por teclado 2 parametros e incluiremos estos en 
una array (vector) y utilizaremos estos valores para paremetrizar una matriz
'''

m = int(input('Digite la cantidad de filas: '))
n = int(input('Digite la cantidad de columnas: '))

b = np.zeros((m,n))  #matriz
c = np.array((m,n))  #vector
for i in range(m):
    for j in range(n):
        b[i,j] = int(input(f'Fila {i+1}, columna {j+1} --> '))
        
print(f"Vector {c}")        
print()
print(f'Matriz con los rangos {m} ^ {n}')
print(b)
