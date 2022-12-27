#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:52:50 2021

@author: Bard
"""
import random
#%%
a = 1/6

#%%
N = 100000
M = 0
for _ in range(N):
    M += random.randint(1, 6) == 6
print(M/N)
print(1/6)

#%%
N = 100000
M = 0
for i in range(N):
    s = 0
    for ii in range(4):
        s += random.randint(1, 6) == 6
    M += s == 4
print(M/N)
print((1/6)**4)

#%%
s = 0
while s < 3:
    s += random.randint(1, 6) == 6
N = 100000
M = 0
for _ in range(N):
    M += random.randint(1, 6) == 6
print(M/N)
print(1/6)
