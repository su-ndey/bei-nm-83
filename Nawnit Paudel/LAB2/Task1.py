import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x - 2

x0 = 1
x1 = 2
tolerance = 0.0001
max_iter = 100

for i in range(max_iter):

    denominator = f(x1) - f(x0)

    if denominator == 0:
        print("Division by zero encountered.")
        break

    x2 = x1 - (f(x1) * (x1 - x0)) / denominator

    print(f"Iteration {i + 1}: x = {x2}")

    if abs(x2 - x1) < tolerance:
        print("Approximate root:", x2)
        break

    x0 = x1
    x1 = x2


x = np.linspace(-3, 3, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = x^3 - x - 2')
plt.axhline(0, color='black')
plt.grid(True)
plt.legend()

plt.title("Graph of Nonlinear Equation")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()
