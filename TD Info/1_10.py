# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 13:25:15 2018

@author: lucasad
"""

x = 42
y = 3
print("avant : x =", x, " y =", y)

_x = x
x = y
y = _x

print("après : x =", x, " y =", y)