# -*- coding: utf-8 -*-

# Exercice 6

L1 = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
      "août", "septembre", "octobre", "novembre", "décembre"]
L2 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def intercalage(l1,l2):
    liste = [] 
    for i in range(min(len(l1), len(l2))):
        liste.append(l1[i])
        liste.append(l2[i])
    
    return liste
        

#print (intercalage(L1,L2))

# Résultat attendu
# ['janvier', 31, 'février', 28, 'mars', 31, 'avril', 30, 'mai', 31,
# 'juin', 30, 'juillet', 31, 'août', 31, 'septembre', 30, 'octobre', 31,
# 'novembre', 30, 'décembre', 31]
