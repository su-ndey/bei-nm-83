import math
import matplotlib.pyplot as plt
import numpy as np

def secant(f, x0, x1, tol=1e-7, ite=100):
    for i in range(ite):
        f_x0 = f(x0)
        f_x1 = f(x1)
        if abs(f_x1 - f_x0) < tol:
            break
        xn = x1 - f_x1 * (x1 - x0) / (f_x1 - f_x0)
        x0, x1 = x1, xn
        if abs(x1 - x0) < tol:
            break
    return x1

func = lambda x: x * np.sin(x) + np.cos(x)
root = secant(func, 2.5, 3)
print("found root", root)

x = np.linspace(-3, 3, 400)
y = func(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x)=x*sin(x)+cos(x)')
plt.axhline(0, color='black', linewidth=0.8)
plt.legend()
plt.show()