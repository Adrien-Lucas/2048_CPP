# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 12:52:25 2018

@author: lucasad
"""

print("Entrez  la  premiere  valeur :")
x =int(input())
maximum = x
# ...

while x  >= 0:
    # ...
    print("Entrez  la  valeur  suivante :")
    x = int(input())
    if x > maximum :
        maximum = x
        
print("Le  maximum  est :", maximum)
