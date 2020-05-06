# -*- coding: utf-8 -*-
"""
Created on Wed May  6 18:15:49 2020

@author: LustrosoBurbuja
"""

# Elimina los elementos par
import datetime
numeros = []
impares = []
date_time = datetime.datetime.now()
cantidad = int(input('Digite la cantidad de digitos que ingresara: '))
for i in range(cantidad):
    digito = int(input('Ingrese un digito: '))
    numeros.append(digito)
    
impar = (x for x in numeros if x % 2 != 0)
for i in impar:
    impares.append(i)
    
print(f'Los numeros impares son {impares}')
print()
print(date_time.strftime('%d/%m/%Y %H:%M:%S'))
