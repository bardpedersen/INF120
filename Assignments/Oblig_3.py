#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 12:46:45 2021

__author__ = "bård Pedersen"
__email__ = "bard.tollef.pedersen@nmbu.no"
"""
def loadBook(filename, textfra, texttil): #Laster inn boka og fjerner alt før textfra og etter texttil 
    with open(filename, 'r') as f:        #Laster inn boka for å lese
        lines = f.readlines()             #Deler den opp i linjer
        for i, line in enumerate(lines):   
            if textfra in line:           #Sjekker hvilken linje textfra er på
                break
        for j, line in enumerate(lines):
            if texttil in line:           #Sjekker hvilken linje texttil er på
                break
        trimmedText = lines[i+1:j]        #Returnere kun de linjene mellom textfra og texttil
    return trimmedText 

def removeNL_and_doLowerCase(trimmedText):
    newTextList = []    
    for element in trimmedText:
        newTextList.append(element.strip())       #Fjerner '/n'
    newTextList = list(filter(None, newTextList)) #Fjerner tommelinjer
    for i, line in enumerate(newTextList):
        newTextList[i]=newTextList[i].lower()     #Gjør om alle bokstaver til lowercase 
    return newTextList
    
def doubleDashToSpace(newTextList):
    for i, line in enumerate(newTextList):
       newTextList[i] = newTextList[i].replace("--", " ") #Fjerner '--' og setter inn ' '
    return newTextList

def deleteSpecChar(newTextList, remove):
    for i, line in enumerate(remove):    #Kjører en gang for hvert spesial tegn
        for j, line in enumerate(newTextList):      #Kjører for hver linje i filen
            newTextList[j] = newTextList[j].replace(remove[i], "")  #Fjerner spesialtegn
    return newTextList

def splitter(newTextList):
    ordliste=[]
    for i in newTextList:
        ordliste.append(i.split())      #denne splitter ord 
    wordList=[item for sublist in ordliste for item in sublist] #denne flater ut listen, så jeg ikke får liste i liste med ord
    return wordList

def countWords(wordList):
    from collections import Counter
    counts = dict(Counter(wordList))    #Denne teller antall ganger et ord forekommer og gjør om til dictionary
    return counts

def getMostFrequent(wordList, notcount, toppnr):
    import operator
    for i, line in enumerate(notcount):     #Denne kjører for hvert ord vi ikke skal ha med
        if line in wordList:                #den her sjekker om ordet vi ikke skal ha med er i lista
            wordList.pop(line)              #Hvis ordet er i lista, fjernes det
    topFreqWords = dict(sorted(wordList.items(), key=operator.itemgetter(1),reverse=True)[:toppnr]) #Den her sorter etter mest brukt, og hvor mange vi vil hap å topp
    return topFreqWords

if __name__ == "__main__":
    specialChars = ['.', ',', ':', ';',  '[', ']', '(', ')', "'s", '"',
                    '*', '&', '!', '?'] 
    englPrep = ['about', 'beside', 'near', 'to', 'above', 'between', 'of', 
                'towards', 'across', 'beyond', 'off', 'under', 'after', 'by',
                'on', 'underneath', 'against', 'despite', 'onto', 'unlike', 
                'along', 'down', 'opposite', 'until', 'among', 'during', 'out', 
                'up', 'around', 'except', 'outside', 'along', 'as', 'for', 
                'over', 'via', 'at', 'from', 'past', 'with', 'before', 'in', 
                'round', 'within', 'behind', 'inside', 'since', 'without', 
                'below', 'into', 'than', 'beneath', 'like', 'through']
    englConj = ['for', 'and', 'nor', 'but', 'or', 'yet', 'so']
    englPronouns = ['you', 'he', 'she', 'him', 'her', 'his', 'hers', 'yours']
    specialWords = ['the']
    fra= '*** START OF THE PROJECT GUTENBERG EBOOK'  #Definerer hvor vi vil starte
    til='*** END OF THE PROJECT GUTENBERG EBOOK'     #Definerer hvor vi vil slutte
    fil='pg7163.txt'  #Definerer filen vi vil lese
    n=50              #Antall ord vi vil hapå topp lista 
    notcount=(englPrep + englConj + englPronouns+ specialWords) #Setter alle ord vi ikke vil ha i en liste
    
    #Her bruker vi funskjonene, og kan hente ut det vi vil etter den funksjonen vi vil
    a=loadBook(fil,fra,til)
    b=removeNL_and_doLowerCase(a)
    c=doubleDashToSpace(b)
    d=deleteSpecChar(c,specialChars)
    e=splitter(d)
    f=countWords(e)
    g=getMostFrequent(f,notcount,n)
    
    