# -*- coding: utf-8 -*-
"""
Editor de Spyder

Este es un archivo temporal.
"""

import datetime

ahora = datetime.datetime.now()
print(ahora)

print(type(ahora))

'''
fecha
este debe estar separada por '/'
o cualquier otroo caravter que quiere que los separe
poner esos depues de los comando que se muetran:
%d para DIA
%m para MES
%Y para YEAR

HORA
cade reasaltar que estos deben estar separados por ':'
o cualquier otro caracter que quiera que separes estos
poner despues delos comandos daos:
%H HOra
%M MINUtos
%S SEGundos

'''
    
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))
