
def pythagore (x, y) :
    return (x ** 2 + y ** 2) ** 0.5
    
def max2(x, y) :
    if(x >= y):
        return x
    else :
        return y

def max3(a, b, c):
    return max2(a, max2(b, c))    
    
def multiplication (x, y):
    if y > x :
        z = x
        x=y
        y=z
    
    resultat = 1
    for i in range (0, y):
        resultat = resultat + x
        print("Dans la boucle, resultat =", resultat)
    
    print("Résultat :", resultat)

def puissance(x, y):
    resultat = 1
    for i in range (0, y):
        resultat = resultat * x
        print("Dans la boucle, resultat =", resultat)
    
    print("Résultat :", resultat)


