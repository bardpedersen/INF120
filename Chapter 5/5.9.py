#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:00:44 2021

@author: Bard
"""

from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show

g = 9.81
Vo= 10
t = linspace(0, 2*Vo/g)
y = lambda t: Vo*t-1/2*g*t**2


plot(t, y(t))
xlabel('tid [s]')
ylabel('høyde [m]')
show()

