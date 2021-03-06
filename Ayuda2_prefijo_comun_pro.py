# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:28:59 2020

@author: DELL.E5430.SSD
"""

import datetime

def obtener_prefijo_más_común(cadena):

    palabras = cadena.split()

    if not palabras: return ""

    i = 0

    while True:

        try:

            únicos = set(palabra[i] for palabra in palabras)

            if len(únicos) != 1:
                break

        except IndexError:
            break

        i += 1

    return palabras[0][:i]


if __name__ == "__main__":
    
    ahora = datetime.datetime.now()
    
    cadena = input('Ingrese un texto: ')

    prefijo = obtener_prefijo_más_común(cadena)

    print(prefijo)
    
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))