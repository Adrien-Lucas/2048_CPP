# -*- coding: utf-8 -*-
"""
Created on Thu Mar  1 14:09:46 2018

@author: lucasad
"""

from random import random
import mesmaths

n = 10000000
z = 0

for i in range(0,n):
    x = random()
    y = random()
    if(mesmaths.pythagore(x, y) <= 1):
        z += 1
        
print((z/n)*4)