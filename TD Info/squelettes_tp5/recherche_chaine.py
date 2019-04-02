# -*- coding: utf-8 -*-

# Exercice 1


def coincide(t, i, m):
    """ Renvoie True si la sous-chaine de <t> démarrant à l'indice <i> et 
        de la même longueur que <m> est égale à <m>
    """
    a = 0
    while(a < len(m) and t[i+a] == m[a]):
        a += 1
        
    if(a == len(m)):
        return True
    return False


# Exercice 2
def recherche_mot(m, t):
    """ Renvoie l'indice de <t> où se commence le mot <m> s'il existe
        et None sinon.
    """
    a = 0
    r = 0
    for i in range(len(t)):
        if(t[i] == m[a]):
            if(a == 0):
                r = i
            
            a += 1
            if(a == len(m)):
                return r
        else :
            a = 0

    return None


# Pour tester votre programme

print(coincide("ceci est un test de texte", 12, "test"))  # doit afficher : True
print(recherche_mot("test", "ceci est un test de texte"))  # doit afficher : 12
print(recherche_mot("test", "test"))  # doit afficher : 0
print(recherche_mot("test", "tesxteststests"))  # doit afficher : 4
