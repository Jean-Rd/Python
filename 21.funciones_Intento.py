# -*- coding: utf-8 -*-
"""
Created on Thu May 14 00:09:05 2020

@author: DELL.E5430.SSD
"""


import datetime

def Perimetro_Triangle(datos):
    return perimetro

# Programa Principal
ahora = datetime.datetime.now()
message = ['Digite el primer cateto: ','Digite el segundo cateto: ','Digite la hipotenusa: ','El perimetro es: ']
perimetro = 0
for i in range(3):
    datos = float(input(f'{message[i]}'))
    perimetro += datos
print(f'{message[3]}',Perimetro_Triangle(datos))

# Coordenadas Temporales
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))