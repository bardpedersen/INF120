#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 14:11:30 2021

@author: Bard
"""

from numpy import linspace
from matplotlib.pyplot import plot, xlabel, ylabel, show, figure, legend

F = linspace(-20, 120)
Cu =  (F-30)/2
Cn =  (F-32)*5/9

figure()
plot(F, Cn)
plot(F, Cu)
xlabel('Farenhet [º]')
ylabel('Celsius [º]')
legend(["Tilnærmet", "Nøyaktig"])
show()
