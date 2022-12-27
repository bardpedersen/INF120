#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 11:55:26 2021

@author: Bard
"""
import numpy as np

N = 10000
tails = np.sum(np.random.randint(2, size=N))    # tails = 1
print(tails)