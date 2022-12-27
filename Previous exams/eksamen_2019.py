#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 12:23:57 2021

@author: Bard
"""
#%% Oppgave 1
print(27==42)
print('Pizza with ham and cheese.'.replace('ham', 'pepperoni'))
print('The best mirror is an old friend.'.split()[-3:-1])
print('house'.upper() in 'The house is on fire')
print('Always remember: it is never too late'.split(':')[0].split()[0][0:-3])


#%% Oppgave 2 
print([e + f for e, f in [[4,2],[4,3]]])
print([sum([n,m,o]) for n, m, o in zip([2,1,4],[0,3,4],[0,6,2])])
print([name[-2:] for name in ['ida', 'Olav', 'Kritsin'] if 'a' not in name])
print([z+z*z for z in range(1,6,2)])


#%% Oppgave 3
def multiplayer(x,y,z):
    return x*y*z

print(multiplayer(1,5,5))


#%% Oppgave 4
def adder(x, z=2):
   return x + z

print(adder(3))


#%% Oppgave 5
names = ['Jensen', 'Olsen', 'Svendson']
def title_adder(names):
    title_list=[]
    for i, name in enumerate(names):
        title_list.append('Dr.'+str(name))
    return title_list


def title_adder2(names):
    return['Dr.' + name for name in names]
    
print(title_adder(names))
print(title_adder2(names))


#%% Oppgave 6
dict = {}
for i in range(5):
    dict[i+1]=((i+1)**2)


#%% Oppgave 7 
myList = [4,'The', 3, 'dog', 'ate', 1, 18, 'my', 'homework']
def extractor(liste):
    intList=[]
    strList = []
    for element in liste:
        print(element)
        try: 
            intList.append(int(element))
        except ValueError:
            strList.append(str(element))
    return strList
            
res = extractor(myList)

def extractor2(liste):
    strList = []
    for element in liste:
        try:
            int(element)
        except:
            strList.append(element)
    return strList
            

#%% Oppgave 8
def max_of_three(x,y,z):
    liste = [x,y,z]
    liste=sorted(liste)
    return liste[len(liste)-1]
print(max_of_three(1,5,11))


#%% Oppgave 9
import numpy as np
def stand_dev(liste):
    xsum=0
    n=len(liste)
    m=sum(liste)/n
    for x, num in enumerate(liste):
        delsum=(num-m)**2
        xsum += delsum
    xsum = np.sqrt(1/n*xsum)
    return xsum

values = [3,6,9]
print(stand_dev(values))


#%%% Oppgave 10
import random 
n=10000
m=2
grønn=0
balls = ['red', 'red', 'black', 'black', 'green', 'green']
for i in range(n):
    baregrønn=0
    for j in range(m):
        hat1=random.choice(balls)
        hat2=random.choice(balls)
        if hat1 == 'green' and hat2 == 'green':
            baregrønn += 1
    if baregrønn == 2:
        grønn+=1
print(grønn/n)

N = 10000
M = 0
for exp in range(N):
    hat_1 = []
    hat_2 = []
    colours = ['red', 'black', 'green']
    for colour in colours:
        for ball in range(2):
            hat_1.append(colour)
            hat_2.append(colour)
            random.shuffle(hat_1)
            random.shuffle(hat_2)
            drawnBalls = []
    for draw in range(2):
        drawnBalls.append(hat_1.pop(0))
        drawnBalls.append(hat_2.pop(0))
    if drawnBalls.count('green') == 4:
        M += 1
prob = M/N 
print(prob)
#%%% Oppgave 11
"""
import pandas as pd
def get_info(file,  Continent=None, Coastline='yes', Desert='yes'):
    with open(file) as csv_file:
        result=[]
        rows = [line.split(";") for line in csv_file]
        for row in rows :
            ro = [line.strip().strip('"') for line in row]
            result.append(ro)
    head=result[0]
    del result[0]
    df = pd.DataFrame(result, columns=head)
    return df[(df.Continent == Continent) & (df.Coastline == Coastline) & (df.Desert == Desert)][['Country', 'Population[million]']]

print(get_info('Country.csv', Continent='Asia', Coastline='yes', Desert='yes'))
"""
#%%% Oppgave 12
class Murstein:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.diag = None
        
    def computeDiagonal(self):
        self.diag =np.sqrt(self.a**2 + self.b**2 + self.c**2 )
        return self.diag
    
    def printResult(self):
        if self.diag == None :
            print('Can´t compute, need some input')
        else:
            print('Length of diagnol is ', self.diag)
