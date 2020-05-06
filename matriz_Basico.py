# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:28:12 2020

@author: LustrosoBurbuja
"""
# Matriz nula de 5x5

m = [[1,0,0],[0,1,0],[0,0,1]]
print(m[-1][0])
print(m[-1][-1])
print('--')
for i in range(0,3):
    print(m[i])
print('--')
for i in range(0,3):
    for j in range(0,3):
        print(m[i][j])