x = 5
y = 6

print("Avant multiplication : x =", x, "et y =", y)
"""
if y > x :
    z = x
    x=y
    y=z
"""
resultat = 1
for i in range (0, y):
    resultat = resultat * x
    print("Dans la boucle, resultat =", resultat)

print("Résultat :", resultat)

