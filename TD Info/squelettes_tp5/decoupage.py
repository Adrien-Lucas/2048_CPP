# -*- coding: utf-8 -*-

# Exercice 9

L = [35, 72, -5, 50, 24, 19]
Lpaire = []
Limpaire = []

for i in range(len(L)):
    if(L[i]%2 == 0):
        Lpaire.append(L[i])
    else:
        Limpaire.append(L[i])
# Écrivez votre programme ici
# pour mettre tous les nombres pairs de L dans Lpaire,
# et les impairs dans Limpaire

print (Lpaire)
print (Limpaire)
