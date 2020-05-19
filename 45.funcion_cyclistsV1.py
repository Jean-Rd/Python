# -*- coding: utf-8 -*-
"""
Created on Sun May 17 22:29:36 2020

@author: DELL.E5430.SSD
"""

import numpy as np
import datetime

def TotalWinner(NamesCyclists,DatesTimes):
    SumDatesTimesRows = DatesTimes.sum(axis=1)
    #RounsSumDatesTimesRows = [round(SumDatesTimesRows[x], 2) for x in range(len(SumDatesTimesRows))]
    MinDateTimeRow = SumDatesTimesRows.min()
    for i in range(len(NamesCyclists)):
        if SumDatesTimesRows[i] == MinDateTimeRow:
            print('El ciclista',NamesCyclists[i]+', es el ganador por mejor tiempo total.')
            print('Tiempos de sus etapas',DatesTimes[i])
            print('Tiempo total:',round(SumDatesTimesRows[i],2))
            return

def GetNumber(DatesTimes):
    Stage = None
    while Stage not in range(len(DatesTimes[0])):
        print(f'La carrera cuenta con {len(DatesTimes[0])}, etapas.')
        if Stage == None:
            Stage = int(input('Digite una etapa: '))
        else:
            print('Por favor ingrese una opcion valida.')
    return Stage-1

def StageWinner(NamesCyclists,DatesTimes,Stage):
    RowDates = [DatesTimes[x, Stage] for x in range(len(DatesTimes))]
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

Names = ['Pere Porcar','Joan Beltran','Lledo Fabra']
Times = np.array([[10092.0,12473.1,13732.3,10232.1,10332.3],
                  [11726.2,11161.2,12272.1,11292.0,12534.0],
                  [10193.4,10292.1,11712.9,10133.4,11632.0]])

WinnerStages(Names, Times)
