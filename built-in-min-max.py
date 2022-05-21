# -*- coding: utf-8 -*-
"""
Created on Sat May 21 14:30:45 2022

@author: sande
"""

min(15, 9, 27, 14)

max(12, 27, 36)

def minimum(val1, val2, val3):
    min_val = val1
    if val2 < min_val:
        min_val = val2
    if val3 < min_val:
        min_val = val3
    return min_val

minimum(2, 5, -1)
