# -*- coding: utf-8 -*-
"""
Created on Sat May 23 01:03:25 2020

@author: DELL.E5430.SSD
"""

import pandas as pd

df = pd.DataFrame({
    'Name':['Jean Rada','Lennys Ramirez','Nayla Magaly'],
    'Age':[16,15,15],
    'Sex':['Masculino','Femenino','Femenino']
    })
# Creamos el dataframe
print(df)
print()

# trabajaremos con series/SERIES ES OLO UNA COLUMNA
#sseries
print(df['Name'])
print()
print(df['Age'])
print()
print(df['Sex'])
print()

# COMO CREAR UNA SERIE

serie_1 = pd.Series([2000,2001,2002], name='Year')
print(serie_1)

print()

#funciones max, min
print(df['Age'].max())
print(serie_1.max())
#tambien se pude usar min


print()

#datos estadisticos/numericos

print(df.describe())
print()
print(serie_1.describe())
