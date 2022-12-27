#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 13:23:37 2021

@author: Bard
"""
"""
#%% Oppgave 1
print('The problem is not the problem'[4:11])
print('The problem is you attitude about the problem'.split()) 
print('Do or do not'.find('do'))
print('There is no try'.upper())
print('My favourite courses: {2}, {0}, {3}, {1}'.format('fys230', 'inf120', 'math112', 'stat100'))


#%% Oppgave 2
x=10
y=-1

if x < 0 and y > 0:
    print('True1')
if x > 0 or y < 0:
    print('True2')
if x >= 4 or y != -2:
    print('True3')
if not(x < 0) and y >= -2:
    print('True4')
if not(x < 10 or y < 1):
    print('True5')
    
    
#%% Oppgave 3
def alder(grense1, grense2):
    try:
        alder=float(input('Skriv inn din alder '))
    except ValueError:
        raise ValueError ('Du må skrive inn et tall')
    if alder >= grense1:
        print('Du er velkommen til å kjøre')
    elif alder > grense2 and alder < grense1:
        print('Du kan øvelseskjøre')
    else:
        print('Du må vente noen år til')
    
if __name__ == '__main__':
    alder(18,16)
   
    
#%% Oppgave 4
l1 = ['banan', 'eple', 'appelsin', 'eple', 'kiwi']
l2 = ['eple', 'fersken', 'drue', 'fersken', 'appelsin']
print(set(l1)) 
print(set(l2) -set(l1))
print(set(l2) & set(l1))
print(set(l2) |set(l1))


#%% Oppgave 5
dict = {'Temperature': 15.0, 'Humidity': 68, 'Precipitation':  3}
print('dict[’Humidity’]:', dict['Humidity'])
"print(dict[68])"
dict['Location'] = 'Ås'
dict['Temperature'] = 21
"""

#%% Oppgave 6
import numpy as np
a=np.array([[1,2,3,4,5,6,7],
           [8,9,10,11,12,13,14],
           [15,16,17,18,19,20,21],
           [22,23,24,25,26,27,28],
           [29,30,31,32,33,34,35],
           [36,37,38,39,40,41,42],
           [43,44,45,46,47,48,49]])

print(a[4:6,4:6])
print('-')
print(a[1:10:3,5:])
"""
C= np.array([[241, -14, 88],[-30, 127, 39],[-22, -51, -7],[155, 61, 172]])
C[C>0] = 0

D=np.linspace(1, 5, 9)

E=np.arange(0, 16, 3)


#%% Oppgave 7
import random 
n=int(input('hvor mange ganger?'))
ndice=5
nequal=3
m=0
for i in range(n):
    throw=[]
    for j in range(ndice):
        throw.append(random.randint(1, 6))
    for k in range(1,7):
        if throw.count(k)==nequal:
            m+=1
p=float(m)/n
print('probability:', p)


#%% Oppgave 8

import matplotlib.pyplot as plt
data = np.loadtxt('temp_aas.dat', comments='#')
plt.plot(data[:,0],data[:,1],'--')
plt.plot(data[:,0],data[:,2],'-')
m1=np.mean(data[:,1])
m2=np.mean(data[:,2])
plt.xlabel('Dag i mars')
plt.ylabel('Temperatur i C')
plt.title('Temperatur i ås i 2011 og 2012')
plt.legend(['mean 2012:{0:.2f}'.format(m1),'mean 2011:{0:.2f}'.format(m2)])
plt.show


#%% Oppgave 9
class Dog:
    def __init__(self,name):
        self.name=name
        self.tricks = []
    def addtrick(self,trick):
        self.tricks.append(trick)


#%% Oppgave 10
def contains(sequence, subsequence):
    if len(sequence) < len(subsequence):
        return False
    if sequence [: len(subsequence)] == subsequence:
        return True
    return contains (sequence[1:],subsequence)

"""
