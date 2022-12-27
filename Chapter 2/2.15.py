#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 12:32:22 2021

@author: Bard
"""


q = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h']]

print(q[0][0])
print(q[1])
print(q[-1][-1])
print(q[1][0])


for i in q:    # i = første liste
    for j in range(len(i)):    # j = nummer i listene
        print(i[j])