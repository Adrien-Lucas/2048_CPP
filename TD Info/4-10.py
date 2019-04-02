# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:45:24 2018

@author: lucasad
"""

L = [1, -5, 4, 4, 15, 6, 7, 8]

def max_list(l):
    maximum = l[0]
    for e in l:
        if e > maximum:
            maximum = e
    return maximum

def min_list(l):
    minimum = l[0]
    for e in l:
        if e < minimum:
            minimum = e
    return minimum
    
print("max : ", max_list(L))
print("min : ", min_list(L))