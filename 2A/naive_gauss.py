"""Une version naïve du pivot de Gauss,
   qu'il faut chercher à améliorer"""

import numpy


def solve_triangular(A, b):
    assert A.ndim == 2
    assert b.ndim == 1
    n = len(b)
    x = numpy.zeros([n])
    for i in range(n - 1, -1, -1):
        x[i] = (b[i] - numpy.dot(A[i, :], x)) / A[i, i]
    return x


def pivot_index(A, i):
    n = A.shape[0]  # nombre de lignes
    m = 0
    mk = 0
    for k in range(i, n):
        if A[k, i] != 0.0 and A[k,i] > m:
            m = A[k,i]
            mk = k
    return mk
    raise ValueError("Oops, aucun pivot non-nul disponible")


def swap_lines(A, i, j):
    tmp = A[i, :].copy()
    A[i, :] = A[j, :]
    A[j, :] = tmp


def transvection_lines(A, i, k, factor):
    A[k, :] = A[k, :] + A[i, :] * factor


def gauss(A0, b0):
    A = A0.copy()  # pour ne pas détruire A
    b = b0.copy()
    print("A :\n", A, "\nB :\n", b)
    assert A.ndim == 2
    assert b.ndim == 1
    n = len(b)
    assert A.shape[0] == n
    assert A.shape[1] == n
    for i in range(n - 1):
        input ("Appuyez  sur  une  touche  pour  continuer ...")
        # choix du pivot
        ipiv = pivot_index(A, i)
        print("Nouveau pivot : \n", A[ipiv])
        # echanges
        if ipiv != i:
            swap_lines(A, i, ipiv)
            tmp = b[ipiv]
            b[ipiv] = b[i]
            b[i] = tmp
        # pivotage
        for k in range(i + 1, n):
            factor = -A[k, i] / A[i, i]
            transvection_lines(A, i, k, factor)
            b[k] = b[k] + b[i] * factor
            print("A : " , A , "\nB: " , b)
    return [A, b]


def solve(A0, b0):
    Ab = gauss(A0, b0)
    return solve_triangular(Ab[0], Ab[1])


def affiche_ecart(nom1, x1, nom2, x2):
    """Affiche l'écart entre deux vecteurs 'x1' et 'x2'
       'nom1' et 'nom2' sont deux chaînes de caractères 
       qui servent à nommer ces vecteurs."""
    assert x1.ndim == 1
    assert x2.ndim == 1
    print(nom1, x1)
    print(nom2, x2)
    msg = nom1 + "-" + nom2
    print("Ecart", msg , x1 - x2)
    print("Norme de l'ecart", msg, numpy.linalg.norm(x1 - x2))
    print()
