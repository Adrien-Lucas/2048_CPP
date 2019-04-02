# -*- coding: utf-8 -*-

# Exercice 7
import intercalage

def nb_melanges(paquet):
    L1 = []
    for i in range(paquet):
        L1.append(i)
    
    L2 = list(L1)
    n = 0
    while(L2 != L1 and n != 0):
        L3 = []
        L4 = []
        for i in range(len(L1)):
            
    
# Écrivez votre programme ici (vous pouvez peut-être utiliser une fonction intermédiaire qui réalise un seul mélange...)



print(nb_melanges(2)) # devrait renvoyer 1
print(nb_melanges(4)) # devrait renvoyer 2

# à calculer :
#print(nb_melanges(8))
#print(nb_melanges(12))
#print(nb_melanges(32))
#print(nb_melanges(52))


