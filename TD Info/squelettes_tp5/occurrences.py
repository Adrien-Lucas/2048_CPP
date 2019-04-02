# -*- coding: utf-8 -*-

# Exercice 4


def occurrence(liste, valeur):
    """ Retourne l'indice de la première
        occurrence de 'valeur' dans 'liste' """

    for i in range(len(liste)):
        if(liste[i] == valeur):
            return i

    return None


# Exercice 5
def nb_occurrences(liste, valeur):
    """ Retourne le nombre d'occurrences de 'valeur' dans 'liste' """
    nb = 0
    for i in range(len(liste)):
        if(liste[i] == valeur):
            nb += 1

    return nb


# Pour tester votre programme

liste = [-4, 3, 7, 3]
print(occurrence(liste, 7))  # doit afficher 2
print(occurrence(liste, 3))  # doit afficher 1
print(occurrence(liste, 5))  # doit afficher None
print(nb_occurrences(liste, 3))
