# -*- coding: utf-8 -*-
"""
Created on Tue May 12 23:16:40 2020

@author: DELL.E5430.SSD
"""

numeros = []
def numeros_contiguos(numero):
    contiguos = 0
    for i in range(1,len(numero)):
        sumatorio = numero[i] - numero[i-1]
        contiguos += sumatorio
    return contiguos
    

rango = int(input('Digite la cantidad de numeros: '))
for i in range(rango):
    num = float(input('Digite un numero --> '))
    numeros.append(num)
print(numeros_contiguos(numeros))