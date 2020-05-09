# -*- coding: utf-8 -*-
"""
Created on Sat May  9 16:32:15 2020

@author: DELL.E5430.SSD
"""
import numpy as np

# Generando un bucle random

a = np.linspace(0,9,15)
print(a,'\n')
print(a.sum(),'\n') # Sumamos todos los elementos puede guardar en variable
print(a.max(),'\n') # Maximo de todos, puede guardar en variable
print(a.min(),'\n') # Minimo de todos, puede guardar en variable

# operaciones con axis

a = np.arange(12).reshape(3,4)
print(a,'\n')

b = a.sum(axis = 0)  # Suma de la primera columna
print(b,'\n')  #lo guarda en una columna

b = a.min(axis=1)  # calor minimo de cada columna
print(b,'\n') # lo guarda en un array

b = a.cumsum(axis=1) #suma acumulativa, la suma es por fila
print(b,'\n')
print('----------un_ejemplo_de_iteraciomn--------')

print(a)
for i in a.flat:  # matriz_mame.flat --> con esa fumcion podemos operar con cada valor de la matris
    print(i)
    
