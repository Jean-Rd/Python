# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:41:27 2020

@author: DELL.E5430.SSD
"""

import datetime

def comprueba_letra_dni(numero,letra):
    return letra == letras[numero % 23]

# Programa Principal

letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
ahora = datetime.datetime.now()

numero_dni = int(input('Digite su numero DNI: '))
letra_dni = input('Ingrese la letra de su DNI: ').upper()
print()
print(f'Sus datos {numero_dni}{letra_dni} es',comprueba_letra_dni(numero_dni,letra_dni))
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
