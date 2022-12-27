#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 10:18:34 2021

@author: Bard
"""
import random
n=100000
begge=0
p1=0
for i in range(n): #Jo høyre n, jo mer nøyaktig, antall ganger vi vil simulere handlingen
    allemennesker=list(range(0,33)) #Liste med alle utfall
    random.shuffle(allemennesker)   #Blander så det blir tilfeldig
    trekkmenneske=[]                #Liste med hvem som har blitt trukket
    for trekk in range(0,10):       #Antall ganger vi skal trekke
        trekkmenneske.append(allemennesker.pop(0)) #Fjerner den som er trukket og putter i egen liste
    if (1 in trekkmenneske) and (2 in trekkmenneske):   #Sjekker om vi er en av de i trukket lista
        begge+=1
    elif (1 in trekkmenneske):
        p1+=1
print('Sansynlighet for at begge vinner er {0}%, for at 1 vinner er {1}%, og for at en av oss skal vinne er {2}%'.format(begge/n*100, p1/n*100, (p1*2)/n*100))
