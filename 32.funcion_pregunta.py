# -*- coding: utf-8 -*-
"""
Created on Fri May 15 20:09:34 2020

@author: DELL.E5430.SSD
"""

import datetime

def si_o_no(cadena):
    respuesta = ''
    while not respuesta in si or respuesta in no:
        print(cadena)
        respuesta = input('Respuesta.- ')
        if(respuesta not in si or respuesta not in no):
            print('Por favor ingrese una de las siguientes opciones:')
            print(f'SI --> {si}\nNO --> {no}')
    return respuesta

# Programa Principal
ahora = datetime.datetime.now()

si = ['si','SI','Si','s']
no = ['no','NO','No','n']
texto = input('Haga una pregunta: ')
si_o_no(texto)
print()
print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))