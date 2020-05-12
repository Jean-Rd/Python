# -*- coding: utf-8 -*-
"""
Created on Mon May 11 23:13:32 2020

@author: DELL.E5430.SSD
"""


import datetime

def centigrados_farenheit(c):
    c = (c*9/5)+32
    return c

print('\n\tCENTIGRADOS A FARENHEIT\n')
ahora = datetime.datetime.now()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
print()
temperatura = float(input('Digite la temperatura en centigrados: '))
print(centigrados_farenheit(temperatura))
opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
while(opcion != 2):
    if(opcion == 1):
        temperatura = float(input('Digite la temperatura in centigrados: '))
        print(centigrados_farenheit(temperatura))
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    else:
        print('Por favor ingrese una opcion valida.')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
