# -*- coding: utf-8 -*-
"""
Created on Thu May 14 22:38:10 2020

@author: DELL.E5430.SSD
"""

import datetime

def numeros_amigos(num1,num2):
    numeros = [num1,num2]
    amigos = []
    for i in numeros:
        suma = 0
        for j in range(1,(i//2)+1):
            if(i % j == 0):
                suma += j
        amigos.append(suma)
    return numeros[0] == amigos[1]

# Programa Principal

ahora = datetime.datetime.now()

amigo_uno = int(input('Digite un numero --> '))
amigo_dos = int(input('Digite un numero --> '))

print()
print(f'{amigo_uno} ^ {amigo_dos}\nSon numeros amigos:',numeros_amigos(amigo_uno,amigo_dos))
print()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))