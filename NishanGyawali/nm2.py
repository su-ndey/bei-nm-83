import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1


x0 = float(input("Enter initial guess: "))
tol = 0.001
iterations = []

for i in range(10):
    x1 = x0 - f(x0)/df(x0)
    iterations.append(x1)

    if abs(x1 - x0) < tol:
        break
    x0 = x1


x = np.linspace(0, 3, 100)
y = f(x)

plt.figure()
plt.plot(x, y)
plt.axhline(0)