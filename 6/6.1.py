#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:27:29 2021

@author: Bard
"""
import requests

def get_constants():
    data = requests.get("https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/dictstring/constants.txt").text
    return {' '.join(row[:-2]): float(row[-2]) for row in [line.split() for line in data.splitlines()[2:]]}
    
print(get_constants())


