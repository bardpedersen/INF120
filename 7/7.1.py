#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:49:37 2021

@author: Bard
"""

class F:
    def __init__(self,a,w):
        self.a = a
        self.w = w
        
    def __call__(self,x):
        from math import exp, sin
        return exp(-self.a * x) * sin(self.w * x)
    
    
f = F(a=1, w=0.1)
from math import pi
f(pi)