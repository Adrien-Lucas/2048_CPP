import numpy

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[1, 1, 1],
     [2, 2, 2]]

C = [[1, 2],
     [3, 4],
     [5, 6],
     [7, 8]]




def afficher_matrice(m):
    ret = ''
    for x in m:
        ret += '['
        for y in x:
            ret += ' ' + str(y) + ' '
        ret += ']\n'
    print(ret)
            

def creer_matrice(n,m):
    return numpy.zeros([n, m])

def addition(m1, m2):
    m = creer_matrice(len(m1), len(m1[0]))
    for x in range(len(m)):
        for y in range(len(m[0])):
            m[x][y] = m1[x][y] + m2[x][y]
    return m
    print("À FAIRE : addition des matrices m1 et m2")

print('A =')
afficher_matrice(A)
print('B =')
afficher_matrice(B)
print('C =')
afficher_matrice(C)
print('A + B =')
afficher_matrice(addition(A, B))
