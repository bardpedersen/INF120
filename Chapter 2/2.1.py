#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:24:26 2021

@author: Bard
"""

for f in range(0, 101, 10):
    c = 5 / 9 * (f - 32)
    cn = (f-30)/2
    print(f"{f:3.0f}°F = {c:6.2f}°C")

print('')

for f in range(0, 101, 10):
    c = 5 / 9 * (f - 32)
    cn = (f-30)/2
    print(f"{f:3.0f}°F = {c:6.2f}°C = {cn:6.2f}°C")