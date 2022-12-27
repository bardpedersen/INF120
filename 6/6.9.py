#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:45:28 2021

@author: Bard
"""
def triangle_area(v):
    return 1/2 * abs(v[2][0]*v[3][1] - v[3][0]*v[2][1] - v[1][0]*v[3][1] + v[3][0]*v[1][1] + v[1][0]*v[2][1] - v[2][0]*v[1][1])

print(triangle_area({1: (0,0), 2: (1,0), 3: (0,2)}))