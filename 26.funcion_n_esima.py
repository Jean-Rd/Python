# -*- coding: utf-8 -*-
"""
Created on Thu May 14 21:29:27 2020

@author: DELL.E5430.SSD
"""

# Raiz_n_esima

import datetime

def raiz_n_esima(x,n):
    return x**(1/n)

# Programa Principal

ahora = datetime.datetime.now()

numero = int(input('Digite un numero --> '))
raiz = int(input(f'Digite una raiz para el numero {numero} --> '))
print()
print('La raiz es:',raiz_n_esima(numero,raiz))
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))