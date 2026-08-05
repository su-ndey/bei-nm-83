import matplotlib.pyplot as plt
import numpy as np
def f(x):
    return x * np.sin(x) + np.cos(x)
x0 = float(input("Enter first guess (x0): "))
x1 = float(input("Enter second guess (x1): "))
tolerance = 0.0001
max_iter = 100
for i in range(max_iter):
    denominator = f(x1) - f(x0)

    if denominator == 0:
        print("Division by zero encountered.")
        break

    x2 = x1 - (f(x1) * (x1 - x0)) / denominator

    if abs(x2 - x1) < tolerance:
        print("\nApproximate Root =", x2)
        print("Number of Iterations =", i + 1)
        break
    x0 = x1
    x1 = x2
else:
    print("Method did not converge.")

# Graph
x = np.linspace(-10, 10, 1000)
y = f(x)
plt.figure(figsize=(8, 5))
plt.plot(x, y, label='f(x) = xsin(x) + cos(x)')
plt.axhline(0)
plt.grid(True)
plt.legend()
plt.title("Graph of Nonlinear Equation")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.show()