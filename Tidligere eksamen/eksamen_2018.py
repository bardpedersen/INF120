#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 10:27:32 2021

@author: Bard
"""
#%% Oppgave 1
print('Cartoon'.replace('o', 'a'))
print(int(10.0 / int('2'))) 
print('*'.join(['student', 'at', 'NMBU'.lower()]))
a='Berlin: 18.4 C at 4 pm'
print(a.split())
print('The person is {0:.2f} m tall, weighs {2} kg and has shoe size {1}.'.format(1.5999, 40, 45))
b='Glasgow: 22.2 C at 4 pm' 
print(b.split(':')[1].split()[0])


#%% Oppgave2
a=7
b=-3

if a > 0 and b < 0:
    print('True')
if b > 0 or a < 0:
    print('True')
if a != 3 and b <= -1:
    print('True')
if a > 1 or not(b != 1):
    print('True')
if not(a < 0 and not(b >= -3)):
   print('True')
   
   
#%% Oppgave3
colours = ['green', 'red', 'blue']
numbers = [7, 8, 9]

for i in range(len(colours)):
    for j in range(len(numbers)):
        print(colours[i],'-',numbers[j])
        
        
#%% Oppgave 4
fridager = {'17. mai':'Nasjonaldagen', '24. desember':'Julafaften', '31. desember':'Nyttårsaften'}
a=input('Angi dato: ')

if a in fridager.keys():
    print('Dette er {0}.'.format(fridager[a]))
else:
    print('Denne fridagen finnes ikke i vår database.')
    
    
#%% Oppgave 5
def integer_adder(liste):
    c=0
    for i in range(len(liste)):
        try :
            c+= liste[i]**2
        except: 
            ValueError
            continue 
    return(c)
    
if __name__ == '__main__':
    data = [2, 'NaN', 5, 9, 'NaN', 'NaN', 3]
    print(integer_adder(data))


#%% Oppgave 6
group_1=['Italy', 'France','Germany', 'UK', 'Spain' ]
group_2=['Ireland', 'Norway','Norway', 'Ireland', 'Italy' ]
group_3=['Ireland', 'Italy','Norway', 'Portugal', 'Portugal' ]
group_4=['Denmark', 'Belgium','Austria', 'Portugal', 'UK' ]

print(set(group_1))
print(set(group_2) - set(group_1))
print(set(group_3) & set(group_4))
print(set(group_2) | set(group_3))


#%% Oppgave 7
import numpy as np

def calc_rmsep(value1,value2):
    e=0
    N=len(value1)
    for i in range(N):
        e +=(value1[i] - value2[i])**2
    RMSEP = np.sqrt(1/N * (e))
    return RMSEP

if __name__ == '__main__':
    originalValues = [4.5,3.3,9.2]
    predictedValues =[4.5,3.7,9.6]
    print(calc_rmsep(originalValues,predictedValues))


#%% Oppgave 8
import random 
n=10000
m=0
for exp in range(n):
    allBalls=list(range(1,49))
    random.shuffle(allBalls)
    drawnBalls=[]
    for draw in range(0,6):
        drawnBalls.append(allBalls.pop(0)) 
    if (2 in drawnBalls) and (48 in drawnBalls):
        m+=1
print("The probability of balls 2 and 48 being among 6 drawn balls out of 48 is approximately {0}".format(m/n))


#%% Oppgave 9
a = np.array([[3,1,5],[4,4,8],[9,9,6]])
b = np.array([[1,1,1],[2,2,2],[3,3,3]])

print(a+b)
print(np.vstack((b, a)))
print(a/2)
b[-1, 1] = 99
print(b)


#%% Oppgave 10
print([(x + y) * z for x, y, z in [[3, 4, 5], [1, 2, 3], [2, 2, 2]]])
print([a + b for a, b in zip(['a', 'b', 'c'], ['3', '2', '1'])])
print([word[1:-1:2] for word in ['Norway', 'Sweden', 'Denmark'] if 'r' in word])
print([2*x for x in range(10) if divmod(x, 2)[1] == 0])


#%% Oppgave 11

class PizzaOrder:
    def __init__(self, costumer):
        self.costumer = costumer
        self.choice = None
        self.menu = ['Pizza A', 'Pizza B', 'Pizza C']
        print('Welcome {0}.'.format(self.costumer))
        
    def showMenu(self):
        print('{0}, please choose your pizza:'.format(self.costumer))
        for ind, item in enumerate(self.menu):
            print('({0}) -{1}'.format(ind + 1, item))

    def selectPizza(self, choice):
        self.choice = choice
        if choice not in self.menu:
            print("Sorry, this one is not on the list.")
            self.choice = None
        else:
            print("Excellent choice, {0}!".format(self.costumer))
                
    def takePizza(self):
        if self.choice == None:
            print("Please make a selection first!")
        else:
            print("Thank you {0}.We hope you will enjoy {1}.".format(self.costumer, self.choice))

