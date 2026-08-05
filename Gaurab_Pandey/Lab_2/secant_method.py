import math
import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x * math.sin(x) + math.cos(x)

start = 2.0
end = 3.0

def secant_method(a, b, tol=1e-6, max_iter=100):
    fa = f(a)
    fb = f(b)

    count = 1
    while count <= max_iter:
        if abs(fb - fa) < 1e-5:
            print("Division by zero in secant method")

        c = b - fb * (b - a) / (fb - fa)
        fc = f(c)

        if abs(c - b) < tol and abs(fc) < tol:
            return c, count

        a, fa = b, fb
        b, fb = c, fc
        count += 1

    print(f"This method did not converge after {max_iter} iterations")


root, iterations = secant_method(start, end)

print(f"Root found: {root}")
print(f"Iterations = {iterations}")

x_values = np.linspace(-2, 5, 1000)
y_values = [f(val) for val in x_values]

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, color='b', linewidth=2, label='f(x) = x·sin(x) + cos(x)')
plt.scatter(root, f(root), color='r', s=40, label=f'Root: x ≈ {root}')
plt.scatter(start, f(start), color='g', s=25, label=f'Initial x0 = {start}')
plt.scatter(end, f(end), color='g', s=25, label=f'Initial x1 = {end}')

plt.xlabel('x', fontsize=12)
plt.ylabel('f(x)', fontsize=12)
plt.title('Secant Method for Finding Root of x sin(x) + cos(x)')
plt.grid(True)
plt.legend()
plt.show()