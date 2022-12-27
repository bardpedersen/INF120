#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 19 11:37:20 2021

@author: Bard
"""
#%% Oppgave 1
print('A list of cities: {2}, {1}, {3}, {0}'.format('Quito','Rio', 'Oslo', 'Perth'))
print('They call it a Royale with cheese.'[-7:-1])
print('John' in 'John is a great bloke.')
print('Ice Cream'.upper())
print(int(6/3))


#%% Oppgave 2
x = 4
y = -2
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
def listepluss(a,b,c):
    liste=[]
    for i, num in enumerate(a):
        liste.append(a[i]+b[i]+c[i])
    return liste

if __name__ == '__main__':
    a = [1, 2, 3, 4]
    b = [5, 6, 7, 8]
    c = [2, 1, 4, 3]
    print(listepluss(a,b,c))
    print([val[0]+val[1]+val[2] for val in zip(a, b, c)])
    
    
#%% Oppgave 4
c = ['Larvik', 'Oslo', 'Bodø', 'Larvik', 'Oslo']
d = ['Larvik', 'Arendal', 'Hamar', 'Arendal']
print(set(c)) 
print(set(c) | set(d))
print(set(c) -set(d))
print(set(c) & set(d))


#%% Oppgave 5
def readFile(fileName):
    infile = open(fileName, 'r')
    firstLine = infile.readline()
    rows = infile.readlines()
    infile.close()
    info = {}
    for row in rows:
        cols = row.split(',')
        info[cols[0]] = int(cols[2])
    return(info)
#data = readFile('data.txt')


#%% Oppgave 6
import numpy as np
a=np.array([[0,1,2,3,4,5],
           [10,11,12,13,14, 15],
           [20, 21,22,23,24,25],
           [30,31,32,33,34,35],
           [40,41,42,43,44,45],
           [50,51, 52, 53, 54, 55]])
print(a[3,:-1])  #[bort, ned] [fraogmed:tilmenikkemed, fraogmed:tilmenikkemed] [start::skritt, start::skritt]
print(a[2:5,1:4])
print(a[:,1::2])

b= [[8, 7], [2, 8], [4, 5], [8, 1]] 
B = np.vstack(b)
print(B)
C = np.array([[241, -14, 88],[-30, 127, 39],[-22, -51, -7],[155, 61, 172]])
print( C[C< 0] == 0)
'skal printe ut:  [[241,   0,  88],[  0, 127,  39],[  0,   0,   0],[155,  61, 172]]'
print(np.linspace(1, 2, 5))
print(np.arange(0, 11, 3))


#%% Oppgave 7
import numpy as np
N = 10000
M = 0
for n in range(0, N):
    throws = np.random.random_integers(1, 6, 10)
    twosCount= list(throws).count(2)
    if twosCount == 2 and 5 not in throws:
        M += 1
        
probability = M/N
print("""Based on {0} simulations, the chance ofgetting exactly two times two eyes and  not5 eyes from 10 throws is about: {1}""".format(N, probability))


#%% Oppgave 8 
print([2 * x for x in range(5)])
print([x + y for x, y in zip([1, 2, 3], [4, 5, 6])])
print([k[1:-1] for k in ['story', 'light', 'sun'] if k[0] == 's'])


#%% Oppgave 9 
def listExtractor(someList, ind):
    try:
        value = someList[ind]
        print('Element at index {0} has value {1} and is a {2}'.format(ind, value, type(value)))
    except:
        print('Need an index between 0 and {0} but got {1}'.format(len(someList)-1, ind))
     
if __name__ == '__main__':
    a = [99, 'Peter', [5, 12, 1], 1.7]
    listExtractor(a,0)
    listExtractor(a,1)
    listExtractor(a,2)
    listExtractor(a,3)
    listExtractor(a,4)


#%% Oppgave 10
import math
class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
        self.s=None
        self.area=None
        
    def computeArea(self):
        self.s=0.5*(self.a+self.b+self.c)
        self.area=math.sqrt(self.s*(self.s-self.a)*(self.s-self.b)*(self.s-self.c))
        return self.area
    
    def printResult(self):
        if self.area == None:
            print('Area not computed')
        else:
            print('Area = {0:.2f} and s = {1} using Herons formula.'.format(self.area, self.s))

            