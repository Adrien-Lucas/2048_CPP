# -*- coding: utf-8 -*-

# Exercice 8

def fusion(l1, l2):
    """ L1 et L2 sont deux listes triées dans l'ordre croissant
        cette fonction fusionne L1 et L2 dans une nouvelle liste L3
        triée dans le même ordre, et elle retourne L3
    """
    L3 = l1 + l2
    L4 = []
    
    while(len(L3) != 0):
        mini = L3[0]
        i = 0
        for j in range(len(L3)):
            if L3[j] < mini:
                mini = L3[j]
                i = j
        L4.append(L3[i])
        del L3[i]

    # Compléter la fonction

    return L4


# Pour tester votre programme
L1 = [5, 7, 25]
L2 = [3, 15, 16, 17, 20]
print (fusion(L1, L2))  # Résultat attendu : [3, 5, 7, 15, 20, 25]
