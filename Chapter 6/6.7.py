#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 21 09:44:07 2021

@author: Bard
"""
import requests

data = requests.get("https://raw.githubusercontent.com/hplgit/scipro-primer/master/src/dictstring/human_evolution.txt").text.splitlines()[3:-3]
humans = {row[:19].strip(): {
    'when': row[21:34].strip(),
    'height': row[37:46].strip(),
    'mass': row[50:58].strip(),
    'brain volume': row[62:].strip()
} for row in data}
print(humans)