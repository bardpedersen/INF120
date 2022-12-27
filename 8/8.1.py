#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:56:04 2021

@author: Bard
"""

import random
def dice(n):
    head=0
    tail=0
    for i in range(n):
        r = random.randint(0,1)
        if r > 0.5:
            print('head')
            head+=1
        else:
            print('tail')
            tail+=1
    print('tail = ',tail )
    print('heads = ', head)