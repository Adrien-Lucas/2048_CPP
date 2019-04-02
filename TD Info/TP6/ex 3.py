# -*- coding: utf-8 -*-
"""
Created on Thu Mar 29 13:14:18 2018

@author: lucasad
"""

f = open('donnees-2-colonnes.csv', 'r')
out_file = open('resultats.csv', 'w')
ligne = f.readline()

pos = 0
t = 0
v = 0

while ligne != '':
    ligne = ligne.split(',')
    pos = pos + (float(ligne[0]) - t)*((v + float(ligne[1])) / 2)
    t = float(ligne[0])
    v = float(ligne[1])
    print(t, v, pos)
    out_file.write(str(t) + "," + str(pos) + '\n')
    ligne = f.readline()

out_file.close()