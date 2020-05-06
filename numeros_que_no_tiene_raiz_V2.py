# -*- coding: utf-8 -*-
"""
Created on Wed May  6 17:47:16 2020

@author: DELL.E5430.SSD
"""
numeros = []
sin_raiz = []
cantidad = int(input('Digite la cantidad de numeros que ingresara: '))
for y in range(cantidad):
    digito = int(input('Digite un numero: '))
    numeros.append(digito)
num = (x**(1/2) for x in numeros)
num1 = (i for i in num if i % 1 != 0)
num2 = (k**2 for k in num1)
for j in num2:
    sin_raiz.append(round(j))
    
print(f'Los numeros que no tienen raiz son {sin_raiz}')