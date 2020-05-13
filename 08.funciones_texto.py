# -*- coding: utf-8 -*-
"""
Created on Tue May 12 21:16:23 2020

@author: DELL.E5430.SSD
"""
import datetime

ahora = datetime.datetime.now()

def es_repeticion(palabra):
    n = len(palabra)
    if n % 2 == 0:
        derecha = palabra[0:n//2]
        izquierda = palabra[n//2:]
        return derecha == izquierda

cadena = input('Ingrese la palabra: ')
if(es_repeticion(cadena) == True):
    print("Correcto.")
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
else:
    print('Incorrecto.')
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))