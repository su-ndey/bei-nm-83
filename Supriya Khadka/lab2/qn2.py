import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

x0 = float(input("Enter initial guess: "))
n = int(input("Enter number of iterations: "))

print("\nStep\t x\t\t f(x)")
for i in range(1, n+1):
    x1 = x0 - f(x0)/df(x0)
    print(f"{i}\t {x1:.6f}\t {f(x1):.6f}")
    x0 = x1

print(f"\nApproximate root after {n} iterations: {x1:.6f}")

# Graphical representation
x = np.linspace(-3, 3, 400)
y = f(x)

plt.figure(figsize=(8, 5))
plt.plot(x, y, label="f(x) = x^3 - x - 2")
plt.axhline(0, color="black")  # x-axis
plt.scatter(x1, f(x1), color="red", zorder=5, label="Approximate Root")
plt.title("Newton-Raphson Method")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.legend()
plt.show()
