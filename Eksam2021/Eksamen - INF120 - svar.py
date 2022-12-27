# -*- coding: utf-8 -*-
"""
Eksamensbesvarelse INF120

vår 2021
"""
#%% SVAR OPPGAVE -- 1 -- (12 poeng)

#a) (2 poeng)
if __name__ == '__main__': # Byttet ut ` ` med ' '
    pass

#b) (2 poeng)
alist = list(range(3,12,4)) #byttet ut ; med ;

#c) (2 poeng)
def f(x):               #La på :
    return 2*x - 3

#d) (2 poeng)
days=0 #legger på så koden skal funke videre uten syntaxerror
if days == 3: #Må ha ==
    pass

#e) (2 poeng)
acc = sum([4, 7, 9, 34]) #Må lage til liste, legge på []

#f) (2 poeng)
mengde=minutter=100 #legger på så koden skal funke videre uten syntaxerror
while mengde < 100 or minutter == 60: #Bytter ut 'eller' med 'or'
    pass


#%% SVAR OPPGAVE -- 2 -- (6 poeng)

#a) (1 poeng)
m=12 #int

#b) (1 poeng)
n = 45.2395 #float

#c) (1 poeng)
p=[1,3,5] #list

#d) (1 poeng)
q=1,3,5,'sju' #tuple

#e) (1 poeng)
r = ('en', 'to', 'tre') #tuple

#f) (1 poeng)
s={1,3,5} #set


#%% SVAR OPPGAVE -- 3 -- (16 poeng)

#a) (1 poeng)
a='NARIÑO;ALDANA;12;4.3;0;128'
print(a.split(';'))  #Må splitte orden ved ;

#b) (5 poeng)
a='NARIÑO;ALDANA;12;4.3;0;128'
b=[]
c=a.split(';')  #Splitter
for i, line in enumerate(c):
    try:
        b.append(float(c[i])) #Prøver å gjøre om til float, det som da er str, vil gå vidre til except
    except:
        b.append(c[i])  #her blir str lagt til i lista
print(b)

#c) (3 poeng)
a=[1/3, 5/7, 12.3]
print('{:.2f}'.format(a[0]),'{:.2f}'.format(a[1]),'{:.2f}'.format(a[2])) #Formaterer med 2 desimaler

#d) (3 poeng)
a={'fem': 5, 'to': 2, 'en': 1}
b = {}
for k, v in a.items(): #bytter plass på key og value for hver key
    b[v] = k
print(b)

#e) (4 poeng)
a=[[3, 6, 8], ['NOK', 'SEK', 'USD']]
res1, res2,res3 = map(list, zip(*a)) #Lager 3 lister med verdien og tilhørende valutaen
res1  = [str(res1[0]*2),res1[1]]    #ganger valutaen med 2 og gjør om til str
res2  = [str(res2[0]*2),res2[1]]
res3  = [str(res3[0]*2),res3[1]]
List=[(' '.join(res1)),(' '.join(res2)),(' '.join(res3))]   #Legger sammen de tre listene
print(List)
    

#%% SVAR OPPGAVE -- 4 -- (10 poeng)

#a) (5 poeng)
import numpy as np #Må importere for å få pi
def kjegle_volum(r,h):  #Definerer funskjonen
    V = (np.pi * r**2 * h) / 3  #Regner ut volum
    return V #returnerer V

#b) (5 poeng)
def sum_even(n):
    total=0
    for number in range(2, n+1): #for alle tallene opp til n
        if(number % 2 == 0):     #sjekker om det er partall
            print("{0}".format(number)) 
            total = total + number  #Dette legger sammen alle partall opp til n
    return total    #returnerer totalen, og 0 hvis n<2


#%% SVAR OPPGAVE -- 5 -- (6 poeng)

# Variant a er rasket, ettersom den regner ut alt med engang. 
# Numpy er laget for å regne med matriser, arrays eller store datasett, mens math er laget for enkle utregninger.


#%% SVAR OPPGAVE -- 6 -- (12 poeng)

#a) (6 poeng)
#a[4:6, 4:6], Fra og med rad 4, til rad 6, fra og med colonne 4, til 6
#[[69, 24]
#[87, 94]]

#b) (6 poeng)
#a[1:10:3, 5:], Fra og med rad 1, til rad 10, med steg på 3. Fra kolonne 5 og ut
#[[77, 39, 6, 67, 17]
#[24, 99, 61, 92, 14]
#[8, 49, 77, 90, 1]]


#%% SVAR OPPGAVE -- 7 -- (12 poeng)

class Rutenett: #Definere classen
    def __init__(self, rows, cols): #legger inn betingelser og start
        self.rows=rows #Gjør alle veridene tilhørige til den classen det gjeller for 
        self.cols=cols
        
    def draw(self): #legger inn en funsjon som printer rutenett
        self.x=[]
        for i in range(self.rows):  #For antall rader
            print('X'*self.cols)    #For antall colonner


#%% SVAR OPPGAVE -- 8 -- (16 poeng)

#a) (4 poeng)
import pandas as pd 
df = pd.read_csv('weight-height.csv') #Leser csv fil og gjør om til df

#b) (6 poeng)
df['Height'] = df['Height'] * 2.54          #Ganger alle ting i kolonen med tallet 
df['Weight'] = df['Weight'] * 0.453592

#c) (6 poeng)
df.boxplot(column = ['Height'], by = 'Gender')  #Lager et boxplot basert på høyde og kjønn


#%% SVAR OPPGAVE -- 9 -- (10 poeng)

#a) (2 poeng)
#temperatur > 20 and regn == 0  

#b) (2 poeng)
#fart < 50 and not bruker_mobil

#c) (3 poeng)
#inntekt < 150000 or utgift >= inntekt 

#d) (3 poeng)
#sum(passager_vekt_liste) < vekt_grense,  Kunne evt skrevet "not sum(passager_vekt_liste) > vekt_grense"









