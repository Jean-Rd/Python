# -*- coding: utf-8 -*-
"""
Created on Tue May 12 00:13:17 2020

@author: DELL.E5430.SSD
"""

letras = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
def DNI(letra):
    letra = numero % 22
    return letras[letra]


numero = int(input('Digite el numero para otorfarle una letra: '))

print(numero,DNI(numero))