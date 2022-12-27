#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 11:48:25 2021

@author: Bard
"""
from math import factorial

def binomial(x, n, p):
    return factorial(n)/(factorial(x)*factorial(n-x)) *p**x *(1-p)**(n-x)
print(binomial)
    