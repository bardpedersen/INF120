#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:39:12 2021

@author: Bard
"""
F = list(range(0, 101, 10))
C_approx = [(f - 30) / 2 for f in F]
C = [5 / 9 * (f - 32) for f in F]
"""
C = list()
for i in range(len(F)):         Alternativ til C
    c = 5/9 * (F[i]-32)
    C.append(c)
 """   

l = [F, C, C_approx]
ferdig=list()

for i in range(len(F)):
    print(f"{l[0][i]:3.0f}°F = {l[1][i]:6.2f}°C = {l[2][i]:3.0f}°C")
ferdig.append(F)
ferdig.append(C)
ferdig.append(C_approx)
