#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  10 10:07:40 2021
"""
__author__ = "Bård Pedersen"

__email__ = "bard.tollef.pedersen@nmbu.no"

"""
Del 1
"""
import pandas as pd              #impoterer panda og matlpotlib.pyplor
import matplotlib.pyplot as plt

def csv_til_liste(filnavn):         #Definerer funksjonen
    occuDF = pd.read_csv(filnavn)   #Leser en csv fil og retuner det som en DataFrame
    occuList=occuDF.values.tolist() #Gjør om DataFrame til en Nested Liste
    return occuDF, occuList         #Returnere verdiene

"""
Del 2
"""
from datetime import datetime   #impoterer datetime og numpy
import numpy as np

def tid_siden_midnatt(liste):   #Definerer funskjonen med 1 variabel
    Dato=list()                 #Lager en ny liste
    for i in range(len(liste)):  #Gjør så den bruker alle radene 
        Dato.append(liste[i][1]) #Fyller listen inn med kun tid og dato kolonnen
        
    dato_int_sek=list()         #Definere ny liste
    for i in range(len(Dato)): 
        dt=datetime.strptime(Dato[i],"%Y-%m-%d %H:%M:%S") #Gjør om str til dato og tid
        dato_int_sek.append(dt.year*0 + dt.month* 0 +dt.day * 00 + dt.hour*60*60  +  dt.minute*60 + dt.second) #Gjør om dato og tid til sekunder
    
    tid_s_midnatt_min=list()
    tid_s_midnatt_timer=list()  #Definere nye lister
    for i in range(len(dato_int_sek)):  #kjører en gang for alle tidene
        tid_s_midnatt_timer.append(int((dato_int_sek[i])/(60*60) - 000000)) #Gjør om til heltall og minutter fra midnatt
        tid_s_midnatt_min.append(int((dato_int_sek[i])/(60) - 000000)) #Gjør om til heltall og timer fra midnatt
    
    return tid_s_midnatt_min, tid_s_midnatt_timer #Retunerer timene og minuttene

"""
Del 3
"""
def hent_kolonner(dataframe, kolonne1, kolonne2, lagPlott = True):  #Definere funksjonen med variablene 
    x=dataframe[[kolonne1]].to_numpy() #Definere en x-akse, og gjør det til array
    y=dataframe[[kolonne2]].to_numpy() #Definere en y-akse, og gjør det til array
    color=list()      #Definere en ny liste
    for i in range(len(dataframe)): #Antall ganger den skal kjøre
        color.append(i)#Dette gjør at vi får en liste med tall fra 0 til antall rader i occuDF-1
    fig=0
    if lagPlott == True:    #Så lenge lagPlott = True så skal den plotte grafen.
        fig=plt.figure(2)   #Definere til plot nr2
        plt.scatter(x, y, c=color)  #Velger x og y akse samt farge
        plt.xlabel(kolonne1)    #Leger på tekst på x og y aksene
        plt.ylabel(kolonne2)
        plt.colorbar()  #Gir farger en verdi man kan se
    return fig, x, y          #Printer ut graf, og array med de froskjellige kolonnene

"""
Anvender funskjonene
"""
if __name__ == "__main__":
    
    occuDF, occuList = csv_til_liste("occupancy.csv")   #Legger inn filnavnet
    occuDF.boxplot(column = ['Temperature'], by = 'Occupancy') #kode for å boxplotte
    plt.suptitle('')    #Fjerner overskriften