import matplotlib.pyplot as plt
import numpy as np

plt.title("Le graphe de l'ambiance")
plt.xlabel("Axe x")
plt.ylabel("Axe y")

p = 500
q = 10000

t = np.linspace(0, 2*q*np.pi, 10000)
x = (1+np.cos((p/q)*t))*np.cos(t)
y = (1+np.cos((p/q)*t))*np.sin(t)

plt.plot(x, y)