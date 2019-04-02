"""Fichier d'exemple en Python.

 Pour exécuter ce programme, faites :
   python factorielle.py
 Le code sera interprété par python.

 Ce fichier calcule une factorielle de plusieurs manieres."""


def f_rec(nbr):
    """ version recursive inefficace. """
    if nbr <= 1:
        return 1
    else:
        return f_rec(nbr-1) * nbr


def f_term(nbr, acc):
    """ version recursive terminale """
    if nbr <= 1:
        return acc
    else:
        return f_term(nbr-1, acc * nbr)


def f_imperative(nbr):
    """ version iterative """
    res = 1

    for i in range(2, nbr+1):
        res = res * i

    return res

# Procédure principale
if __name__ == "__main__":

    try:
        NBR_LU = int(input("Entrez une valeur : "))
    except ValueError:
        print("Ce n'est pas un nombre.")
        exit(-1)

    print("La factorielle (calculee recursivement) de " +
          str(NBR_LU) +
          " est : " +
          str(f_rec(NBR_LU)) +
          ".")

    print("La factorielle"
          " (calculee avec une fonction recursive terminale) de " +
          str(NBR_LU) +
          " est :" +
          str(f_term(NBR_LU, 1)) +
          ".")
    print("La factorielle (calculee avec une boucle) de " +
          str(NBR_LU) +
          " est : " +
          str(f_imperative(NBR_LU)) +
          ".")
