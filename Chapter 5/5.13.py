#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:21:17 2021

@author: Bard
"""

from numpy import tan, cos, linspace, pi, sin, sqrt
from matplotlib.pyplot import plot, show 

g=9.81
y0 = float(input("y0 = "))
phi = float(input("phi = ")) * pi / 180
v0 = float(input("v0 = "))
root = v0 * cos(phi) / g * (v0*sin(phi) + sqrt(2*g*y0 + (v0**2 * sin(phi)**2)))
x = linspace(0, root)

f = lambda x: x*tan(phi) - 1/(2*v0**2) * (g*x**2)/cos(phi)**2 + y0

plot(x,f(x))
show()