#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:34:07 2021

@author: Bard
"""
import random
def random_color(n):
    colors = ['Green', 'Red', 'Blue', 'Yellow', 'Orange', 'White', 'Black', 'Purple']
    for i in range(n):
        r = random.choice(colors)
        print(r)