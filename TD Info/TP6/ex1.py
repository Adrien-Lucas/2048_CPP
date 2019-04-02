# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 12:58:03 2018

@author: lucasad
"""


f = open('donnees.txt', 'r')
ligne = f.readline()

somme = 0
i = 0

while ligne != '':
    print("ligne =", ligne)
    somme += float(ligne)
    i += 1    
    ligne = f.readline()

print(somme / i)
    