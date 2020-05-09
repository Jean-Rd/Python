# -*- coding: utf-8 -*-
"""
Created on Fri May  8 21:01:07 2020

@author LustrosoBurbuja
"""
import matplotlib.pyplot as plt
import numpy as np

# Creamos vector comn rango 'n'
n = 8
y = np.zeros(n)
# puntos en x
x_1 = np.linspace(0,10,n, endpoint = True)
x_2 = np.linspace(0,10,n, endpoint = False)
'''
---> Imprimimos cada punto que busco para x_1 ^ x_2 como no varia en y
en la primera grafica x esta en y = 0, es por eso que sumamos +0.5 para que suba y veamos
la diferencia que hay en que si se toma o no el ultimo punto
'''
plt.plot(x_1, y, 'o')
# [<matplotlib.lines.Line2D object at 0x...>]
'''
plt.plot(eje_x,eje_y,figura) --> esta fuincion es como un for toma todos los
valores que hay y lo grafica.
'''
plt.plot(x_2, y+0.5, 'o')
# [<matplotlib.lines.Line2D object at 0x...>]

plt.ylim([-0.5,1])
# Damos limite a el eje y de -0.5 a 1

plt.show()
# mostramos grafica