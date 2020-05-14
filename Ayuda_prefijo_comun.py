# -*- coding: utf-8 -*-
"""
Created on Thu May 14 15:28:39 2020

@author: DELL.E5430.SSD
"""


def obtener_prefijo_más_común(cadena):

    palabras = cadena.split()

    palabras.sort(key=lambda x: len(x))

    más_corta = palabras.pop(0)

    for i in range(len(más_corta), 0, -1):

        prefijo = más_corta[:i]

        for palabra in palabras:

            if not palabra.startswith(prefijo):
                break

        else:
            return prefijo

    return ""


if __name__ == "__main__":

    cadena = 'poliedro policia polifona polinizar polaridad politica'

    prefijo = obtener_prefijo_más_común(cadena)

    print(prefijo)