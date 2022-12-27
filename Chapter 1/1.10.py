#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:19:28 2021

@author: Bard
"""
from math import sqrt, pi, exp

m = 0   
s = 2    
x = 1    
f = 1 / sqrt(2 * pi) / s * exp(-1 / 2 * ((x - m) / s)**2)
print(f)