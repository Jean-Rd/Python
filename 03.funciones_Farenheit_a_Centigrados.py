# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:03:47 2020

@author: DELL.E5430.SSD
"""

import datetime

def farenheit_centigrados(c):
    c = (c-32)*(5/9)
    return c

print('\n\tFARENHEIT A CENTIGRADOS\n')
ahora = datetime.datetime.now()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
print()
temperatura = float(input('Digite la temperatura ne Farenheit: '))
print(farenheit_centigrados(temperatura))
opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
while(opcion != 2):
    if(opcion == 1):
        temperatura = float(input('Digite la temperatura ne Farenheit: '))
        print(farenheit_centigrados(temperatura))
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    else:
        print('Por favor ingrese una opcion valida.')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
