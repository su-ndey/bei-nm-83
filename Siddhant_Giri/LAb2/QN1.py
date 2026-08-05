import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x**3 - x - 2

def df(x):
    return 3 * x**2 - 1

x0 = 1.5
tolerance = 0.0001
max_iter = 100

for i in range(max_iter):

    derivative = df(x0)

    if derivative == 0:
        print("Derivative became zero.")
        break

    x1 = x0 - f(x0) / derivative

    print(f"Iteration {i + 1}: x = {x1}")

    if abs(x1 - x0) < tolerance:
        print("Approximate root:", x1)
        break

    x0 = x1

x = np.linspace(-3, 3, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = x^3 - x - 2')
plt.axhline(0)
plt.grid(True)
plt.legend()

plt.title("Graph of Nonlinear Equation")
plt.xlabel("x")
plt.ylabel("f(x)")

plt.show()