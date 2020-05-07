# -*- coding: utf-8 -*-
"""
Created on Wed May  6 19:40:59 2020

@author: LustrosoBurbuja
"""
matriz = []
c = 0
for i in range(4):
    matriz.append([0]*4)
    
#while(c < 4):
 #   matriz[c][c] = 1
  #  c+=1

for i in range(4):
    matriz[i][i] = 1
    
for i in matriz:
    print(i)