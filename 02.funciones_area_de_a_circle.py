# -*- coding: utf-8 -*-
"""
Created on Mon May 11 22:41:55 2020

@author: DELL.E5430.SSD
"""

from numpy import pi
import datetime

def area_circle(r):
    return (r**2)*pi

print('\n\tAREA DE UN CIRCULO\n')
ahora = datetime.datetime.now()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
radio = float(input('Digite el radio del circulo: '))
print(area_circle(radio))
opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
while(opcion != 2):
    if(opcion == 1):
        radio = float(input('Digite el radio del circulo: '))
        print(area_circle(radio))
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
    else:
        print('Por favor ingrese una opcion valida')
        opcion = int(input('\n\t1. Continuar\n\t2. Salir\n\nDigite una opcion: '))
