import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 2

def derivative(f, x, h=1e-6):
    return (f(x + h) - f(x - h)) / (2 * h)

def newton_raphson(f, x0, tol=1e-6, max_iter=100):
    x = x0

    for _ in range(max_iter):
        x_new = x - f(x) / derivative(f, x)

        if abs(x_new - x) < tol:
            return x_new

        x = x_new

    return x

root = newton_raphson(f, 1.5)

x = np.linspace(-2, 2, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label=r'$f(x)=x^3-x-2$')
plt.axhline(0, color='black', linewidth=0.8)

plt.scatter(root, f(root), color='red', zorder=5,
            label=f'Root ≈ {root:.6f}')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Newton-Raphson Root Visualization')
plt.grid(True)
plt.legend()
plt.show()

print("Root:", root)