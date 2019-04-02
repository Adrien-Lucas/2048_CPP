import naive_gauss  as g
import numpy  as np

auto=np.linalg.solve(np.array([[1,1/4,0,0],[1,5/4,12,0], [1,1/3,1,1], [1,5/4,13,1]]), np.array([0, 0, 1E16, 0]))
#print(g.solve(np.array([[1,1/4,0,0],[1,5/4,12,0], [1,1/3,1,1], [1,5/4,13,1]]), np.array([0, 0, 1E16, 0])))
#g.affiche_ecart("Auto ", auto, "naive", naive)

def it(f, n, x):
    r = x
    for i in range(0, n):
        r = f(r)
    return r
    
def succ(x):
    return  x+1
    
def double(x):
    return it(succ , x, x)
    
print(it(succ, 10, 3))
print(it(double, 10, 3))
