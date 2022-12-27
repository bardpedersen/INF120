#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  8 15:14:12 2021

__author__ = "Bård Pedersen"
__email__ = "bard.tollef.pedersen@nmbu.no"

"""
rhList = [[4.276, 7.000], [4.000, 8.000], [3.771, 9.000], \
          [4.443, 3.142], [3.142, 6.284], [2.565, 9.425], [2.221, 12.566]]
resultList = []        #Definerer listen vi skal fylle inn

print('Radius   Høyde    Overflate  Volum')  #For kjønnhetens skyld 
from math import pi    #Må hente inn pi for å kunne bruke det
n=0                    #Definerer n

while n < len(rhList): #Den skal kjøre 1 gang for antall lister i rhlist
    whilelist = []     #Definerer en ny liste
    syl=rhList[n]      #Dette gjør at vi kan ta ut enkelt tall fra listen med lister
    r=syl[0]           #Definerer r og h
    h=syl[1]
    O = 2*pi*r**2+2*pi*r*h #Beregner ved formler
    V = pi*r**2*h
    n += 1             #Må øke med 1 for hvergang så den ikke går i det uendleige 
    a=print('{0:.3f},   {1:.3f},   {2:.3f},   {3:.3f}'.format(r,h,O,V)) #Printer med 3 desimaler
    whilelist.append(r)               #Dette gjør at man kan plotte enkelt tall i listen
    whilelist.append(h)    
    whilelist.append(O)
    whilelist.append(V)
    resultList.append(whilelist)      #Dette gjør at jeg kan plotte lister i en liste
print(resultList)
    
"""
Det vi ser på utregningene er at h bør vøre dobbelt så stor som r
for å få best mulig utnyutnyttelse av råmaterialene
"""