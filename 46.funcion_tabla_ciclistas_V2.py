# -*- coding: utf-8 -*-
"""
Created on Mon May 18 23:54:34 2020

@author: DELL.E5430.SSD
"""


import numpy as np
import datetime
import time

def NamesCyclists(QuantifyCyclists):
    ListNamesCyclists = []
    for i in range(QuantifyCyclists):
        NameCyclist = input(f'Ingrede el nombre del {i+1}, ciclista: ')
        ListNamesCyclists.append(NameCyclist)
    return ListNamesCyclists

def StageDatesTimes(ListNamesCyclists,Stages):
    DatesTimes = np.arange(len(ListNamesCyclists)*Stages).reshape(len(ListNamesCyclists),Stages)
    for i in range(len(ListNamesCyclists)):
        for j in range(Stages):
            print('\t\t--------------------------------')
            print('Nombre',ListNamesCyclists[i])
            print('Etapa:',j+1)
            StageTime = float(input('Tiempo: '))
            DatesTimes[i,j] = StageTime
    return DatesTimes

def OptionMenu():
    print('\n\n')
    Option = None
    print(ahora.strftime('%d/%m/%Y  %H:%M:%S'))
    while Option not in KeysOptions:
        Option = None
        print('\n\n\tMENU DE OPCIONES')
        for Keys in OPTION:
            print(Keys+')',OPTION[Keys])
        if Option == None:
            Option = input('Digite una opcion: ')
        else: print('Por favor ingrese una opcion valida.')
    return Option

def TotalWinner(NamesCyclists,DatesTimes):
    SumDatesTimesColumns = DatesTimes.sum(axis=1)
    MinDateTimeColumn = SumDatesTimesColumns.min()
    for i in range(len(NamesCyclists)):
        if SumDatesTimesColumns[i] == MinDateTimeColumn:
            print('El ciclista',NamesCyclists[i]+', es el ganador por mejor tiempo total.')
            print('Tiempos de sus etapas',DatesTimes[i])
            print('Tiempo total:',round(SumDatesTimesColumns[i],2))
    return

def GetNumber(DatesTimes):
    Stage = None
    while Stage not in range(len(DatesTimes[0])):
        Stage = None
        print(f'La carrera cuenta con {len(DatesTimes[0])}, etapas.')
        if Stage == None:
            Stage = int(input('Digite una etapa: '))
        else:
            print('Por favor ingrese una opcion valida.')
    return Stage-1

def StageWinner(NamesCyclists,DatesTimes,Stage):
    RowDates = [DatesTimes[x, Stage-1] for x in range(len(DatesTimes))]
    MinTime = min(RowDates)
    for i in range(len(RowDates)):
        if RowDates[i] == MinTime:
            print(f'El ganador de etapa {Stage+1} es:',NamesCyclists[i])
            print('Tiempo:',MinTime)
            return
        
def WinnerStages(NamesCyclists,DatesTimes):
    for i in range(len(DatesTimes)):
        ColumnDatesTimes = [DatesTimes[i,x] for x in range(len(DatesTimes[0]))]
        MinTime = min(ColumnDatesTimes)
        for j in range(len(ColumnDatesTimes)):
            if ColumnDatesTimes[j] == MinTime:
                print(f'Ganador de la {i+1} etapa.')
                print('Nombre:',NamesCyclists[j])
                print('Tiempo:',MinTime)
    return

# Programa Principal
ahora = datetime.datetime.now()
'''
'Names = ['Pere Porcar','Joan Beltran','Lledo Fabra']
Times = np.array([[10092.0,12473.1,13732.3,10232.1,10332.3],
                  [11726.2,11161.2,12272.1,11292.0,12534.0],
                  [10193.4,10292.1,11712.9,10133.4,11632.0]])
'''
QuantifyParticipants = int(input('Ingrese la cantidad de corredores: '))
DateNames = NamesCyclists(QuantifyParticipants)
AddStage = int(input('Ingrese la cantidad de etapas: '))
DataTime = StageDatesTimes(DateNames, AddStage)
OPTION = {'1':'Ganador, menor tiempo en las % etapas.',
          '2':'Ganador Etapa..',
          '3':'Ganador de cada una de las etapas.',
          '4':'Salir'
          }
KeysOptions = OPTION.keys()
while True:
    OptionRequest = OptionMenu()
    if(OptionRequest == '1'):
        #print('\n'+OPTION[OptionRequest])
        print('Opcion requerida:',OptionRequest)
        TotalWinner(DateNames,DataTime)
    if(OptionRequest == '2'):
        print('Opcion requerida:',OptionRequest)
        Stage = GetNumber(DataTime)
        StageWinner(DateNames,DataTime,Stage)
    if(OptionRequest == '3'):
        print('Opcion requerida',OptionRequest)
        WinnerStages(DateNames, DataTime)
    if(OptionRequest == '4'):
        print('Opcion requerida:',OptionRequest)
        print('Lamentamos verlo irse.')
        break
    time.sleep(5)