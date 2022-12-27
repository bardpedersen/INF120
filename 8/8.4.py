#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:39:02 2021

@author: Bard
"""
import numpy as np
import random
hat = 10*['red'] + 10*['blue'] + 10*['yellow'] + 10*['purple']
N = 100000
M = 0
for _ in range(100000):
    draw = [random.choice(hat) for _ in range(10)]
    success = draw.count('blue') == 2 and draw.count('purple') == 2
    M += success
p = M / N
print(f"The probability is approximately {100*p}%")