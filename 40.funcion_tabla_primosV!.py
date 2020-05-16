# -*- coding: utf-8 -*-
"""
Created on Sat May 16 17:18:38 2020

@author: DELL.E5430.SSD
"""

import datetime

def es_primo(n):
    creo_que_es_primo = True
    for i in range(2,n):
        if(n % i == 0):
            creo_que_es_primo = False
            break
    return creo_que_es_primo

def tabla_primos(m):
    for i in range(1, m+1):
        if(es_primo(i) == True):
            print('El numero',i,',es primo.')
            
# Programa Principal
ahora = datetime.datetime.now()

rango = int(input('Digite un rango --> '))
tabla_primos(rango)
print()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))