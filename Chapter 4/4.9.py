#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:42:52 2021

@author: Bard
"""

v0 = float(input("v0 = ")) 
t = float(input("t = "))
g = 9.81
y = v0*t - 0.5*g*t**2
print(y)