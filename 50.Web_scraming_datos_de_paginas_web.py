# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:24:13 2020

@author: DELL.E5430.SSD
"""


from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://resultados.as.com/resultados/futbol/primera/clasificacion/?omnil=src-sab'
# Descargaremos la pagina 
page = requests.get(url)
# tranformamos a beautiful para poder manipular los datos
soup = BeautifulSoup(page.content, 'html.parser')

# equipos
# hasta aqui ya tenemos los datos de los nokmbres pero con las clases
eq = soup.find_all('span', class_="nombre-equipo")

c = 0
# obtengamos los datos solo nom,bres
equipo = list()
for i in eq:
    if c < 10:
        equipo.append(i.text)
    c += 1
    
print(equipo)


# resultado

pt = soup.find_all('td', class_="destacado")
cont = 0
puntos = list()
for i in pt:
    if cont < 10:
        puntos.append(i.text)
    cont += 1
    
print(puntos)
'''
aca creamos un DataFrame que es como un tabla donde guardamos
los datos, el index es para poner el numero(indice)
'''

df = pd.DataFrame({'Nombre:':equipo,'Puntos:':puntos}, index = list(range(1,11)))

print(df)



