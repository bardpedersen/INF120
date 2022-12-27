#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 20 13:33:04 2021

@author: Bard
"""
#%% Oppgave 1
print('s = %.2f degrees' % 5.66667)
print('hello\nworld')
print(int(5.667))
#print(float('hello'))
print(eval('3+5'))


#%% Oppgave 2
x = -5.0  
y  = 4.0
if x <= 2 and y < -3:
    print('True1')
if x  < 0 or y <0:
    print('True2')
if x  < 5 and y< 1:
    print('True3')
if not (x <2 or y < -2):
    print('True4')
if x > -6.0 and y > -4:
    print('True5')
    
    
#%% Oppgave 3
def f(x):
    if x <= -5:
        return 3-x
    elif x < 1:
        return 2-x
    elif x == 1:
        return 10
    elif x <= 10:
        return x+5
    else:
        return x-5
    
    
#%% Oppgave 4
def read_data(filename):
    infile = open(filename, 'r')
    tettheter= {}
    infile.readline()
    for line in infile.readlines():
        matereal, tetthet= line.split()
        tetthet = float(tetthet)
        tettheter[matereal] = tetthet
    return tettheter


#%% Oppgave 5
lst = [10, 20, 30, 40, 50]
lst2 = [5,25,10,50,65]
lst3=[]
for i, num in enumerate(lst):
    if lst[i] > lst2[i]:
        lst3.append(lst[i])
    else:
        lst3.append(lst2[i])
print(lst3)

print([max(k,l) for k,l in zip(lst,lst2)])


#%% Oppgave 6
import numpy as np
a = np.linspace(11,30,20)
b = a.reshape(5,4)

A =np.array([[0,   1,  2,  3],[4,   5,  6,  7],[8,   9, 10, 11],[12, 13, 14, 15],[16, 17, 18, 19]])
print(A[:,:-2])
print(A[::2,1:3])

c = np.array([ 11., 12., -4., 14., 15., 16., -14., -6., 19., 20.])
c[c<0]=10.


#%% oppgave 7
"""
import random
attempts=0
guess=0
number=random.randint(0,6) +random.randint(0,6) 
while guess != number:
    try:
        guess = int(input('Take a guess :'))
    except ValueError:
        raise ValueError (u'Du må skrive et heltall') 
    attempts += 1
    if guess < number:
        print('Your guess is too low')
    elif guess > number:
        print('Your guess is too high')
    else:
        print('Good job ! You guessed my number in %d attempts' %attempts)
"""

#%% Oppgave 8
"""
import matplotlib.pyplot as plt
data = np.loadtxt('co2.txt', comments = '#')
plt.plot(data[5::12,2],data[5::12,4],'r.')
plt.plot(data[9::12,2],data[9::12,4],'b.')
plt.plot(data[:,2],data[:,5],'g')

plt.legend(['June','October','Mean annual'])
plt.xlabel('year')
plt.ylabel('CO2')
plt.title('CO2 concentration over Mauna Kea')
plt.show()
"""

#%% Oppgave 9
class Gravity:
    def __init__(self, m1, m2, x1, x2):
        self.m1=m1
        self.m2=m2
        self.x1=x1
        self.x2=x2
        self.g=6.6742*(10**(-11))
        
    def distace(self):
        self.r = self.x1-self.x2
        return self.r
        
    def force(self):
        self.fors = (self.g*self.m1*self.m2)/(self.r**2)
        return self.fors


#%% Oppgave10
def listsum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
         return numList[0]+listsum(numList[1:])
    
if __name__ == '__main__':
    lit1=[1, 2,  3, 4, 5]
    print(listsum(lit1))
    
