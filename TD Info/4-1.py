# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 12:47:08 2018

@author: lucasad
"""

import  math

def f(x):
    return  -x
    
def  zero_dichotomie(a, b, epsilon ):
    if f(a)/abs(f(a)) == f(b)/abs(f(b)):
        raise RuntimeError("La fonction n'a pas de solution")
    
    if(f(a) > 0 and f(b) <= 0):
        z = a
        a = b
        b = z
    
    while abs(b - a) > epsilon:
        pivot = (a + b) / 2
        value = f(pivot)
        if value  <= 0:
            a = pivot
        else:
            b = pivot
    return a
    
print("Solution :", math.pi / 6)
print("Approximation à 0.00001  pres :",zero_dichotomie (-1, 1, 0.00001))
print("Erreur :",math.pi / 6 - zero_dichotomie (-1, math.pi / 2, 0.00001))