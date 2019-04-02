import math

def pythagore (x, y) :
    return (math.sqrt(x ** 2 + y ** 2))
    
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

def egyptian (x, y):
    result = 0
    while(x > 1):
        if x/2 != int(x/2):
            result += y
        x = int(x/2)
        y *= 2
        
    return y + result

def pgcd_euclide(x, y):
    if y > x :
        z = x
        x=y
        y=z
        
    reste = -1
    while(reste != 0):
        q = int(y / x)
        reste = y - q*x
        y = x      
        if reste != 0:
            x = reste
    return x
