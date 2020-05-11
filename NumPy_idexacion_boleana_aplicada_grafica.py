# -*- coding: utf-8 -*-
"""
Created on Sun May 10 21:20:08 2020

@author: DELL.E5430.SSD
"""

import numpy as np
import matplotlib.pyplot as plt
def mandelbrot(h,w, maxit=20 ):
    #Devuelve una imagen del fractal de tamaño de la funcion Mandelbrot h,w
    y, x = np.ogrid[ -1.4:1.4:h*1j, -2:0.8:w*1j ]
    c = x+y*1j
    z = c
    divtime = maxit + np.zeros(z.shape, dtype=int)
    for i in range(maxit):
        z = z**2+c
        diverge = z*np.conj(z) > 2**2  #quien está divergiendo
        div_now = diverge & (divtime == maxit)  #quien está divergiendo no
        
        divtime[div_now] = i  #nota nueva
        z[diverge] = 2  #evite divergir también
    return divtime
plt.imshow(mandelbrot(400,400))