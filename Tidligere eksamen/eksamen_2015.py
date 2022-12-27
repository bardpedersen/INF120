#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 12:58:37 2021

@author: Bard
"""
#%% Oppgave 1
print('Monday\nTuesday\nWednesday')
print('Monday,Tuesday,Wednesday'.split(','))
print(float(7))
print('4' in '37.5 degrees')
print(sum([1,2,3]))


#%% Oppgave 2
x = 5.0
y  = -1.0
if x <= 2 and y < -3:
    print('True1')
if x  < 0 or y <0:
    print('True2')
if x  > 5 and y< 1:
    print('True3')
if not (x <8 and y < -2):
    print('True4')
if x > -6.0 and y > -4.:
    print('True5')
    
    
#%% Oppgave 3
import random
def trek_tall(liste):
    tall = random.choice(liste)
    liste.remove(tall)
    return tall, liste


#%% Oppgave 4
"""
number = random.randint(1,20)
attempts = 0
guess = 0
name = input('What is your name ?')
print('Hello', name,' I am thinking of a number between 1 and 20:')
while guess != number:
    guess = int(input('Take a guess :'))
    attempts += 1
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        print('Good job ! You guessed my number in %d attempts' %attempts)
"""          
                
#%% Oppgave 4
def read_data(filename):
    infile = open(filename, 'r')
    befolkning= {}
    infile.readline()
    for line in infile.readlines():
        land, folk= line.split()
        folk = float(folk)
        befolkning[land] = folk
    return befolkning

                
#%% oppgave 5  
import numpy as np              
print(np.arange(1,9,2)) 
print(np.linspace(1,10,10))
A = np.array([[0,   1,  2,  3],[4,   5,  6,  7],[8,   9, 10, 11],[12, 13, 14, 15],[16, 17, 18, 19]])
print(A[2,:-1])
print(A[::2,3])
c = np.array([ 11., 12., -4., 14., 15., 16., -14., -6.])
c[c<0]=0
            
    
#%% Oppgave 6
N=10000
n=10
nkonge=2
m=0

for i in range(N):
    kortstokk=[v for v in range(1,14) for i in range(4)] 
    kort=[]
    for j in range(n):
        index = random.randint(0, len(kortstokk)-1)
        kor = kortstokk.pop(index)
        kort.append(kor)
    if kort.count(13) == nkonge:
        m +=1
print(float(m)/N)


#%% Oppgave 7
import numpy as np
import matplotlib.pyplot as plt
t = np.linspace(0, 7., 50)
y1 = np.sin(t)*np.cos(t)
y2 = np.cos(t)*np.cos(t)
y3 = np.sin(t)
y4 = np.cos(t)

plt.figure()
plt.subplot(2, 1, 1)
plt.plot(t, y1, 'r-')
plt.plot(t,y3,'bo')
plt.xlabel('t')
plt.ylabel('y')
plt.axis([t[0], t[-1], min(y3)-0.05, max(y3)+0.05])
plt.legend(['sin(t)*cos(t)','sin(t)'])

plt.subplot(2, 1, 2)
plt.plot(t, y2, 'b-')
plt.plot(t, y4, 'ro')
plt.xlabel('t')
plt.ylabel('y')
plt.axis([t[0], t[-1], min(y4)-0.05, max(y4)+0.05])
plt.legend(['cos(t)*cos(t)','cos(t)'])
plt.show()