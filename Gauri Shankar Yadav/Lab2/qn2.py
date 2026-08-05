import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return x * np.sin(x) + np.cos(x)

def df(x):
    return x * np.cos(x)

x0 = float(input("Enter initial guess: "))

tolerance = 0.0001
max_iter = 100

for i in range(max_iter):

    derivative = df(x0)

    if derivative == 0:
        print("Derivative became zero.")
        break

    x1 = x0 - f(x0) / derivative

    if abs(x1 - x0) < tolerance:
        print("\nApproximate Root =", x1)
        print("Number of Iterations =", i + 1)
        break

    x0 = x1
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