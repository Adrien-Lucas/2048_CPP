import math

def f(x):
    return math.sin(x) - 0.5

def zero_dichotomie(a, b, epsilon):
    while b - a > epsilon:
        pivot = (a + b) / 2
        value = f(pivot)
        if value <= 0:
            a = pivot
        else:
            b = pivot
    return a

print("Solution :", math.pi / 6)
print("Approximation à 0.00001 pres :",
      zero_dichotomie(-1, math.pi / 2, 0.00001))
print("Erreur :", 
      math.pi / 6 - zero_dichotomie(-1, math.pi / 2, 0.00001))
