# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 13:05:12 2018

@author: lucasad
"""
import math

def f(x) :
    return x*math.sin(x**2)

def integrale_trapeze(a, b, n):
    somme = 0.
    for i in range (1, n+1):
        somme += f(a + i*((b-a)/n))
    return ((b-a)/(n))*somme
    
def erreur(n) :
    return 1. - integrale_trapeze(0, math.sqrt(math.pi), n)   

import  pylab

n = range(2, 31)
s = list(map(erreur ,n))
pylab.plot(n, s)
pylab.show()