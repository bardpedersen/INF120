#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:56:26 2021

@author: Bard
"""

from numpy import sqrt, exp, pi, linspace, zeros
from matplotlib.pyplot import plot, show, xlabel, ylabel
import matplotlib.pyplot as plt


h = lambda x: 1 / sqrt(2 * pi) * exp(-1/2 * x**2)
xlist = linspace(-4, 4, 41)
hlist = [h(x) for x in xlist]
print(hlist)

x = y = zeros(41)
x_ = -4
dx = 8 / 40
for i in range(41):
    x[i] = x_
    y[i] = h(x_)
    x_ += dx
print(y)

x = linspace(-4, 4, 41)
y = h(x)

plt.plot(x, y)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

