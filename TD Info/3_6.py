# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 13:24:27 2018

@author: lucasad
"""

import math

n = 10000000
z = 0

somme = 0.0
c = 0.0
for e in range(1, n):
    y = 1./(e ** 2) - c
    # Puis on  ajoute  ce  nombre à somme :
    t = somme + y
    # Mais si y était  petit  et somme  grand , on a probablement  fait  une
    # erreur. Calculons  cette  erreur (attention  aux  parenthèses) pour
    # la  compenser  lors du  calcul  du terme  suivant.
    c = (t - somme) - y
    somme = t
    #z = z + 1./(i ** 2)
    
print(((math.pi** 2)/6.) - somme)
#print(somme)