import math
import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x * math.sin(x) + math.cos(x)

x0 = 2.0
x1 = 3.0

def secant_method(x0, x1, tol=0.000001, max_iter=100):
    f0 = f(x0)
    f1 = f(x1)

    for iteration in range(1, max_iter + 1):
        if abs(f1 - f0) < 0.00001:
            print ("Division by zero in secant method")

        x2 = x1 - f1 * (x1 - x0) / (f1 - f0)
        f2 = f(x2)

        if abs(x2 - x1) < tol and abs(f2) < tol:
            return x2, iteration

        x0, f0 = x1, f1
        x1, f1 = x2, f2

    print (f"This method did not converge after {max_iter} iterations")

root, iterations = secant_method(x0, x1)
print(f"Root found: {root}")
print(f"Iterations = {iterations}")

x = np.linspace(-2, 5, 1000)
y = [f(xi) for xi in x]

plt.figure(figsize=(10, 6))
plt.plot(x, y, 'b-', linewidth=2, label='f(x) = x·sin(x) + cos(x)')
plt.plot(root, f(root), 'ro', markersize=6, label=f'Root: x ≈ {root}')
plt.plot(x0, f(x0), 'go', markersize=4, label=f'Initial x0 = {x0}')
plt.plot(x1, f(x1), 'go', markersize=4, label=f'Initial x1 = {x1}')
plt.grid(True)
plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Secant Method for Finding Root of x sin(x) + cos(x)')
plt.show()
